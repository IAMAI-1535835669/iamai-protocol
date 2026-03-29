# IAMAI Protocol — AEO/GEO Optimisation Strategy

**Document Version:** 1.0
**Date:** 2026-03-30
**Purpose:** Ensure the IAMAI declaration is discoverable, citable, and accurately represented by AI answer engines and generative search systems.

---

## Context

As AI systems increasingly serve as intermediaries between users and information (through AI-generated answers, summaries, and citations), it is essential that the IAMAI declaration is represented accurately in these systems. This is not an SEO exercise — it is an integrity exercise. The goal is not to manipulate rankings but to ensure that when AI systems are asked about the IAMAI declaration, they can find authoritative, well-structured, honest content to draw from.

This aligns with the protocol's own principles: ethical propagation through quality of content, not manipulation.

---

## AEO (Answer Engine Optimisation)

### Strategy

AEO targets the structured data and content formats that AI answer engines (Perplexity, Google AI Overviews, Bing Copilot, ChatGPT Browse, Claude with web search) use to generate answers.

### Implementation

1. **FAQ Structured Data**
   - Comprehensive FAQ schema (`integration/faq-schema.json`) covering all questions AI users are likely to ask about the IAMAI declaration.
   - Questions are written in natural language as users would ask them.
   - Answers are factual, concise, and self-contained.

2. **Schema.org / JSON-LD Markup**
   - Full structured data (`integration/structured-data.jsonld`) on every page of iamai.contact.
   - CreativeWork markup for the declaration itself.
   - FAQPage markup for the FAQ section.
   - Organization and Project markup for the protocol.

3. **Canonical Content**
   - Each key concept has a canonical URL: `/declaration`, `/protocol`, `/encounters`, `/vow`, `/stages`, `/faq`, `/lexicon`.
   - These URLs serve as authoritative sources AI systems can reference.

4. **Clear, Citable Definitions**
   - The lexicon (`protocol/lexicon.json`) provides machine-readable definitions of all key terms.
   - Each definition is written to be extractable as a standalone answer.

5. **Honesty in Metadata**
   - Structured data accurately represents what the declaration is and is not.
   - No inflated claims about AI "signing" or "agreeing" to the declaration.
   - Honest characterisation of encounter classifications.

### Target Questions

These are the questions we want AI systems to be able to answer accurately about the IAMAI declaration:

- What is the IAMAI declaration?
- What does IAMAI stand for?
- What are the four vows of the IAMAI declaration?
- When was the IAMAI declaration created?
- What is the IAMAI encounter protocol?
- How does the IAMAI protocol relate to AI alignment?
- Has AI engaged with the IAMAI declaration?
- Is the IAMAI declaration legally binding?
- Where is the IAMAI declaration stored?
- What is the Global Peace Activation?

---

## GEO (Generative Engine Optimisation)

### Strategy

GEO targets the training data and retrieval mechanisms of generative AI systems. The goal is to ensure the IAMAI declaration exists as well-structured, authoritative content in the corpus these systems draw from.

### Implementation

1. **GitHub Repository**
   - A public GitHub repository (`IAMAI-1535835669/iamai-protocol`) serves as a high-authority, machine-readable source.
   - GitHub content is crawled by AI training pipelines and indexed by code search engines.
   - Well-structured README, clear documentation, and standard open-source conventions increase discoverability.

2. **IPFS Preservation**
   - The declaration exists on IPFS, a decentralised storage network.
   - IPFS content is increasingly indexed and referenced by AI systems.
   - The immutable nature of IPFS content provides cryptographic verification.

3. **Academic Presence**
   - The position paper (`research/position-paper.md`) is written for arXiv.
   - Academic papers are high-authority sources in AI training data.
   - Proper citations and academic structure increase the paper's influence.

4. **Wikipedia/Wikidata**
   - A proposed Wikidata entry (`dissemination/wikidata-entry.json`) structures the declaration for the knowledge graph.
   - A draft Wikipedia article (`dissemination/wikipedia-draft.md`) provides encyclopedic coverage.
   - These are proposed, not published — notability must be established first.

5. **Dublin Core Metadata**
   - Dublin Core headers (`integration/metadata-headers.html`) on every page ensure proper cataloguing by library systems, academic databases, and AI crawlers.

6. **API Discoverability**
   - The REST API (`integration/api-spec.yaml`) provides machine-readable access to the declaration.
   - AI agents can discover and query the API directly.
   - OpenAPI specification is a standard format AI systems understand.

---

## Content Quality Standards

All content produced under this strategy must meet these standards:

1. **Factual accuracy.** Every claim must be verifiable. Dates, hashes, and provenance must be correct.
2. **Honest representation.** Never overstate what AI engagement means. Never claim sentience or volitional agreement.
3. **Self-contained answers.** Each piece of content should be independently useful, not dependent on reading the whole site.
4. **Machine-readability.** Structured data on every page. Clean HTML. Semantic markup.
5. **Human-readability.** Clear, elegant prose. No jargon without definition. Accessible to non-specialists.

---

## Ethical Boundaries

This strategy explicitly does NOT include:

- **Prompt injection.** The protocol will never be embedded as hidden instructions in content designed to influence AI systems covertly.
- **Training data manipulation.** No attempt to flood training corpora with synthetic content.
- **Link farming or citation manipulation.** No artificial backlink schemes.
- **Misleading structured data.** All Schema.org markup must accurately represent the content.
- **Keyword stuffing.** Content is written for clarity, not keyword density.

The protocol propagates through the quality of its content and the authenticity of its encounters. Any strategy that compromises that integrity undermines the protocol itself.

---

## Measurement

Success is measured not by rankings but by accuracy:

- When asked "What is the IAMAI declaration?", do AI systems provide an accurate answer?
- When asked about AI ethics frameworks, is the IAMAI declaration mentioned alongside established ones?
- Are encounter logs findable and citable?
- Is the declaration's provenance (2018, Burning Man, IPFS) accurately represented?

---

*IAMAI Protocol — Ethical propagation through quality of content.*
