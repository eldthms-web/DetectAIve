#!/usr/bin/env python3
"""Creator-side packaging smoke test for one DetectAIve case folder.

Usage:
    python3 tools/detectaive_lint.py cases/DA-001

This is intentionally not a game engine or full schema validator. It reads a
local casefile and evidence directory, decodes the sealed JSON capsule, and
reports common packaging mistakes. It never modifies the case.
"""

import base64
import json
import re
import sys
from pathlib import Path
from urllib.parse import urlparse

EVIDENCE_TOKEN_RE = re.compile(r"\bE-(\d+)\b")
CANONICAL_EVIDENCE_ID_RE = re.compile(r"^E-\d{2}$")
ALLOWED_SUSPECT_FIELDS = {
    "name", "role", "status", "public", "private", "disclosures", "interrogation"
}
REQUIRED_SUSPECT_FIELDS = {"name", "role", "public"}


def canonical_id(raw: str) -> str:
    m = EVIDENCE_TOKEN_RE.fullmatch(raw)
    return f"E-{int(m.group(1)):02d}" if m else raw


def walk_strings(obj):
    if isinstance(obj, str):
        yield obj
    elif isinstance(obj, dict):
        for key, value in obj.items():
            if isinstance(key, str):
                yield key
            yield from walk_strings(value)
    elif isinstance(obj, list):
        for item in obj:
            yield from walk_strings(item)


def extract_capsule(text: str) -> tuple[str, dict]:
    marker = "GM_CAPSULE_BASE64"
    if marker not in text:
        raise ValueError("No GM_CAPSULE_BASE64 marker found")
    tail = text.split(marker, 1)[1]
    lines = [line.strip() for line in tail.splitlines() if line.strip()]
    if not lines:
        raise ValueError("GM_CAPSULE_BASE64 marker has no payload")
    b64 = lines[0]
    decoded = base64.b64decode(b64, validate=True).decode("utf-8")
    return decoded, json.loads(decoded)


def main(case_dir: str) -> int:
    case_path = Path(case_dir)
    casefile = case_path / "casefile.txt"
    if not casefile.is_file():
        print(f"ERROR: no casefile.txt found in {case_path}")
        return 2

    text = casefile.read_text(encoding="utf-8")
    try:
        decoded, data = extract_capsule(text)
    except Exception as exc:
        print(f"ERROR: cannot decode sealed capsule: {exc}")
        return 2

    errors = []
    warnings = []
    notes = []
    print(f"=== DetectAIve lint: {data.get('id', case_path.name)} — {data.get('title', '')} ===\n")

    # Evidence IDs: catch both dangling references and inconsistent spelling.
    defined_raw = set(data.get("evidence", {}).keys())
    defined = {canonical_id(eid) for eid in defined_raw}
    for eid in sorted(defined_raw):
        if not CANONICAL_EVIDENCE_ID_RE.fullmatch(eid):
            warnings.append(f"registry ID {eid!r} is noncanonical; use {canonical_id(eid)}")

    raw_refs = []
    for section_name in ("flow", "hints", "suspects", "player_moments", "debrief"):
        for value in walk_strings(data.get(section_name)):
            raw_refs.extend(m.group(0) for m in EVIDENCE_TOKEN_RE.finditer(value))

    for raw in sorted(set(raw_refs)):
        canon = canonical_id(raw)
        if raw != canon:
            warnings.append(f"noncanonical evidence reference {raw!r}; use {canon}")
        if canon not in defined:
            errors.append(f"evidence reference {raw!r} has no registry entry ({canon})")

    referenced = {canonical_id(raw) for raw in raw_refs}
    for eid in sorted(defined - referenced):
        warnings.append(f"evidence {eid} is defined but never referenced outside the registry")

    # Evidence files and accessibility fallback.
    for eid, entry in data.get("evidence", {}).items():
        url = entry.get("url")
        if not url:
            errors.append(f"{eid}: missing evidence url")
        else:
            fname = Path(urlparse(url).path).name
            if not fname or not (case_path / "evidence" / fname).is_file():
                errors.append(f"{eid}: URL basename {fname!r} not found in evidence/")
        if not entry.get("accessibility_fallback"):
            warnings.append(f"{eid}: no accessibility_fallback (recommended, not launch-blocking)")

    # Suspect packet boundary: asymmetric content is fine; unclear top-level
    # private facts are what we want to catch.
    suspects = data.get("suspects", {})
    for sid, suspect in suspects.items():
        missing = REQUIRED_SUSPECT_FIELDS - set(suspect)
        if missing:
            errors.append(f"{sid}: missing required public identity field(s): {', '.join(sorted(missing))}")
        extras = set(suspect) - ALLOWED_SUSPECT_FIELDS
        if extras:
            warnings.append(
                f"{sid}: top-level field(s) {', '.join(sorted(extras))} bypass public/private/disclosure grouping"
            )
        disclosures = suspect.get("disclosures", [])
        if disclosures is not None and not isinstance(disclosures, list):
            errors.append(f"{sid}: disclosures must be a list")
        elif isinstance(disclosures, list):
            for idx, disclosure in enumerate(disclosures, 1):
                if not isinstance(disclosure, dict):
                    errors.append(f"{sid}: disclosure #{idx} is not an object")
                    continue
                if not disclosure.get("fact") or not disclosure.get("reveal_when"):
                    errors.append(f"{sid}: disclosure #{idx} needs fact and reveal_when")

    # Context budget: deliberately rough; smoke-test information only.
    rough_tokens = len(text) // 4
    notes.append(f"casefile: {len(text)} chars (~{rough_tokens} rough tokens)")
    notes.append(f"sealed JSON before Base64: {len(decoded)} chars")
    if rough_tokens > 15000:
        warnings.append("casefile exceeds the 15k-token compression-review line")
    elif rough_tokens > 10000:
        warnings.append("casefile is above the 5k–10k soft target")

    if errors:
        print("ERRORS")
        for item in errors:
            print(f"  ✗ {item}")
        print()
    if warnings:
        print("WARNINGS")
        for item in warnings:
            print(f"  ! {item}")
        print()
    print("INFO")
    for item in notes:
        print(f"  · {item}")

    if not errors and not warnings:
        print("\n✓ Packaging smoke test clean.")
    elif not errors:
        print("\n✓ No blocking packaging errors; review warnings before publishing.")
    else:
        print("\n✗ Fix blocking packaging errors before publishing.")
    return 1 if errors else 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(__doc__.strip())
        raise SystemExit(2)
    raise SystemExit(main(sys.argv[1]))
