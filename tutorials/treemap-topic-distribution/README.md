# Treemap Visualization: Topic Distribution with NewsDataHub

Learn how to create professional treemap visualizations in Python using Squarify and real news data from the NewsDataHub API.

## What You'll Build
<img width="600" height="450" alt="topic-distribution-treemap" src="https://github.com/user-attachments/assets/0ba1d34a-ef5a-4b2a-926b-d927b8cd81eb" />


- **Topic distribution treemap** — Visualize the top 20 most popular topics in news coverage
- **Enhanced treemap with counts** — Display both topic names and article counts
- **Space-efficient visualization** — Show 20+ categories in a single, readable chart

## Prerequisites

- Python 3.7+
- NewsDataHub API key ([Get free key](https://newsdatahub.com/login))

## Installation

```bash
pip install requests matplotlib squarify
```

## Quick Start

1. Clone this repository
2. Replace `your_api_key_here` in the script with your NewsDataHub API key (or leave empty to use sample data)
3. Run the script:

```bash
python treemap-visualization.py
```

4. Check your directory for generated PNG files

## Features

- **Sample data support** — Works without API key by downloading sample news data
- **Top 20 topics filter** — Focuses on dominant topics for readability
- **Vibrant color palette** — 20 distinct, high-contrast colors optimized for data visualization
- **Multiple visualizations** — Basic treemap + enhanced version with article counts
- **High-resolution export** — 300 DPI treemaps ready for reports and presentations
- **White borders** — Clear separation between topic rectangles

## Generated Visualizations

The script generates 2 PNG files:
- `topic-distribution-treemap.png` — Clean treemap with topic names
- `topic-distribution-treemap-with-counts.png` — Treemap with article counts included

## Tutorial

For the complete step-by-step tutorial, visit:
[How to Create Treemap Visualizations in Python to Display Topic Distribution](https://newsdatahub.com/learning-center/article/treemap-visualization-topic-distribution-with-newsdatahub)

## API Documentation

- [NewsDataHub API Docs](https://newsdatahub.com/docs)
- [API Plans & Pricing](https://newsdatahub.com/plans)

## License

MIT
