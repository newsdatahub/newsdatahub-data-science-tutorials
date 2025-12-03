# Treemap Visualization: Topic Distribution with NewsDataHub

Learn how to create professional treemap visualizations in Python using Squarify and real news data from the NewsDataHub API.
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/newsdatahub/newsdatahub-data-science-tutorials/blob/main/tutorials/treemap-topic-distribution/treemap-visualization.ipynb)

## What You'll Build
<img width="600" height="450" alt="topic-distribution-treemap" src="https://github.com/user-attachments/assets/0ba1d34a-ef5a-4b2a-926b-d927b8cd81eb" />


- **Topic distribution treemap** — Visualize the top 20 most popular topics in news coverage
- **Enhanced treemap with counts** — Display both topic names and article counts
- **Space-efficient visualization** — Show 20+ categories in a single, readable chart

## Quick Start

### Option 1: Jupyter Notebook (Interactive)

**With sample data (no API key needed):**
```bash
pip install requests matplotlib squarify
jupyter notebook treemap-visualization.ipynb
# Leave API_KEY = "" to auto-download sample data from GitHub
```

**With live data:**
```bash
pip install requests matplotlib squarify
jupyter notebook treemap-visualization.ipynb
# Set API_KEY = "your-key-here" in the notebook
# Get free API key: https://newsdatahub.com/login
```

### Option 2: Python Script (Command Line)

**With sample data (no API key needed):**
```bash
pip install requests matplotlib squarify
python treemap-visualization.py
# Sample data auto-downloads from GitHub if not present
```

**With live data:**
```bash
pip install requests matplotlib squarify
# Edit treemap-visualization.py and set API_KEY = "your-key-here"
python treemap-visualization.py
```

## Files

- treemap-visualization.ipynb — Interactive Jupyter notebook (recommended)
- treemap-visualization.py — Standalone Python script

## Generated Output

Generates 2 PNG files:
- topic-distribution-treemap.png
- topic-distribution-treemap-with-counts.png

## Tutorial

Complete walkthrough with explanations: https://newsdatahub.com/learning-center/article/treemap-visualization-topic-distribution-with-newsdatahub

## Resources

- https://newsdatahub.com/docs
- https://newsdatahub.com/login
- https://newsdatahub.com/plans

License

MIT
