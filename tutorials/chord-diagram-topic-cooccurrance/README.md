# Chord Diagram: Topic Co-occurrence in News Data

Learn how to create professional chord diagrams in Python using Matplotlib to visualize topic co-occurrence patterns in real news data from the NewsDataHub API.
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/newsdatahub/newsdatahub-data-science-tutorials/blob/main/tutorials/chord-diagram-topic-cooccurrance/chord-diagram.ipynb)

## What You'll Build

- **Topic co-occurrence chord diagram**
  
<img width="400" height="400" alt="topic_cooccurrence_chord" src="https://github.com/user-attachments/assets/b54f0a55-c899-404a-92d8-3b27bfe6c902" />

## Quick Start

### Option 1: Jupyter Notebook (Interactive)

**With sample data (no API key needed):**
```bash
pip install requests matplotlib mpl_chord_diagram
jupyter notebook chord-diagram.ipynb
# Leave API_KEY = "" to auto-download sample data from GitHub
```

**With live data:**
```bash
pip install requests matplotlib mpl_chord_diagram
jupyter notebook chord-diagram.ipynb
# Set API_KEY = "your-key-here" in the notebook
# Get free API key: https://newsdatahub.com/login
```

### Option 2: Python Script (Command Line)

**With sample data (no API key needed):**
```bash
pip install requests matplotlib mpl_chord_diagram
python chord-diagram.py
# Sample data auto-downloads from GitHub if not present
```

**With live data:**
```bash
pip install requests matplotlib mpl_chord_diagram
# Edit chord-diagram.py and set API_KEY = "your-key-here"
python chord-diagram.py
```

## Files

- chord-diagram.ipynb — Interactive Jupyter notebook (recommended)
- chord-diagram.py — Standalone Python script

## Generated Output

Generates PNG file:
- topic_cooccurrence_chord.png

## Tutorial

Complete walkthrough with explanations: https://newsdatahub.com/learning-center/article/chord-diagram-topic-cooccurrence

## Resources

- https://newsdatahub.com/docs
- https://newsdatahub.com/login
- https://newsdatahub.com/plans

License

MIT
