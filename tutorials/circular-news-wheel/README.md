# Circular News Wheel: Topic Distribution Using Polar Charts

Learn how to create a circular "news wheel" visualization using Python's polar area charts to display news topic distribution from NewsDataHub API.
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/newsdatahub/newsdatahub-data-science-tutorials/blob/main/tutorials/circular-news-wheel/circular-news-wheel.ipynb)

## What You'll Build

- **Polar area chart** — Circular visualization showing topic distribution
- **Topic aggregation** — Extract and count topics from news articles
- **Professional styling** — Vibrant colors and clear labels
- **Top 10 filtering** — Display most popular topics without clutter

## Quick Start

### Option 1: Jupyter Notebook (Interactive)

**With sample data (no API key needed):**
```bash
pip install requests matplotlib numpy
jupyter notebook circular-news-wheel.ipynb
# Leave API_KEY = "" to auto-download sample data from GitHub
```

**With live data:**
```bash
pip install requests matplotlib numpy
jupyter notebook circular-news-wheel.ipynb
# Set API_KEY = "your-key-here" in the notebook
# Get free API key: https://newsdatahub.com/login
```

### Option 2: Python Script (Command Line)

**With sample data (no API key needed):**
```bash
pip install requests matplotlib numpy
python circular-news-wheel.py
# Sample data auto-downloads from GitHub if not present
```

**With live data:**
```bash
pip install requests matplotlib numpy
# Edit circular-news-wheel.py and set API_KEY = "your-key-here"
python circular-news-wheel.py
```

## Files

- circular-news-wheel.ipynb — Interactive Jupyter notebook (recommended)
- circular-news-wheel.py — Standalone Python script

## Generated Output

Generates PNG file:
- topic_distribution_wheel.png

## Tutorial

Complete walkthrough with explanations: https://newsdatahub.com/learning-center/article/circular-news-wheel-topic-distribution

## Resources

- https://newsdatahub.com/docs
- https://newsdatahub.com/login
- https://newsdatahub.com/plans

License

MIT
