# Circular News Wheel: Topic Distribution Using Polar Charts

Learn how to create a circular "news wheel" visualization using Python's polar area charts to display news topic distribution from NewsDataHub API.

## What You'll Build

- **Polar area chart** — Circular visualization showing topic distribution
- **Topic aggregation** — Extract and count topics from news articles
- **Professional styling** — Vibrant colors and clear labels
- **Top 10 filtering** — Display most popular topics without clutter

## Prerequisites

- Python 3.7+
- NewsDataHub API key ([Get free key](https://newsdatahub.com/login))

## Installation

```bash
pip install requests matplotlib numpy
```

## Quick Start

1. Clone this repository or download the script
2. Replace `your_api_key_here` in the script with your NewsDataHub API key (or leave empty to use sample data)
3. Run the script:

```bash
python circular-news-wheel.py
```

4. Check your directory for `topic_distribution_wheel.png`

## Features

- **Polar coordinate visualization** — Circular chart with radial segments
- **Top 10 topic filtering** — Prevents chart clutter from rare topics
- **Vibrant color palette** — Professional, high-contrast colors optimized for data visualization
- **Value labels on segments** — Shows exact counts for easy reading
- **High-resolution export** — 300 DPI chart ready for reports and presentations
- **Sample data fallback** — Works without API key using sample data

## Generated Output

The script generates:
- `topic_distribution_wheel.png` — Circular visualization of top 10 news topics

## Tutorial

For the complete step-by-step tutorial, visit:
[How to Create a Circular "News Wheel" with Python](https://newsdatahub.com/learning-center/article/circular-news-wheel-topic-distribution)

## API Documentation

- [NewsDataHub API Docs](https://newsdatahub.com/docs)
- [API Plans & Pricing](https://newsdatahub.com/plans)

## License

MIT
