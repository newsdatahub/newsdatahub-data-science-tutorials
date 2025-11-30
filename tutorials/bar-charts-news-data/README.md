# Bar Charts in Python Using Real News Data

Learn how to create professional bar charts in Python using Matplotlib and real news data from the NewsDataHub API.

## What You'll Build

- **Topic distribution chart** — Visualize the top 15 most popular topics
- **Language distribution chart** — Analyze article distribution across languages
- **Top 10 sources chart** — Identify the most active news publishers
- **Political leaning chart** — Understand bias distribution (optional, requires paid plan)

## Prerequisites

- Python 3.7+
- NewsDataHub API key ([Get free key](https://newsdatahub.com/login))

## Installation

```bash
pip install requests matplotlib
```

## Quick Start

1. Clone this repository
2. Replace `your_api_key_here` in the script with your NewsDataHub API key
3. Run the script:

```bash
python news_bar_charts.py
```

4. Check your directory for generated PNG files

## Features

- **Multi-country data fetching** — Fetches from US, France, Germany, Spain, and Brazil for diverse language coverage
- **Cursor-based pagination** — Properly handles API pagination to fetch multiple pages
- **Top 15 topics filter** — Prevents chart clutter from rare topics
- **Vibrant color palette** — Professional, high-contrast colors optimized for data visualization
- **Value labels on bars** — Shows exact counts for easy reading
- **High-resolution export** — 300 DPI charts ready for reports and presentations

## Generated Charts

The script generates 4 PNG files:
- `topic-distribution-chart.png` — Top 15 topics in news coverage
- `language-distribution-chart.png` — Language distribution (horizontal bars)
- `top-sources-chart.png` — Top 10 most active news sources
- `political-leaning-chart.png` — Political leaning distribution (if available)

## Tutorial

For the complete step-by-step tutorial, visit:
[How to Create Bar Charts in Python Using Real News Data](https://newsdatahub.com/learning-center/article/bar-charts-in-python-using-real-news-data)

## API Documentation

- [NewsDataHub API Docs](https://newsdatahub.com/docs)
- [API Plans & Pricing](https://newsdatahub.com/plans)

## License

MIT

