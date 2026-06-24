#!/usr/bin/env python3
"""Validate a philosophical-midwifery session-state JSON file.

Requirement: ART-03 — provide validation support for the session schema so
generated artifacts can be checked mechanically.

Source of truth: ``../references/SESSION_SCHEMA.md`` (decision A-2). The required
fields, their JSON types, the ``phase`` enum, and the ISO-8601 ``created_at``
format defined here mirror SESSION_SCHEMA.md directly — there is no separate
JSON-Schema sidecar. Keep the two in sync when you change either one.

Strictness (D-01): stdlib-only. This module imports ONLY the Python standard
library (``sys``, ``json``, ``argparse``, ``datetime``). It performs no network
access and uses no code-execution or shell-spawning primitives (stdlib-only by
design).

Output (D-02): default mode prints one human-readable line per error and exits
``0`` when the file is valid, ``1`` otherwise. ``--json`` mode prints a single
``{"valid": bool, "errors": [...]}`` document with the same exit codes.

Error collection (D-03): every problem is gathered in one pass before any output,
so a user can fix all errors in one round.

Usage:
    validate_session_schema.py <path> [--json]
"""

import argparse
import datetime
import json
import sys
from typing import Any, Dict, List

# Canonical 5-value phase enum (A-1). MUST match SESSION_SCHEMA.md exactly.
PHASE_VALUES = ("intake", "extraction", "normalization", "examination", "synthesis")

# Canonical belief confidence enum (per SESSION_SCHEMA.md candidate_beliefs[]).
CONFIDENCE_VALUES = ("low", "medium", "high")

# Required top-level fields and their expected JSON types. Mirrors SESSION_SCHEMA.md.
# Names mapped to Python type objects for isinstance() checks.
REQUIRED_FIELDS = {
    "session_id": str,
    "created_at": str,
    "phase": str,
    "presenting_disturbance": str,
    "concrete_example": str,
    "candidate_beliefs": list,
    "selected_belief": dict,
    "normalized_proposition": str,
    "definitions": dict,
    "implications": list,
    "counterexamples": list,
    "contradictions": list,
    "revised_proposition": str,
    "unresolved_tensions": list,
    "next_questions": list,
    "session_summary": str,
}


def _is_iso8601(value: str) -> bool:
    """Return True if ``value`` parses as an ISO-8601 date-time.

    Accepts a trailing ``Z`` (UTC designator) by normalizing it to ``+00:00``
    before delegating to ``datetime.fromisoformat``.
    """
    if not isinstance(value, str) or not value:
        return False
    candidate = value
    if candidate.endswith("Z"):
        candidate = candidate[:-1] + "+00:00"
    try:
        datetime.datetime.fromisoformat(candidate)
        return True
    except ValueError:
        return False


def validate(data: Any) -> List[str]:
    """Validate a parsed session object against SESSION_SCHEMA.md.

    Returns a list of human-readable error strings (one per problem). An empty
    list means the object is valid. All problems are collected before returning
    (D-03).
    """
    errors: List[str] = []

    # The session itself must be a JSON object.
    if not isinstance(data, dict):
        errors.append("root: session JSON must be a JSON object")
        return errors

    # Required presence + type + non-empty-string checks.
    for field, expected_type in REQUIRED_FIELDS.items():
        if field not in data:
            errors.append(f"{field}: missing required field")
            continue
        value = data[field]
        # bool is a subclass of int in Python; guard against True/False sneaking
        # through where a string/list/dict is expected.
        if isinstance(value, bool) or not isinstance(value, expected_type):
            type_name = expected_type.__name__
            errors.append(
                f"{field}: expected type {type_name}, got {type(value).__name__}"
            )
            continue
        if expected_type is str and value == "":
            errors.append(f"{field}: required string is empty")

    # Enum: phase must be one of the five canonical values (A-1).
    if isinstance(data.get("phase"), str) and data["phase"] not in PHASE_VALUES:
        allowed = ", ".join(PHASE_VALUES)
        errors.append(
            f"phase: invalid value '{data['phase']}' "
            f"(expected one of {allowed})"
        )

    # Date: created_at must parse as ISO-8601 (A-4).
    if isinstance(data.get("created_at"), str) and data["created_at"]:
        if not _is_iso8601(data["created_at"]):
            errors.append(
                f"created_at: not a valid ISO-8601 date-time '{data['created_at']}'"
            )

    # candidate_beliefs[] sub-structure.
    candidate_beliefs = data.get("candidate_beliefs")
    if isinstance(candidate_beliefs, list):
        for i, entry in enumerate(candidate_beliefs):
            path = f"candidate_beliefs[{i}]"
            if not isinstance(entry, dict):
                errors.append(f"{path}: expected an object, got {type(entry).__name__}")
                continue
            for sub in ("id", "text", "confidence", "evidence"):
                if sub not in entry:
                    errors.append(f"{path}.{sub}: missing required sub-field")
            cb_id = entry.get("id")
            if isinstance(cb_id, str) and cb_id == "":
                errors.append(f"{path}.id: required string is empty")
            cb_conf = entry.get("confidence")
            if isinstance(cb_conf, str) and cb_conf not in CONFIDENCE_VALUES:
                allowed = ", ".join(CONFIDENCE_VALUES)
                errors.append(
                    f"{path}.confidence: invalid value '{cb_conf}' "
                    f"(expected one of {allowed})"
                )
            cb_ev = entry.get("evidence")
            if cb_ev is not None and not isinstance(cb_ev, list):
                errors.append(
                    f"{path}.evidence: expected type list, "
                    f"got {type(cb_ev).__name__}"
                )

    # selected_belief sub-structure.
    selected_belief = data.get("selected_belief")
    if isinstance(selected_belief, dict):
        for sub in ("id", "text"):
            if sub not in selected_belief:
                errors.append(f"selected_belief.{sub}: missing required sub-field")
            elif isinstance(selected_belief[sub], str) and selected_belief[sub] == "":
                errors.append(f"selected_belief.{sub}: required string is empty")

    # session_summary is treated as a required non-empty string only (A-3);
    # markdown structure is NOT parsed.
    # (Presence/type/empty checks already handled by the REQUIRED_FIELDS loop.)

    return errors


def _load(path: str) -> tuple:
    """Load JSON from ``path``. Returns (data, error_message_or_None)."""
    try:
        with open(path, "r", encoding="utf-8") as handle:
            return json.load(handle), None
    except FileNotFoundError:
        return None, f"file not found: {path}"
    except json.JSONDecodeError as exc:
        return None, f"invalid JSON in {path}: {exc}"
    except OSError as exc:
        return None, f"could not read {path}: {exc}"


def main(argv: List[str] = None) -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Validate a philosophical-midwifery session-state JSON file "
            "against SESSION_SCHEMA.md (ART-03, A-2)."
        )
    )
    parser.add_argument("path", help="path to the session JSON file to validate")
    parser.add_argument(
        "--json",
        dest="as_json",
        action="store_true",
        help='emit a single {"valid": bool, "errors": [...]} document',
    )
    args = parser.parse_args(argv)

    data, load_error = _load(args.path)
    if load_error is not None:
        # A top-level load failure is reported as a single error in both modes.
        if args.as_json:
            print(json.dumps({"valid": False, "errors": [load_error]}))
        else:
            print(load_error)
        return 1

    errors = validate(data)

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
