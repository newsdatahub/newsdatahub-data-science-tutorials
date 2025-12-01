# Sankey Diagram: News Sources to Topic Flows

Learn how to create beautiful static Sankey diagrams in Python using Plotly to visualize how news sources distribute their coverage across topics using real NewsDataHub API data.

## What You'll Build

- **Source-to-topic flow visualization** — See how each news outlet distributes coverage across different topics
- **Publication-ready images** — Generate high-resolution PNG files
- **Professional styling** — Color-coded sources with clean, presentation-ready design
- **Top 10 sources filter** — Focuses on most active sources for clarity

## Prerequisites

- Python 3.7+
- NewsDataHub API key ([Get free key](https://newsdatahub.com/login))

## Installation

```bash
pip install requests plotly kaleido
```

**Note:** `kaleido` is required for exporting static PNG images.

## Quick Start

1. Replace the empty `API_KEY` variable in the script with your NewsDataHub API key, or leave it empty to use sample data
2. Run the script:

```bash
python sankey-diagram-news-sources-to-topic-flows_example.py
```

3. Open the generated PNG file to view your diagram

## Features

- **Top 10 source filtering** — Automatically limits visualization to most active sources
- **Multi-topic handling** — Properly processes NewsDataHub's array-based topic structure
- **Custom labels** — Shows "Source → Topic: N articles" format
- **Professional color scheme** — Bright, vibrant colors for both sources and topics with color-coded flows
- **High-resolution output** — PNG files with 2x scale for retina displays

## Generated Output

The script generates:
- `news_source_topic_sankey.png` — High-resolution raster image (1200x700, 2x scale)

## Tutorial

For the complete step-by-step tutorial with explanations, visit:
[How to Create Sankey Diagrams to Visualize News Source-to-Topic Flows](https://newsdatahub.com/learning-center/article/sankey-diagram-news-sources-to-topic-flows)

## API Documentation

- [NewsDataHub API Docs](https://newsdatahub.com/docs)
- [API Plans & Pricing](https://newsdatahub.com/plans)

## License

MIT
