# Chord Diagram: Topic Co-occurrence in News Data

Learn how to create professional chord diagrams in Python using Matplotlib to visualize topic co-occurrence patterns in real news data from the NewsDataHub API.

## What You'll Build

- **Co-occurrence matrix** — Calculate how often topic pairs appear together
- **Chord diagram** — Circular visualization showing topic relationships
- **Professional styling** — High-resolution PNG output ready for reports and presentations

## Prerequisites

- Python 3.7+
- NewsDataHub API key ([Get free key](https://newsdatahub.com/login))

## Installation

```bash
pip install requests matplotlib mpl_chord_diagram
```

## Quick Start

1. Clone this repository or download the script
2. Replace the empty `API_KEY` variable with your NewsDataHub API key (or leave empty to use sample data)
3. Run the script:

```bash
python chord-diagram.py
```

4. Check your directory for the generated PNG file

## Features

- **Automatic sample data** — Works without API key using cached sample data
- **Top 8 topics selection** — Prevents clutter by focusing on most frequent topics
- **Co-occurrence calculation** — Builds symmetric matrix showing topic relationships
- **High-resolution export** — 300 DPI PNG ready for reports and presentations
- **Professional styling** — Clean, publication-ready output using matplotlib

## Output

The script generates `topic_cooccurrence_chord.png` containing a chord diagram where:
- **Thicker ribbons** = stronger topic relationships (more co-occurrences)
- **Arc size** = topic's total involvement in connections
- **Colors** = distinct topics around the circle

## Tutorial

For the complete step-by-step tutorial, visit:
[How to Create Chord Diagrams in Python](https://newsdatahub.com/learning-center/article/chord-diagram-topic-cooccurrence)

## API Documentation

- [NewsDataHub API Docs](https://newsdatahub.com/docs)
- [API Plans & Pricing](https://newsdatahub.com/plans)

## License

MIT
