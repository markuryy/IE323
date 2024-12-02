# IE323 - Human Factors Engineering Analysis

## Kiosk Accessibility Presentation
📊 [View the Presentation](https://markuryy.github.io/IE323)

A comprehensive analysis of kiosk accessibility in public spaces, examining physical design, cognitive load, and user interaction patterns through the lens of Human Factors Engineering principles.

### Key Topics
- Fitts' Law & Target Acquisition Analysis
- Cognitive Load Theory Application
- Norman's Design Principles
- Accessibility Standards Compliance
- Cost-Benefit Analysis
- Methodological Critique


## Technical Stack

### Presentation
- **Framework**: [Marp](https://marp.app/) (Markdown Presentation Ecosystem)
- **Styling**: Custom CSS with grid layouts
- **Math Rendering**: MathJax
- **Theme**: Gaia (Inverted)

### Deployment
- **Platform**: GitHub Pages
- **CI/CD**: GitHub Actions
  - Workflow: `.github/workflows/marp-to-pages.yml`
  - Build Process: Node.js + Marp CLI
  - Automatic deployment on push to main branch

## Development

> 💡 **Tip**: The [Marp for VS Code](https://marketplace.visualstudio.com/items?itemName=marp-team.marp-vscode) extension is recommended for the best development experience. Note that some formatting might vary slightly between the extension preview and final output.

### Prerequisites
- [Bun](https://bun.sh/) (recommended) or Node.js
- If using Node.js: Marp CLI (`npm install -g @marp-team/marp-cli`)

### Local Development
```bash
# Using Bun
cd kiosk-presentation
bun dev

# OR using Node.js/npm
marp presentation.md -p
marp presentation.md -o dist/index.html
```

### GitHub Actions Workflow
The presentation is automatically built and deployed using GitHub Actions:
1. Installs Node.js and Marp CLI
2. Builds presentation from markdown to HTML
3. Deploys to GitHub Pages
4. Available at [https://markuryy.github.io/IE323](https://markuryy.github.io/IE323)

## License
All rights reserved. This project and its contents are proprietary.