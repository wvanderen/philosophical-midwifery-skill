#!/usr/bin/env python3
"""Check the completeness of the philosophical-midwifery skill package.

Requirement: EVAL-03 — confirm the shipped package is complete (every required
file present and every expected internal cross-reference resolving) before it is
called v1-ready.

Source of truth: the hardcoded manifest below, derived from the shipped file set
and from ``SKILL.md``'s "Companion references" section (decision D-05 / A-3).
There is no separate manifest file: the rules are encoded directly here, mirroring
the "single source of truth" stance the validator takes with SESSION_SCHEMA.md.
Keep the manifest in sync with the package when files are added or removed.

Structural binding (D-04): this module is a near-verbatim structural copy of
``validate_session_schema.py`` — same module-docstring shape, same stdlib-only
import discipline, same ``validate() -> List[str]`` collect-all signature, same
``main()`` + ``argparse`` + ``--json`` + exit-code block. Only two departures:
there is no positional ``<path>`` argument (the script locates the package root
itself), and the body of ``validate()`` checks presence + cross-references rather
than JSON schema.

Strictness (D-01 continuity): stdlib-only. This module imports ONLY the Python
standard library (``sys``, ``json``, ``argparse``, ``pathlib``). It performs no
network access and uses no code-execution or shell-spawning primitives (stdlib-only
by design).

Output (D-02): default mode prints one human-readable line per error and exits
``0`` when the package is complete, ``1`` otherwise. ``--json`` mode prints a
single ``{"valid": bool, "errors": [...]}`` document with the same exit codes.

Error collection (D-03): every problem is gathered in one pass before any output,
so a user can fix all errors in one round.

Usage:
    check_package.py [--json]
"""

import argparse
import json
import sys
from pathlib import Path
from typing import List

# Every file a complete v1 package must ship, as paths relative to the package
# root (the ``philosophical-midwifery/`` directory). Mirrors the shipped file set
# across Phase 1 (SKILL.md + 3 references), Phase 2 (SESSION_SCHEMA.md, assets,
# validator + schema fixtures), and Phase 3 (EVALUATION_RUBRIC.md, examples/,
# this script). D-05 / A-3.
REQUIRED_FILES = (
    "SKILL.md",
    "references/PATHOLOGOS_PATTERNS.md",
    "references/QUESTION_TAXONOMY.md",
    "references/SAFETY_BOUNDARIES.md",
    "references/SESSION_SCHEMA.md",
    "references/EVALUATION_RUBRIC.md",
    "assets/session_summary_template.md",
    "assets/belief_graph_template.json",
    "scripts/validate_session_schema.py",
    "scripts/check_package.py",
    "scripts/fixtures/valid.json",
    "scripts/fixtures/invalid.json",
    "examples/normal-inquiry.md",
    "examples/overinterpretation-prevention.md",
    "examples/advice-avoidance.md",
    "examples/high-emotion-slowdown.md",
    "examples/safety-boundary-handling.md",
)

# Internal cross-reference map: each package-relative file path is mapped to the
# list of internal-reference substrings it is expected to contain. Derived
# conservatively from the shipped prose (A-3); the SKILL.md entry encodes its
# "Companion references" section verbatim. D-05.
CROSS_REFERENCES = {
    "SKILL.md": [
        "references/PATHOLOGOS_PATTERNS.md",
        "references/QUESTION_TAXONOMY.md",
        "references/SAFETY_BOUNDARIES.md",
    ],
    "references/SESSION_SCHEMA.md": [
        "../SKILL.md",
        "../scripts/validate_session_schema.py",
        "../assets/session_summary_template.md",
    ],
    "references/PATHOLOGOS_PATTERNS.md": [
        "../SKILL.md",
    ],
    "references/QUESTION_TAXONOMY.md": [
        "../SKILL.md",
        "SAFETY_BOUNDARIES.md",
    ],
    "references/SAFETY_BOUNDARIES.md": [
        "../SKILL.md",
    ],
}


def validate(package_root: Path) -> List[str]:
    """Check the package at ``package_root`` for completeness.

    Confirms every file in :data:`REQUIRED_FILES` is present and that every
    expected entry in :data:`CROSS_REFERENCES` resolves as a substring of the
    named file's text. Returns a list of human-readable error strings (one per
    problem). An empty list means the package is complete. All problems are
    collected before returning (D-03).
    """
    errors: List[str] = []

    # Presence pass: every required file must exist at the package root.
    missing: List[str] = []
    for rel in REQUIRED_FILES:
        if not (package_root / rel).exists():
            missing.append(rel)
    for rel in missing:
        errors.append(f"{rel}: missing required file")

    # Cross-reference pass: for each file that DOES exist, each expected
    # internal reference must appear as a substring of its text. Missing files
    # are already reported above, so guard with exists() to avoid a crash here.
    for rel, refs in CROSS_REFERENCES.items():
        path = package_root / rel
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        for ref in refs:
            if ref not in text:
                errors.append(f"{rel}: missing expected reference '{ref}'")

    return errors


def main(argv: List[str] = None) -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Check philosophical-midwifery package completeness: required files "
            "present and internal cross-references resolve (EVAL-03, D-05)."
        )
    )
    # NOTE: no positional `path` arg (D-04) — operates on the package root
    # relative to this script.
    parser.add_argument(
        "--json",
        dest="as_json",
        action="store_true",
        help='emit a single {"valid": bool, "errors": [...]} document',
    )
    args = parser.parse_args(argv)

    # Resolve the package root relative to this script: the script lives at
    # <pkg>/scripts/check_package.py, so .parent = scripts/ and .parent.parent =
    # the philosophical-midwifery/ package root.
    package_root = Path(__file__).resolve().parent.parent

    errors = validate(package_root)

    if args.as_json:
        print(json.dumps({"valid": not errors, "errors": errors}))
    else:
        if errors:
            for line in errors:
                print(line)
        else:
            print("valid")

    return 0 if not errors else 1


if __name__ == "__main__":
    sys.exit(main())
