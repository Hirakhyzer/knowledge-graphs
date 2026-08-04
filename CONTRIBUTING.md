# Contributing

Thank you for considering a contribution to Knowledge Graphs Lab.

This repository welcomes improvements that make the project more useful for academic research, graph analytics, explainable AI, and knowledge representation.

---

## Useful Contribution Areas

- Add new sample datasets.
- Improve graph analytics utilities.
- Add graph visualization examples.
- Improve documentation and diagrams.
- Add tests for edge cases.
- Build importers for BibTeX, CSV, JSON-LD, or RDF-style data.

---

## Development Setup

```bash
git clone https://github.com/Hirakhyzer/knowledge-graphs.git
cd knowledge-graphs
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest
```

On Windows, activate the environment with:

```bash
.venv\Scripts\activate
```

---

## Coding Guidelines

- Keep functions small and easy to test.
- Use clear names for node types and relation types.
- Preserve evidence text when creating graph relations.
- Avoid hard-coding project-specific assumptions into reusable utilities.
- Add tests for new behavior.

---

## Documentation Guidelines

When adding a new graph concept, include:

1. What the node or relation means.
2. Why it is useful.
3. Example input data.
4. Expected output or graph structure.
5. Limitations or assumptions.

---

## Pull Request Checklist

Before opening a pull request:

- [ ] The code runs locally.
- [ ] Tests pass.
- [ ] Documentation is updated.
- [ ] New graph data is small enough for the repository.
- [ ] Any generated or derived data is clearly labeled.

---

## Academic Integrity

Please do not add fabricated citations, unsupported claims, or misleading benchmark results. All research-oriented examples should be clearly labeled as sample, synthetic, or source-derived.
