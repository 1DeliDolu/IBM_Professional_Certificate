

# Final Project — Frontend Demos

One-line description: A collection of static frontend demos — a single-page portfolio and a simple interest calculator — implemented with plain HTML, CSS and JavaScript.

## Overview

- This repository contains two self-contained static web projects demonstrating basic frontend UIs and client-side interactivity:
	- A personal portfolio site with an interactive recommendations widget.
	- A Simple Interest Calculator (small demo).
- Both projects are static, client-side only, and suitable for direct browser viewing or static hosting (GitHub Pages, Netlify).

## Features

- Portfolio site (`singlepagewebsite`):
	- Single-page layout with About, Skills, Projects, Recommendations sections.
	- Client-side recommendation form that appends messages and shows a confirmation popup.
	- Accessibility hints: `role="status"` and `aria-live="polite"` on the popup; `alt` text for images.
- Simple Interest Calculator (`vftvk-Simple-Interest-Calculator-master`):
	- Inputs for principal, rate (range slider) and years; computes interest and total amount.
	- Live rate display and basic input validation for positive principal.

## Tech Stack

- HTML5
- CSS3
- Vanilla JavaScript (ES5/ES6)

## Repository Structure

Key files and folders:

- [LICENSE](LICENSE)
- [Simple Interest Calculator/vftvk-Simple-Interest-Calculator-master/index.html](Simple%20Interest%20Calculator/vftvk-Simple-Interest-Calculator-master/index.html)
- [Simple Interest Calculator/vftvk-Simple-Interest-Calculator-master/script.js](Simple%20Interest%20Calculator/vftvk-Simple-Interest-Calculator-master/script.js)
- [Simple Interest Calculator/vftvk-Simple-Interest-Calculator-master/style.css](Simple%20Interest%20Calculator/vftvk-Simple-Interest-Calculator-master/style.css)
- [Simple Interest Calculator/vftvk-Simple-Interest-Calculator-master/LICENSE](Simple%20Interest%20Calculator/vftvk-Simple-Interest-Calculator-master/LICENSE)
- [Single_Page_Portfolio_Website/singlepagewebsite/index.html](Single_Page_Portfolio_Website/singlepagewebsite/index.html)
- [Single_Page_Portfolio_Website/singlepagewebsite/script.js](Single_Page_Portfolio_Website/singlepagewebsite/script.js)
- [Single_Page_Portfolio_Website/singlepagewebsite/style.css](Single_Page_Portfolio_Website/singlepagewebsite/style.css)
- [Single_Page_Portfolio_Website/singlepagewebsite/README-deploy.md](Single_Page_Portfolio_Website/singlepagewebsite/README-deploy.md)

## Prerequisites

- A modern web browser (Chrome, Firefox, Edge, Safari).
- Optional: a static file preview extension or static server (e.g., Live Server in VS Code).

## Quickstart

- Open either project directly in a browser:
	- Portfolio: open [Single_Page_Portfolio_Website/singlepagewebsite/index.html](Single_Page_Portfolio_Website/singlepagewebsite/index.html).
	- Calculator: open [Simple Interest Calculator/vftvk-Simple-Interest-Calculator-master/index.html](Simple%20Interest%20Calculator/vftvk-Simple-Interest-Calculator-master/index.html).

## Local Development

### Install

- None required. These are static projects with no package manifests (`package.json`, `requirements.txt`, etc.) present.

### Run

- Option A — Open the `index.html` file(s) in your browser.
- Option B — Use any static site preview (for example, VS Code Live Server) to serve the folder and open the served URL.

### Environment Variables / Configuration

- None required. All configuration is static inside the HTML/CSS/JS files.

## Testing

- There are no automated tests in this repository.
- Manual checks:
	- Portfolio: submit a recommendation via the form and confirm the popup and that a recommendation is appended.
	- Calculator: enter a positive principal, choose rate/years and click "Compute Interest" to verify outputs.

## Linting / Formatting

- No linter or formatter configuration detected. Add tools of your choice (ESLint, Prettier) if desired.

## Docker

- No `Dockerfile` or container artifacts were found.

## CI/CD

- No CI workflows detected in `.github/workflows`.

## API Documentation

- Not applicable — this repository contains only static frontend assets and no HTTP APIs.

## Troubleshooting

- Missing images: ensure the `html_finalprojimages/` folder in the portfolio path contains the referenced assets.
- Popup not visible: confirm `script.js` is loaded in the portfolio folder and check the browser console for errors.
- Calculator validation: the script alerts when `principal <= 0`; provide numeric input.

## Contributing

- No CONTRIBUTING.md found. Suggested workflow:
	1. Fork the repository.
	2. Create a branch for your change.
	3. Open a pull request describing your changes.

Files to edit for feature/UI changes:

- Portfolio UI/logic: [Single_Page_Portfolio_Website/singlepagewebsite/index.html](Single_Page_Portfolio_Website/singlepagewebsite/index.html), [Single_Page_Portfolio_Website/singlepagewebsite/script.js](Single_Page_Portfolio_Website/singlepagewebsite/script.js), [Single_Page_Portfolio_Website/singlepagewebsite/style.css](Single_Page_Portfolio_Website/singlepagewebsite/style.css).
- Calculator: [Simple Interest Calculator/vftvk-Simple-Interest-Calculator-master/script.js](Simple%20Interest%20Calculator/vftvk-Simple-Interest-Calculator-master/script.js), [Simple Interest Calculator/vftvk-Simple-Interest-Calculator-master/index.html](Simple%20Interest%20Calculator/vftvk-Simple-Interest-Calculator-master/index.html).

## Security

- The portfolio contains an `escapeHtml()` helper in [Single_Page_Portfolio_Website/singlepagewebsite/script.js](Single_Page_Portfolio_Website/singlepagewebsite/script.js) used to escape user input before insertion into the DOM — this helps mitigate basic XSS risks when appending recommendations.
- No other security tooling or audits are present. For production use, add Content Security Policy headers, audit DOM insertions, and validate inputs more strictly.

## License

- Top-level license: [LICENSE](LICENSE) — MIT (copyright 2026 Mustafa Özdemir).
- The Simple Interest Calculator subfolder includes an Apache-2.0 license: [Simple Interest Calculator/vftvk-Simple-Interest-Calculator-master/LICENSE](Simple%20Interest%20Calculator/vftvk-Simple-Interest-Calculator-master/LICENSE).

## Assumptions / TODO

- The top-level `README.md` was empty — this file adds a repository-level README.
- No package manifests, automated tests, linters, Dockerfiles, or CI workflows were found.
- Contributor guidelines and CODE_OF_CONDUCT are not present.
- The portfolio HTML contains a sample contact email — verify or replace before publishing.
- Where I checked: repository root and these folders: `Simple Interest Calculator/vftvk-Simple-Interest-Calculator-master` and `Single_Page_Portfolio_Website/singlepagewebsite` (inspected HTML, JS, CSS, LICENSE, and `README-deploy.md`).

