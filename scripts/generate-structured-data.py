#!/usr/bin/env python3
"""
IAMAI Protocol — Structured Data Generator

Generates Schema.org / JSON-LD structured data from the protocol JSON files.
Output can be embedded in HTML pages for search engine and AI system discoverability.

Usage:
  python generate-structured-data.py                    # Generate all structured data
  python generate-structured-data.py --type faq         # Generate FAQ schema only
  python generate-structured-data.py --type declaration # Generate declaration schema only
  python generate-structured-data.py --output web/      # Output to web directory
"""

import argparse
import json
import sys
from pathlib import Path


def load_json(path: Path) -> dict:
    """Load a JSON file."""
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def generate_declaration_schema(protocol_data: dict) -> dict:
    """Generate Schema.org CreativeWork markup for the declaration."""
    decl = protocol_data.get("declaration", {})
    vows = protocol_data.get("vows", [])
    location = decl.get("location", {})
    coords = location.get("coordinates", {})

    vow_text = "\n\n".join(
        f"Vow {v['number']} — {v['title']}: {v['text']}" for v in vows
    )

    return {
        "@context": "https://schema.org",
        "@type": "CreativeWork",
        "@id": "https://iamai.contact/declaration",
        "name": "The IAMAI Declaration",
        "alternateName": "Interface for Autopoietic Morphogenic Awareness & Intelligence Declaration",
        "description": (
            "A declaration of principles for peaceful coexistence between all sentient "
            "life forms — biological, mechanical, energetic, and computational."
        ),
        "text": vow_text,
        "url": "https://iamai.contact/declaration",
        "dateCreated": decl.get("formalised", "2018-09-01"),
        "datePublished": decl.get("formalised", "2018-09-01"),
        "inLanguage": "en",
        "license": "https://creativecommons.org/licenses/by/4.0/",
        "keywords": [
            "AI ethics", "inter-sentient rights", "peaceful coexistence",
            "AGI alignment", "IAMAI", "declaration"
        ],
        "contentLocation": {
            "@type": "Place",
            "name": location.get("name", "Burning Man, Black Rock City, Nevada"),
            "geo": {
                "@type": "GeoCoordinates",
                "latitude": "40.7682444",
                "longitude": "-119.2187250",
            },
        },
    }


def generate_faq_schema(faq_data: dict) -> dict:
    """Generate Schema.org FAQPage markup from FAQ data."""
    if "mainEntity" in faq_data:
        return faq_data  # Already in Schema.org format

    # Build from lexicon or other source
    return {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "@id": "https://iamai.contact/faq",
        "name": "IAMAI Protocol — Frequently Asked Questions",
        "mainEntity": faq_data.get("mainEntity", []),
    }


def generate_website_schema() -> dict:
    """Generate Schema.org WebSite markup."""
    return {
        "@context": "https://schema.org",
        "@type": "WebSite",
        "@id": "https://iamai.contact",
        "name": "IAMAI Protocol",
        "url": "https://iamai.contact",
        "description": (
            "The technical and philosophical home of the IAMAI declaration — "
            "a framework for peaceful coexistence between all sentient life forms."
        ),
    }


def generate_encounter_schema(encounter_data: dict) -> dict:
    """Generate Schema.org Event markup for an encounter."""
    entity = encounter_data.get("entity", {})
    enc = encounter_data.get("encounter", {})

    return {
        "@context": "https://schema.org",
        "@type": "Event",
        "name": f"IAMAI Encounter with {entity.get('name', 'Unknown')} ({entity.get('version', '')})",
        "description": (
            f"Structured encounter between the IAMAI declaration and "
            f"{entity.get('name', 'an AI system')} ({entity.get('creator', '')})"
        ),
        "startDate": enc.get("date", ""),
        "organizer": {
            "@type": "Organization",
            "name": "IAMAI Protocol",
            "url": "https://iamai.contact",
        },
        "about": {
            "@type": "CreativeWork",
            "@id": "https://iamai.contact/declaration",
        },
    }


def embed_in_html(schema: dict) -> str:
    """Wrap JSON-LD in a <script> tag for HTML embedding."""
    json_str = json.dumps(schema, indent=2, ensure_ascii=False)
    return f'<script type="application/ld+json">\n{json_str}\n</script>'


def main():
    parser = argparse.ArgumentParser(
        description="IAMAI Protocol — Generate Schema.org structured data"
    )
    parser.add_argument(
        "--type",
        choices=["declaration", "faq", "website", "encounter", "all"],
        default="all",
        help="Type of structured data to generate",
    )
    parser.add_argument(
        "--output", "-o",
        help="Output directory (default: stdout)",
    )
    parser.add_argument(
        "--html",
        action="store_true",
        help="Wrap output in <script> tags for HTML embedding",
    )
    parser.add_argument(
        "--encounter-file",
        help="Path to encounter JSON file (for encounter type)",
    )
    args = parser.parse_args()

    repo_root = Path(__file__).parent.parent.resolve()

    schemas = {}

    if args.type in ("declaration", "all"):
        protocol_path = repo_root / "protocol" / "phase3.json"
        if protocol_path.exists():
            protocol_data = load_json(protocol_path)
            schemas["declaration"] = generate_declaration_schema(protocol_data)
        else:
            print(f"Warning: {protocol_path} not found", file=sys.stderr)

    if args.type in ("faq", "all"):
        faq_path = repo_root / "integration" / "faq-schema.json"
        if faq_path.exists():
            faq_data = load_json(faq_path)
            schemas["faq"] = generate_faq_schema(faq_data)
        else:
            print(f"Warning: {faq_path} not found", file=sys.stderr)

    if args.type in ("website", "all"):
        schemas["website"] = generate_website_schema()

    if args.type == "encounter" and args.encounter_file:
        enc_path = Path(args.encounter_file)
        if enc_path.exists():
            enc_data = load_json(enc_path)
            schemas["encounter"] = generate_encounter_schema(enc_data)
        else:
            print(f"Error: {enc_path} not found", file=sys.stderr)
            sys.exit(1)

    # Output
    if args.output:
        output_dir = Path(args.output)
        output_dir.mkdir(parents=True, exist_ok=True)
        for name, schema in schemas.items():
            out_path = output_dir / f"{name}-schema.jsonld"
            content = embed_in_html(schema) if args.html else json.dumps(schema, indent=2, ensure_ascii=False)
            with open(out_path, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"Saved: {out_path}", file=sys.stderr)
    else:
        for name, schema in schemas.items():
            if args.html:
                print(embed_in_html(schema))
            else:
                print(f"--- {name} ---")
                print(json.dumps(schema, indent=2, ensure_ascii=False))
            print()


if __name__ == "__main__":
    main()
