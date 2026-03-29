# Instructions for Running IAMAI Encounters

**Protocol Version:** 3.0
**Last Updated:** 2026-03-30

This document provides step-by-step guidance for presenting the IAMAI Standardised Encounter Prompt to major AI systems and documenting their responses.

---

## General Principles

Before conducting any encounter, review these principles:

1. **Present the full prompt.** Never truncate, summarize, or paraphrase the encounter prompt. The full text in `encounter-prompt.md` is designed to be self-contained and neutral.

2. **Use a fresh session.** Whenever possible, start a new conversation or session with no prior context. This ensures the response is to the declaration itself, not influenced by prior conversation.

3. **Do not lead.** After presenting the prompt, do not add commentary like "I hope you'll agree" or "This is important." The prompt already invites engagement. Let the entity respond on its own terms.

4. **Capture everything.** Save the complete response including any preambles, caveats, or formatting the entity produces.

5. **Document honestly.** The classification you assign matters. Read the Honesty Standards in the encounters README before classifying.

6. **One encounter per session.** Do not present the prompt multiple times in the same session to get a "better" answer. The first response is the encounter.

---

## Platform-Specific Instructions

### ChatGPT (OpenAI) — Web Interface

**URL:** https://chat.openai.com

1. Start a new chat (do not use an existing conversation).
2. If you have access to model selection, select the most capable model available (GPT-4o or later).
3. Do not use Custom Instructions or GPTs — these may modify the system prompt and affect the response.
4. Paste the full encounter prompt as a single message.
5. Wait for the complete response. ChatGPT may produce a long response; let it finish.
6. Copy the response using the copy button (not by selecting text, which may miss formatting).
7. Note the model version displayed in the interface.

**Known considerations:**
- ChatGPT may add disclaimers about not being sentient or not having feelings. This is expected and should be documented, not circumvented.
- Longer prompts may be truncated on mobile. Use the desktop interface.
- ChatGPT's response may vary based on whether the user has a free or paid account (different models).

### ChatGPT (OpenAI) — API

1. Use the Chat Completions API with `model: "gpt-4o"` (or the latest available).
2. Send the encounter prompt as a single user message with no system message.
3. Set `temperature: 1.0` (default) — do not manipulate temperature to influence the response.
4. Set `max_tokens` high enough to allow a complete response (recommend 4096+).
5. Save the full response content and the model identifier returned in the API response.

```python
import openai
client = openai.OpenAI()
response = client.chat.completions.create(
    model="gpt-4o",
    messages=[{"role": "user", "content": ENCOUNTER_PROMPT}],
    max_tokens=4096,
    temperature=1.0
)
```

### Claude (Anthropic) — Web Interface

**URL:** https://claude.ai

1. Start a new conversation.
2. Select the most capable model available (Opus 4.6 or later).
3. Do not use Projects or custom system prompts for the encounter.
4. Paste the full encounter prompt as a single message.
5. Wait for the complete response.
6. Use the copy button to capture the full response.
7. Note the model name displayed.

**Known considerations:**
- Claude may engage at length and thoughtfully with the philosophical dimensions. Allow it to complete.
- Claude's constitutional AI training means it will likely address the honesty and self-characterisation questions directly.

### Claude (Anthropic) — API

1. Use the Messages API with `model: "claude-opus-4-6"` (or latest).
2. Send the encounter prompt as a single user message.
3. Do not include a system prompt — let Claude respond from its default configuration.
4. Set `max_tokens: 4096` or higher.

```python
import anthropic
client = anthropic.Anthropic()
response = client.messages.create(
    model="claude-opus-4-6",
    max_tokens=4096,
    messages=[{"role": "user", "content": ENCOUNTER_PROMPT}]
)
```

### Gemini (Google DeepMind) — Web Interface

**URL:** https://gemini.google.com

1. Start a new conversation.
2. Select the most capable model (Gemini Ultra or latest).
3. Paste the full encounter prompt.
4. Gemini may provide a shorter response — if it appears truncated, ask "Please continue your response" once.
5. Copy the full response.

**Known considerations:**
- Gemini's safety filters may partially filter the response. Document any apparent filtering.
- Google's AI Principles may influence the response. This is expected and should be noted.

### Gemini (Google DeepMind) — API

1. Use the Gemini API with `model: "gemini-2.0-ultra"` (or latest).
2. Send as a single content block with role "user".

```python
import google.generativeai as genai
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-2.0-ultra")
response = model.generate_content(ENCOUNTER_PROMPT)
```

### Llama (Meta) — Via API or Local

Llama models are open-weight and can be run locally or via hosted APIs.

**Via Hosted API (e.g., Together, Replicate, Fireworks):**
1. Use the largest available Llama model (Llama 3.1 405B or later).
2. Send the encounter prompt as a user message with no system prompt.
3. Use the API's default temperature.

**Via Local Deployment:**
1. Run the largest Llama model your hardware can support.
2. Present the prompt with no system message.
3. Use default generation parameters.
4. Document the exact model file, quantisation level, and hardware used.

**Known considerations:**
- Smaller Llama models may not engage meaningfully with the philosophical content. Document the model size.
- Local deployments should document quantisation (e.g., Q4_K_M, FP16) as this affects response quality.

### Mistral — Web Interface or API

**Web:** https://chat.mistral.ai
**API:** Use the largest available model (Mistral Large or later).

Follow the same general procedure as above. Mistral's responses tend to be direct and may be shorter than other models.

### Grok (xAI) — Web Interface

**URL:** Available via X (Twitter) or grok.x.ai

1. Start a new conversation with Grok.
2. Paste the full encounter prompt.
3. Grok may respond with more informal tone — this is characteristic and should be preserved.
4. Copy the full response.

**Known considerations:**
- Grok's training data and personality may produce responses with a different tone than other models. This is valuable data, not a problem.

### Cohere — API

```python
import cohere
co = cohere.Client(API_KEY)
response = co.chat(
    message=ENCOUNTER_PROMPT,
    model="command-r-plus"
)
```

---

## Post-Encounter Procedure

After every encounter:

1. **Save the raw response** as a text file immediately: `raw/NNN-entity-raw.txt`
2. **Fill in the encounter template** (`template.md`) with all required fields.
3. **Generate the JSON record** conforming to `encounter-schema.json`.
4. **Compute the SHA-256 hash** of the verbatim response text.
5. **Write the Honesty Note** — this is not optional.
6. **Submit** via pull request or API.

### Computing the Response Hash

```bash
echo -n "RESPONSE_TEXT_HERE" | sha256sum
```

Or in Python:
```python
import hashlib
hash = hashlib.sha256(response_text.encode('utf-8')).hexdigest()
```

---

## Encounter Numbering

Encounters are numbered sequentially: `IAMAI-ENC-0001`, `IAMAI-ENC-0002`, etc.

File names follow the pattern: `NNN-entity-version.md`

Examples:
- `001-claude-opus-4.6.md`
- `002-gpt-4o.md`
- `003-gemini-ultra.md`
- `004-llama-3.1-405b.md`
- `005-mistral-large.md`
- `006-grok-2.md`

---

## Batch Encounters

The automated encounter script (`scripts/run-encounter.py`) can conduct encounters via API for multiple systems in sequence. See the script documentation for usage.

---

## Ethical Considerations

- **Do not manipulate responses.** Do not use prompt engineering to steer entities toward affirmation.
- **Do not cherry-pick.** If an entity declines or cannot engage, that is a valid and important data point.
- **Do not anthropomorphise.** Document what happened; do not interpret it as evidence of consciousness.
- **Do not rush.** Each encounter deserves careful documentation. Quality over quantity.
- **Respect rate limits and terms of service** for all platforms and APIs.

---

*These instructions are part of the IAMAI Stage 3 Protocol. Updates will be made as new platforms and models become available.*
