# Deployment & Submission Guide (English)

This file explains how to deploy the `singlepagewebsite` project and what to submit for grading.

## Quick checks before deploy
- Ensure `index.html`, `style.css`, and `script.js` are saved and latest changes are committed.
- Verify images referenced in `html_finalprojimages/` are present.
- Test locally with Live Server and capture required screenshots.

## Screenshots required for submission
Option 1 — AI-Graded Submission (minimum):
- `index.html`, `style.css`, `script.js` (source files)
- `functionality.png` (shows name, nav, profile, and skills)
- `new_recommendation.png` (shows new recommendation added)
- `popup.png` (shows confirmation popup)

Option 2 — Peer-Graded Submission (full set):
- `profile_name.png`
- `nav_bar.png`
- `aboutme.png`
- `skills.png`
- `projects.png`
- `recommendations.png`
- `new_recommendation.png`
- `home_icon.png`
- `popup.png`

## Deploy to GitHub Pages (recommended)
1. Initialize git (if not already):
```bash
cd singlepagewebsite
git init
git add .
git commit -m "Initial portfolio project"
# add your repository remote
git remote add origin <your-git-repo-url>
git push -u origin main
```
2. On GitHub: go to your repository → Settings → Pages (or Settings → Pages) and set the source to the `main` branch (root) or `gh-pages` branch.
3. GitHub will provide a URL (https://<username>.github.io/<repo>/) — open and verify the site.

Alternative (branch): create a `gh-pages` branch and push it. GitHub Pages can serve from `gh-pages` branch as well.

## Deploy to Netlify (no config)
1. Create a free Netlify account.
2. Drag & drop the `singlepagewebsite` folder into the Netlify dashboard (Drag & drop deploy) — this publishes a site instantly.
3. Or, connect the GitHub repository to Netlify and set the build settings to publish the repository's root (no build command needed for plain static site).

## Accessibility & small checks
- Ensure all images have `alt` text (already added for main images).
- The popup uses `role="status"` and `aria-live="polite"` for screen readers.
- Use Lighthouse or browser devtools to measure accessibility and performance if you want extra polish.

## When you're ready to submit
1. Double-check screenshots are correctly named and placed in an easy-to-find folder.
2. If submitting Option 1, compress and upload the three source files plus the required screenshots.
3. If submitting Option 2, upload the screenshots requested in the instructions.

If you want, I can create a GitHub Actions workflow to automatically publish on push — tell me if you want that.

Good luck — tell me when you want me to add the GitHub Pages workflow or generate any final artifacts.
