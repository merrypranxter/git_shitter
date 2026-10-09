# 18 Custom Copilot Agent Prompts — Math + Style Repo Nursery

All files use the GitHub custom agent format shown in the user screenshot:

```yaml
---
name: exact-subject-specialist
description: Precisely scoped knowledge expert
---

# Subject — Repository Specialist

Specific instructions...
```

**Staging is not installation.** These 18 files are intentionally stored inside per-repo seed folders on Git Shitter's experimental branch. GitHub recognizes an agent for a given repository only when its file is placed at that repository's *root* `.github/agents/*.agent.md` (and made available on its default branch as applicable). For example, to install the circle inversion specialist in the future `circle_inversion` repository, copy the full contents from `seed_lab/first-wave/circle_inversion/.github/agents/circle-inversion.agent.md` to `circle_inversion/.github/agents/circle-inversion.agent.md`.

**Do not paste all 18 specialists into `git_shitter/.github/agents`.** That would make them agents of Git Shitter instead of their intended domains. Each one belongs in its own source repo after the repo is created.

| Intended new repository | Phase | Agent prompt | Target path in new repo |
|---|---|---|---|
| `circle_inversion` | first-wave | [Open prompt](https://github.com/merrypranxter/git_shitter/blob/seed-lab/first-wave-math-style/seed_lab/first-wave/circle_inversion/.github/agents/circle-inversion.agent.md) | `.github/agents/circle-inversion.agent.md` |
| `guilloche_engine` | first-wave | [Open prompt](https://github.com/merrypranxter/git_shitter/blob/seed-lab/first-wave-math-style/seed_lab/first-wave/guilloche_engine/.github/agents/guilloche-engine.agent.md) | `.github/agents/guilloche-engine.agent.md` |
| `catastrophe_theory` | first-wave | [Open prompt](https://github.com/merrypranxter/git_shitter/blob/seed-lab/first-wave-math-style/seed_lab/first-wave/catastrophe_theory/.github/agents/catastrophe-theory.agent.md) | `.github/agents/catastrophe-theory.agent.md` |
| `tropical_geometry` | first-wave | [Open prompt](https://github.com/merrypranxter/git_shitter/blob/seed-lab/first-wave-math-style/seed_lab/first-wave/tropical_geometry/.github/agents/tropical-geometry.agent.md) | `.github/agents/tropical-geometry.agent.md` |
| `foil_sticker_aesthetics` | first-wave | [Open prompt](https://github.com/merrypranxter/git_shitter/blob/seed-lab/first-wave-math-style/seed_lab/first-wave/foil_sticker_aesthetics/.github/agents/foil-sticker-aesthetics.agent.md) | `.github/agents/foil-sticker-aesthetics.agent.md` |
| `cosmic_airbrush_1984` | first-wave | [Open prompt](https://github.com/merrypranxter/git_shitter/blob/seed-lab/first-wave-math-style/seed_lab/first-wave/cosmic_airbrush_1984/.github/agents/cosmic-airbrush-1984.agent.md) | `.github/agents/cosmic-airbrush-1984.agent.md` |
| `rauzy_fractals` | backlog | [Open prompt](https://github.com/merrypranxter/git_shitter/blob/seed-lab/first-wave-math-style/seed_lab/backlog/rauzy_fractals/.github/agents/rauzy-fractals.agent.md) | `.github/agents/rauzy-fractals.agent.md` |
| `braid_groups` | backlog | [Open prompt](https://github.com/merrypranxter/git_shitter/blob/seed-lab/first-wave-math-style/seed_lab/backlog/braid_groups/.github/agents/braid-groups.agent.md) | `.github/agents/braid-groups.agent.md` |
| `spectre_monotiles` | backlog | [Open prompt](https://github.com/merrypranxter/git_shitter/blob/seed-lab/first-wave-math-style/seed_lab/backlog/spectre_monotiles/.github/agents/spectre-monotiles.agent.md) | `.github/agents/spectre-monotiles.agent.md` |
| `p_adic_dynamics` | backlog | [Open prompt](https://github.com/merrypranxter/git_shitter/blob/seed-lab/first-wave-math-style/seed_lab/backlog/p_adic_dynamics/.github/agents/p-adic-dynamics.agent.md) | `.github/agents/p-adic-dynamics.agent.md` |
| `dessins_denfants` | backlog | [Open prompt](https://github.com/merrypranxter/git_shitter/blob/seed-lab/first-wave-math-style/seed_lab/backlog/dessins_denfants/.github/agents/dessins-denfants.agent.md) | `.github/agents/dessins-denfants.agent.md` |
| `discrete_morse_theory` | backlog | [Open prompt](https://github.com/merrypranxter/git_shitter/blob/seed-lab/first-wave-math-style/seed_lab/backlog/discrete_morse_theory/.github/agents/discrete-morse-theory.agent.md) | `.github/agents/discrete-morse-theory.agent.md` |
| `spectral_graphs` | backlog | [Open prompt](https://github.com/merrypranxter/git_shitter/blob/seed-lab/first-wave-math-style/seed_lab/backlog/spectral_graphs/.github/agents/spectral-graphs.agent.md) | `.github/agents/spectral-graphs.agent.md` |
| `mechanical_linkages` | backlog | [Open prompt](https://github.com/merrypranxter/git_shitter/blob/seed-lab/first-wave-math-style/seed_lab/backlog/mechanical_linkages/.github/agents/mechanical-linkages.agent.md) | `.github/agents/mechanical-linkages.agent.md` |
| `xerox_rave_flyers` | backlog | [Open prompt](https://github.com/merrypranxter/git_shitter/blob/seed-lab/first-wave-math-style/seed_lab/backlog/xerox_rave_flyers/.github/agents/xerox-rave-flyers.agent.md) | `.github/agents/xerox-rave-flyers.agent.md` |
| `scientific_transparencies` | backlog | [Open prompt](https://github.com/merrypranxter/git_shitter/blob/seed-lab/first-wave-math-style/seed_lab/backlog/scientific_transparencies/.github/agents/scientific-transparencies.agent.md) | `.github/agents/scientific-transparencies.agent.md` |
| `print_registration_chaos` | backlog | [Open prompt](https://github.com/merrypranxter/git_shitter/blob/seed-lab/first-wave-math-style/seed_lab/backlog/print_registration_chaos/.github/agents/print-registration-chaos.agent.md) | `.github/agents/print-registration-chaos.agent.md` |
| `jelly_plastic_y2k` | backlog | [Open prompt](https://github.com/merrypranxter/git_shitter/blob/seed-lab/first-wave-math-style/seed_lab/backlog/jelly_plastic_y2k/.github/agents/jelly-plastic-y2k.agent.md) | `.github/agents/jelly-plastic-y2k.agent.md` |

## What these specialists actually do
- Research their specific mathematical or artistic domain accurately and with clear sources.
- Fill subject taxonomies, reference docs, formula/visual or production rules, examples, tests and machine-readable context manifests.
- Read existing code and seed materials before proposing files.
- Distinguish real mechanics and scientific facts from speculative/psychedelic extrapolations.
- Create reusable deterministic operators, renderers, SVG or PNG outputs as appropriate; avoid recurring paid AI.
- Explain useful causal crossbreeds with existing Merry repos.
- Leave personal laboratories intact; monetization and customer packaging are separate.

## Promotion checklist
1. Create or identify the intended source repo and inspect it for overlaps.
2. Copy that repo's seed and agent prompt to the source repo's **root** paths.
3. Merge or commit to its default branch to make the agent available.
4. Ask the specialist to fill its reference material, build low-cost examples and verify actual behavior.
5. Only add a new live source to Git Shitter `config.json` after the corresponding repo really exists.

No standalone mathematical repos were created by staging these files; no live scheduled workflow or storefront was modified.
