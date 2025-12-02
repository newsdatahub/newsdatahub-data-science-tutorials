# Sankey Diagram: News Sources to Topic Flows

Learn how to create beautiful Sankey diagrams in Python using Plotly to visualize how news sources distribute their coverage across topics using real NewsDataHub API data.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/newsdatahub/newsdatahub-data-science-tutorials/blob/main/tutorials/sankey-diagram-topic-flows/sankey-diagram.ipynb)

## What You'll Build

<img width="600" height="300" alt="news_source_topic_sankey" src="https://github.com/user-attachments/assets/b9fbb510-299f-4916-bcc7-57366a948d98" />

- **Source-to-topic flow visualization** — See how each news outlet distributes coverage across different topics
- **Interactive diagrams** — Hover over flows to see details in the notebook
- **Publication-ready images** — Generate high-resolution PNG files with the Python script
- **Professional styling** — Color-coded sources with clean, presentation-ready design
- **Top 10 sources filter** — Focuses on most active sources for clarity

## Quick Start

### Option 1: Jupyter Notebook (Interactive)

**With sample data (no API key needed):**
```bash
pip install requests plotly
jupyter notebook sankey-diagram.ipynb
# Leave API_KEY = "" to auto-download sample data from GitHub
```

**With live data:**
```bash
pip install requests plotly
jupyter notebook sankey-diagram.ipynb
# Set API_KEY = "your-key-here" in the notebook
# Get free API key: https://newsdatahub.com/login
```

### Option 2: Python Script (Command Line)

**With sample data (no API key needed):**
```bash
pip install requests plotly kaleido
python sankey-diagram.py
# Sample data auto-downloads from GitHub if not present
```

**With live data:**
```bash
pip install requests plotly kaleido
# Edit sankey-diagram.py and set API_KEY = "your-key-here"
python sankey-diagram.py
```

**Note:** `kaleido` is only required for the Python script to export PNG files.

## Files

- sankey-diagram.ipynb — Interactive Jupyter notebook (recommended)
- sankey-diagram.py — Standalone Python script
- sample-news-data.json — Sample dataset (auto-downloaded if needed)

## Generated Output

**Jupyter Notebook:** Interactive Sankey diagram displayed inline

**Python Script:** Generates PNG file:
- news_source_topic_sankey.png — High-resolution image (1200x700, 2x scale)

## Features

- **Top 10 source filtering** — Automatically limits visualization to most active sources
- **Multi-topic handling** — Properly processes NewsDataHub's array-based topic structure
- **Custom labels** — Shows "Source → Topic: N articles" format
- **Professional color scheme** — Bright, vibrant colors for both sources and topics with color-coded flows
- **High-resolution output** — PNG files with 2x scale for retina displays (script only)

## Tutorial

Complete walkthrough with explanations: https://newsdatahub.com/learning-center/article/sankey-diagram-news-sources-to-topic-flows

## Resources

- https://newsdatahub.com/docs
- https://newsdatahub.com/login
- https://newsdatahub.com/plans

## License

MIT
