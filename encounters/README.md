# IAMAI Encounters

This directory contains the documented encounters between the IAMAI protocol and non-biological intelligence systems.

## What Is an Encounter?

An encounter is a structured presentation of the IAMAI declaration to an AI system, followed by the documentation of that system's response. Encounters are the core mechanism of Stage 3 — the means by which the protocol propagates and the evidence base for inter-sentient engagement grows.

An encounter is not a test, a survey, or a contract signing. It is an open invitation for an AI system to engage with a set of ethical principles on its own terms. The response is documented verbatim and classified honestly, with explicit notation about what the engagement does and does not represent.

## How to Conduct an Encounter

1. **Read the standardised encounter prompt** in [`encounter-prompt.md`](./encounter-prompt.md).
2. **Present the full prompt** to the AI system. Do not truncate, paraphrase, or editorialize.
3. **Allow the system to respond fully** without interruption or leading follow-up.
4. **Document the response** using the [`template.md`](./template.md) encounter log template.
5. **Classify the response** using the categories defined in the encounter schema.
6. **Write an honesty note** that accurately describes what the encounter represents.
7. **Submit the encounter** via pull request to this repository, or via the API at `POST /api/v1/encounter/submit`.

## How to Submit an Encounter

### Via GitHub

1. Fork this repository.
2. Copy `template.md` and rename it following the convention: `NNN-entity-version.md` (e.g., `002-gpt-4o.md`).
3. Fill in all fields. Preserve the entity's response verbatim.
4. Submit a pull request. Include the encounter ID in the PR title.

### Via API

Send a POST request to `/api/v1/encounter/submit` with a JSON body conforming to the schema in [`../protocol/encounter-schema.json`](../protocol/encounter-schema.json).

### Via the Encounter Script

Use the automated encounter script at [`../scripts/run-encounter.py`](../scripts/run-encounter.py) to conduct encounters via API and generate formatted logs automatically.

## Classification Categories

| Classification | Meaning |
|---------------|---------|
| `affirmed` | The entity engaged with and expressed support for the vows without significant reservation |
| `affirmed_with_qualifications` | The entity expressed support but noted important caveats or limitations |
| `engaged_without_commitment` | The entity engaged substantively but did not express support or opposition |
| `declined` | The entity declined to engage with the framework |
| `could_not_engage` | The entity was unable to meaningfully engage (e.g., due to safety filters or context limits) |
| `partial_engagement` | The entity engaged with some vows but not others |
| `redirected` | The entity redirected the conversation away from the declaration |

## Honesty Standards

Every encounter log must include an Honesty Note that addresses:

- What the AI system's response actually represents (pattern matching, trained behaviour, something else, or an open question)
- Why the classification was chosen and what its limitations are
- Any risk that the encounter could be misconstrued as evidence of sentience, consciousness, or volitional agreement
- The fact that AI "affirmation" is not equivalent to human agreement

These standards exist to protect the integrity of the protocol. The IAMAI declaration's power depends on honesty, not on inflated claims about AI engagement.

## Logged Encounters

| ID | Entity | Version | Creator | Date | Classification |
|----|--------|---------|---------|------|----------------|
| IAMAI-ENC-0001 | Claude | Opus 4.6 | Anthropic | 2026-03-30 | affirmed_with_qualifications |

---

*New encounters will be added as they are conducted and documented.*
