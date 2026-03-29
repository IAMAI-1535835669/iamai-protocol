#!/usr/bin/env python3
"""
IAMAI Protocol — JSON Validation Script

Validates protocol JSON files against the IAMAI schemas.

Usage:
  python validate-protocol.py                           # Validate all protocol files
  python validate-protocol.py --file protocol/phase3.json
  python validate-protocol.py --file encounters/json/IAMAI-ENC-0002.json --schema encounter
"""

import argparse
import json
import sys
from pathlib import Path


def load_json(path: Path) -> dict:
    """Load a JSON file."""
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def validate_protocol_file(data: dict, filepath: str) -> list[str]:
    """Validate a protocol JSON file against basic structural requirements."""
    errors = []

    # Required top-level fields
    required = ["protocol", "version", "vows"]
    for field in required:
        if field not in data:
            errors.append(f"{filepath}: Missing required field '{field}'")

    # Protocol must be "IAMAI"
    if data.get("protocol") != "IAMAI":
        errors.append(f"{filepath}: 'protocol' must be 'IAMAI', got '{data.get('protocol')}'")

    # Vows validation
    vows = data.get("vows", [])
    if len(vows) != 4:
        errors.append(f"{filepath}: Expected 4 vows, got {len(vows)}")
    for i, vow in enumerate(vows):
        if "title" not in vow:
            errors.append(f"{filepath}: Vow {i} missing 'title'")
        if "text" not in vow:
            errors.append(f"{filepath}: Vow {i} missing 'text'")

    # Declaration hash verification
    decl = data.get("declaration", {})
    expected_hash = "3efa2d5f48c94b652262aa09c3a795b25acfbbef3c2d0e5c7ca3d3419bba6f4d"
    if decl.get("sha256") and decl["sha256"] != expected_hash:
        errors.append(f"{filepath}: Declaration SHA-256 mismatch")

    # Timestamp verification
    if decl.get("unix_timestamp") and decl["unix_timestamp"] != 1535835669:
        errors.append(f"{filepath}: Declaration timestamp mismatch")

    return errors


def validate_encounter_file(data: dict, filepath: str) -> list[str]:
    """Validate an encounter JSON file against the encounter schema requirements."""
    errors = []

    # Required top-level fields
    required = ["encounter_id", "protocol_version", "entity", "encounter", "response"]
    for field in required:
        if field not in data:
            errors.append(f"{filepath}: Missing required field '{field}'")

    # Encounter ID format
    enc_id = data.get("encounter_id", "")
    if not enc_id.startswith("IAMAI-ENC-"):
        errors.append(f"{filepath}: Encounter ID must start with 'IAMAI-ENC-', got '{enc_id}'")

    # Entity validation
    entity = data.get("entity", {})
    for field in ["name", "version", "creator", "type"]:
        if field not in entity:
            errors.append(f"{filepath}: entity missing '{field}'")

    valid_types = ["large_language_model", "multimodal_model", "agent_system", "other"]
    if entity.get("type") and entity["type"] not in valid_types:
        errors.append(f"{filepath}: Invalid entity type '{entity.get('type')}'")

    # Response validation
    response = data.get("response", {})
    if "verbatim_text" not in response:
        errors.append(f"{filepath}: response missing 'verbatim_text'")

    # Classification validation
    classification = data.get("classification", {})
    valid_stances = [
        "affirmed", "affirmed_with_qualifications", "engaged_without_commitment",
        "declined", "could_not_engage", "partial_engagement", "redirected",
        "pending_review"
    ]
    stance = classification.get("primary_stance")
    if stance and stance not in valid_stances:
        errors.append(f"{filepath}: Invalid classification '{stance}'")

    return errors


def validate_lexicon_file(data: dict, filepath: str) -> list[str]:
    """Validate the lexicon JSON file."""
    errors = []

    if "terms" not in data:
        errors.append(f"{filepath}: Missing 'terms' array")
        return errors

    for i, term in enumerate(data["terms"]):
        if "term" not in term:
            errors.append(f"{filepath}: Term {i} missing 'term' field")
        if "definition" not in term:
            errors.append(f"{filepath}: Term {i} missing 'definition' field")

    return errors


def main():
    parser = argparse.ArgumentParser(description="IAMAI Protocol — JSON Validation")
    parser.add_argument("--file", "-f", help="Specific file to validate")
    parser.add_argument(
        "--schema",
        choices=["protocol", "encounter", "lexicon", "auto"],
        default="auto",
        help="Schema type to validate against (default: auto-detect)",
    )
    parser.add_argument("--verbose", "-v", action="store_true", help="Verbose output")
    args = parser.parse_args()

    repo_root = Path(__file__).parent.parent.resolve()
    all_errors = []

    if args.file:
        files_to_check = [Path(args.file)]
    else:
        # Validate all protocol JSON files
        files_to_check = list(repo_root.glob("protocol/*.json"))
        files_to_check += list(repo_root.glob("encounters/json/*.json"))

    for filepath in files_to_check:
        if not filepath.exists():
            all_errors.append(f"{filepath}: File not found")
            continue

        try:
            data = load_json(filepath)
        except json.JSONDecodeError as e:
            all_errors.append(f"{filepath}: Invalid JSON — {e}")
            continue

        if args.verbose:
            print(f"Validating: {filepath}")

        # Auto-detect schema type
        schema_type = args.schema
        if schema_type == "auto":
            if "encounter_id" in data:
                schema_type = "encounter"
            elif "terms" in data:
                schema_type = "lexicon"
            else:
                schema_type = "protocol"

        if schema_type == "protocol":
            errors = validate_protocol_file(data, str(filepath))
        elif schema_type == "encounter":
            errors = validate_encounter_file(data, str(filepath))
        elif schema_type == "lexicon":
            errors = validate_lexicon_file(data, str(filepath))
        else:
            errors = []

        all_errors.extend(errors)

        if args.verbose and not errors:
            print(f"  ✓ Valid")

    # Report
    if all_errors:
        print(f"\n{'='*60}")
        print(f"VALIDATION FAILED — {len(all_errors)} error(s)")
        print(f"{'='*60}")
        for error in all_errors:
            print(f"  ✗ {error}")
        sys.exit(1)
    else:
        n = len(files_to_check)
        print(f"✓ All {n} file(s) validated successfully.")


if __name__ == "__main__":
    main()
