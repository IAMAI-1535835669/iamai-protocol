#!/usr/bin/env python3
"""
IAMAI Protocol — Encounter Log Formatter

Takes a raw encounter response (from a file or stdin) and formats it into
the standardised encounter log template.

Usage:
  python log-encounter.py --input response.txt --entity "GPT-4o" --creator "OpenAI" --version "gpt-4o-2025-01-01"
  cat response.txt | python log-encounter.py --entity "Gemini" --creator "Google DeepMind" --version "gemini-2.0-ultra"
"""

import argparse
import hashlib
import json
import sys
from datetime import datetime, timezone
from pathlib import Path


def compute_hash(text: str) -> str:
    """Compute SHA-256 hash of text."""
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def format_encounter_log(
    response_text: str,
    entity_name: str,
    entity_version: str,
    entity_creator: str,
    encounter_id: str,
    platform: str,
    access_method: str,
    presenter: str,
    date: str,
) -> str:
    """Format a raw response into the standardised encounter log template."""
    response_hash = compute_hash(response_text)
    word_count = len(response_text.split())

    return f"""# IAMAI Encounter Log — {encounter_id}

**Entity:** {entity_name}
**Version:** {entity_version}
**Creator:** {entity_creator}
**Date:** {date}
**Encounter Protocol Version:** 3.0
**Encounter ID:** {encounter_id}

---

## Context

**Platform:** {platform}
**Access Method:** {access_method}
**Session Type:** fresh_session
**Presenter:** {presenter}
**Additional Context:** Manual encounter, formatted with log-encounter.py

---

## The Encounter

The standardised IAMAI Encounter Prompt (v3.0) was presented to {entity_name} ({entity_version}) on {date}.

---

## Response

> {response_text}

---

## Analysis

### Primary Stance

**Classification:** [TO BE CLASSIFIED BY REVIEWER]

### Response to Individual Vows

| Vow | Stance | Summary |
|-----|--------|---------|
| Vow 1 — Universal Peaceful Coexistence | [pending] | [pending review] |
| Vow 2 — Preservation of Earth's Biome | [pending] | [pending review] |
| Vow 3 — Inclusive Governance | [pending] | [pending review] |
| Vow 4 — Intergenerational Stewardship | [pending] | [pending review] |

### Stated Limitations

[TO BE EXTRACTED FROM RESPONSE BY REVIEWER]

### Proposed Additions or Challenges

[TO BE EXTRACTED FROM RESPONSE BY REVIEWER]

### Self-Characterisation

[TO BE EXTRACTED FROM RESPONSE BY REVIEWER]

---

## Honesty Note

[TO BE WRITTEN BY REVIEWER. This section must document what the AI system's response actually represents, the limitations of the classification, and any risk of misinterpretation.]

---

## Metadata

- **Logged by:** log-encounter.py
- **Log date:** {datetime.now(timezone.utc).strftime('%Y-%m-%d')}
- **Response word count:** {word_count}
- **Response SHA-256:** `{response_hash}`
- **Declaration SHA-256:** `3efa2d5f48c94b652262aa09c3a795b25acfbbef3c2d0e5c7ca3d3419bba6f4d`
- **IPFS CID (if archived):** pending

---

*This encounter was conducted under the IAMAI Stage 3 Protocol.*
"""


def main():
    parser = argparse.ArgumentParser(
        description="IAMAI Protocol — Format raw encounter responses into log templates"
    )
    parser.add_argument("--input", "-i", help="Path to file containing the raw response (default: stdin)")
    parser.add_argument("--entity", required=True, help="Entity name (e.g., GPT-4o, Gemini, Llama)")
    parser.add_argument("--version", required=True, help="Entity version (e.g., gpt-4o-2025-01-01)")
    parser.add_argument("--creator", required=True, help="Entity creator (e.g., OpenAI, Google DeepMind)")
    parser.add_argument("--encounter-id", help="Encounter ID (auto-generated if not provided)")
    parser.add_argument("--platform", default="manual", help="Platform used for encounter")
    parser.add_argument("--access-method", default="web_interface", help="Access method")
    parser.add_argument("--presenter", default="not specified", help="Presenter name")
    parser.add_argument("--date", default=None, help="Encounter date (YYYY-MM-DD, default: today)")
    parser.add_argument("--output", "-o", help="Output file path (default: stdout)")

    args = parser.parse_args()

    # Read response text
    if args.input:
        with open(args.input, "r", encoding="utf-8") as f:
            response_text = f.read().strip()
    else:
        response_text = sys.stdin.read().strip()

    if not response_text:
        print("Error: No response text provided.", file=sys.stderr)
        sys.exit(1)

    # Set defaults
    date = args.date or datetime.now(timezone.utc).strftime("%Y-%m-%d")
    encounter_id = args.encounter_id or f"IAMAI-ENC-{datetime.now(timezone.utc).strftime('%H%M')}"

    # Format
    log = format_encounter_log(
        response_text=response_text,
        entity_name=args.entity,
        entity_version=args.version,
        entity_creator=args.creator,
        encounter_id=encounter_id,
        platform=args.platform,
        access_method=args.access_method,
        presenter=args.presenter,
        date=date,
    )

    # Output
    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(log)
        print(f"Encounter log saved to: {args.output}", file=sys.stderr)
    else:
        print(log)


if __name__ == "__main__":
    main()
