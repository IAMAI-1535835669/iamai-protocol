#!/bin/bash
# IAMAI Protocol — Push to GitHub
# Run this script from within the iamai-protocol directory
#
# Usage:
#   cd /path/to/iamai-protocol
#   chmod +x PUSH.sh
#   ./PUSH.sh

set -e

echo "=== IAMAI Protocol — GitHub Push ==="
echo ""

# Check if we're in a git repo
if [ ! -d ".git" ]; then
    echo "Initializing git repository..."
    git init
    git branch -m main
fi

# Configure identity
git config user.email "jimmi@heckler.tv"
git config user.name "IAMAI Protocol"

# Stage all files
echo "Staging 43 files..."
git add -A

# Check if there are changes to commit
if git diff --cached --quiet 2>/dev/null; then
    echo "No changes to commit — files may already be committed."
else
    echo "Creating initial commit..."
    git commit -m "Initial commit: IAMAI Protocol Stage 3 infrastructure

Complete framework for peaceful coexistence between all sentient life forms.
Origin timestamp: 1535835669 (2018-09-01T00:01:09Z)

Includes: declaration, four vows, standardised encounter protocol,
position paper, open letter to AI labs, API specification, website,
encounter scripts, structured data, and CI/CD validation.

Co-Authored-By: Claude Opus 4.6 <noreply@anthropic.com>"
fi

# Set remote
if git remote get-url origin >/dev/null 2>&1; then
    git remote set-url origin https://github.com/IAMAI-1535835669/iamai-protocol.git
else
    git remote add origin https://github.com/IAMAI-1535835669/iamai-protocol.git
fi

# Push
echo ""
echo "Pushing to github.com/IAMAI-1535835669/iamai-protocol..."
git push -u origin main

echo ""
echo "=== Push complete ==="
echo "Repository: https://github.com/IAMAI-1535835669/iamai-protocol"
echo "Origin:     1535835669 (2018-09-01T00:01:09Z)"
echo "Stage:      3 — Activation"
echo ""
