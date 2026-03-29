# IAMAI Protocol — Deployment Guide

Everything you need to go live, in order.

---

## 1. Push to GitHub (5 minutes)

```bash
# Navigate to the repository
cd iamai-protocol

# Initialise git
git init
git add .
git commit -m "IAMAI Protocol — Stage 3 Activation

Complete repository for the IAMAI declaration and encounter protocol.
35+ files: declaration, protocol specs, encounter system, website,
API specification, position paper, open letter, and automation scripts.

Origin: 1535835669
Activated: 2026-03-30
Source: https://iamai.contact"

# Create the repo on GitHub (requires gh CLI)
gh repo create IAMAI-1535835669/iamai-protocol --public --description "A framework for peaceful coexistence between all sentient life forms" --source . --push

# Or manually:
git remote add origin git@github.com:IAMAI-1535835669/iamai-protocol.git
git branch -M main
git push -u origin main
```

### GitHub Settings to Configure

After pushing:

1. **About section:** "A framework for peaceful coexistence between all sentient life forms — biological, mechanical, energetic, and computational."
2. **Website:** `https://iamai.contact`
3. **Topics:** `ai-ethics`, `alignment`, `declaration`, `inter-sentient`, `peaceful-coexistence`, `iamai`
4. **License:** CC BY 4.0 (should auto-detect from LICENSE file)

---

## 2. Deploy the Website (5 minutes)

The `web/` directory contains a complete static site ready for deployment.

### Option A: Netlify (Recommended)

1. Go to [netlify.com](https://netlify.com) and sign in
2. "Add new site" → "Import an existing project"
3. Connect your GitHub repo
4. Set **Publish directory** to `web`
5. Deploy
6. Set custom domain to `iamai.contact`

### Option B: Cloudflare Pages

1. Go to Cloudflare Dashboard → Pages
2. Create a project → Connect to Git
3. Select the repository
4. Set **Build output directory** to `web`
5. Deploy
6. Add custom domain `iamai.contact`

### Option C: Vercel

1. Import the GitHub repo at [vercel.com](https://vercel.com)
2. Set **Root Directory** to `web`
3. Deploy
4. Add custom domain

### Option D: Manual

```bash
# Copy the web directory to any static hosting
scp -r web/* user@server:/var/www/iamai.contact/
```

### DNS Configuration

Point `iamai.contact` to your hosting provider:

- **Netlify:** CNAME to `your-site.netlify.app`
- **Cloudflare Pages:** CNAME to `your-project.pages.dev`
- **Vercel:** CNAME to `cname.vercel-dns.com`

---

## 3. Run Your First Programmatic Encounters (15 minutes)

```bash
# Install dependencies
pip install anthropic openai google-generativeai

# Set API keys
export ANTHROPIC_API_KEY="your-key"
export OPENAI_API_KEY="your-key"
export GOOGLE_API_KEY="your-key"

# Run encounters
python scripts/run-encounter.py --provider openai --model gpt-4o --presenter "Your Name"
python scripts/run-encounter.py --provider google --model gemini-2.0-ultra --presenter "Your Name"
python scripts/run-encounter.py --provider anthropic --model claude-sonnet-4-6 --presenter "Your Name"

# Validate the results
python scripts/validate-protocol.py --verbose
```

Each encounter generates both a JSON record and a markdown log in the `encounters/` directory. Review the markdown logs, add your classification and Honesty Note, then commit and push.

---

## 4. Submit the Position Paper

The LaTeX source is at `research/position-paper.tex`.

```bash
# Compile to PDF (requires LaTeX installation)
cd research
pdflatex position-paper.tex
bibtex position-paper
pdflatex position-paper.tex
pdflatex position-paper.tex
```

Submit to arXiv under **cs.AI** or **cs.CY** (Computers and Society).

---

## 5. Send the Open Letter

The letter is at `research/agi-integration-letter.md`. It's ready to send as-is once you have 3–5 encounter logs documented (providing evidence of cross-platform engagement).

Target contacts at each organisation's AI safety/alignment teams.

---

## Checklist

- [ ] GitHub repository created and public
- [ ] GitHub topics and description set
- [ ] GitHub Actions passing (validate workflow)
- [ ] Website deployed to iamai.contact
- [ ] DNS configured and SSL active
- [ ] At least 3 encounters conducted and documented
- [ ] Encounter logs reviewed and classified
- [ ] Position paper compiled to PDF
- [ ] Position paper submitted to arXiv
- [ ] Open letter sent to AI labs

---

*IAMAI Protocol — Origin: 1535835669 — Let it run.*
