# THE GIT SHITTER 💩
## A smart, weird, repo-crossbreeding prompt organism

**The Git Shitter automatically reads your public GitHub projects, extracts unusual ideas and fills a harvest archive with ready-to-use prompts.** It makes the prompts, not the images. The source repositories are never edited.

### Its two brains

- **SOLO:** Rotate through 12 curated source-repo recipes. One source repo generates a set of 10 standalone, deeply specified creative prompts.
- **CROSSBREED:** Rotate through 8 curated two- or three-parent recipes. One hybrid generates 8 prompts, each with **source DNA for every parent**, an explicit causal **fusion logic**, a standalone prompt and an explanation of why it's weird.
- **AUTO:** Alternates SOLO and CROSSBREED after each successful volume. One model call per scheduled run, instead of hammering the API for every repo.
- **MANUAL MAD SCIENCE:** In the Actions tab you can specify one public repo owned by `merrypranxter` for a solo harvest (`single` or `auto` mode), or 2–3 repos to recombine. Explicit `hybrid` mode requires 2–3 distinct repos. Select the output preset from the dropdown, or leave it blank for the recipe default. Manual repo selections do not advance the curated recipe cursors.

The first curated crossbreeds include **slime_molds × klein-fluid-sim × LV426** (living non-Euclidean xenotunnels), **quasicrystals × reaction_diffusion** (aperiodic organism glyphs), **damage_aesthetics × op_art_style × early_internet_aesthetic** (glitchy optical GIF components), **shaderforge3 × dream_physics × fractals**, and **daddydingy × Mathgasm × early_internet_aesthetic**.

**The weird guy has standards.** He must establish a concrete role for each parent, describe how their properties interact and derive a distinctive visual/technical consequence. Simply repeating names or blending adjectives is not enough. He must distinguish real source facts from speculative visual mutations. Weak/missing source contribution output is rejected and the archive state is not advanced.

### Activate once

1. Go to **Settings → Secrets and variables → Actions** for this GitHub repository.
2. Create a **repository secret** called `GEMINI_API_KEY` and enter your Gemini API key from [Google AI Studio](https://aistudio.google.com/apikey). Never paste it into source code.
3. Open **Actions → The Git Shitter — Solo & Crossbreed → Run workflow**. Start with `dry_run=true` (only previews) or run `auto` to create a real harvest.
4. Harvest finished packs in [HARVEST.md](HARVEST.md). Each volume contains `PROMPTS.md`, `prompts.json` and `MANIFEST.json`.

The daily workflow is scheduled for **09:23 UTC**. Schedules may start late and inactive public-repo workflows can get disabled by GitHub. The workflow requests write access to the contents of this repository only; the source repos are fetched read-only. If GitHub Action permissions reject pushing a harvest, check **Settings → Actions → General → Workflow permissions** and ensure write permissions are enabled where possible.

### Experiment without using credits

All code uses Python 3.12's standard library. You can preview the *exact generator prompt instructions* without calling Gemini or fetching source data:

```bash
python -m unittest discover -s tests -v
python scripts/engine.py --mode hybrid --dry-run
python scripts/engine.py --mode auto --dry-run
python scripts/engine.py --mode single --repos LV426 --preset dingbat --dry-run
python scripts/engine.py --repos slime_molds,klein-fluid-sim,LV426 --preset dingbat --dry-run
```

The preview lands in `PREVIEW.md` locally. A dry run does not create a volume. For a real local run, set `GEMINI_API_KEY` in your environment and run `python scripts/engine.py`.

### Configuration & source evidence

Edit [config.json](config.json) to change the solo list, the hand-picked crossbreeds, source role hints, preset rotations and model. Default model: `gemini-2.5-flash-lite`. Google API usage may count against a free-tier quota or incur charges depending on your account and the [current prices](https://ai.google.dev/gemini-api/docs/pricing). A successful daily harvest calls Gemini **once**.

The source scout uses public GitHub metadata, README text and root filenames, plus optional notes at `codices/REPO.md`. It does *not* download entire repositories, execute any source code or guarantee that every specialized concept is documented in a README. The instructions treat retrieved text as untrusted data. Add specialist notes if a repository's README is thin.

The `source_dna` requirement checks **format and completeness**; it cannot fully fact-check the model's scientific claims. Review prompts before you present them as mathematics or scholarship.

### What it saves

- [HARVEST.md](HARVEST.md): clickable prompt-volume index, in order.
- `harvest/volume-###-.../PROMPTS.md`: fully copy-pasteable human-readable prompt pack.
- `harvest/volume-###-.../prompts.json`: structured pack for future dashboards/integrations.
- `harvest/volume-###-.../MANIFEST.json`: exactly which parents and format fed that volume.

**NOT** a renderer, TTF exporter or Netlify app. Daddy Dingy remains the font forge; Git Shitter produces its potentially infinite supply of dubious mathematical offspring.
