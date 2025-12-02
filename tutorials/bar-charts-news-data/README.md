  # Bar Charts in Python Using Real News Data

  Learn to create bar charts in Python using Matplotlib and real news data from the NewsDataHub API.
  [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/newsdatahub/newsdatahub-data-science-tutorials/blob/main/tutorials/bar-charts-news-data/bar_charts.ipynb)

  ## What You'll Build

  - **Topic distribution chart**
    
    <img width="600" height="300" alt="topic-distribution-chart" src="https://github.com/user-attachments/assets/70a2f756-a251-46bf-9e04-3511450e279d" />

  - **Language distribution chart**
    
    <img width="600" height="300" alt="language-distribution-chart" src="https://github.com/user-attachments/assets/a745f700-ccac-4ffe-97a1-0b54e3804d4d" />

  - **Top 10 sources chart**

    <img width="600" height="300" alt="top-sources-chart" src="https://github.com/user-attachments/assets/bb43dd1b-54b9-4c55-babf-fa18c6924646" />

  - **Political leaning chart**
    
    <img width="600" height="300" alt="political-leaning-chart" src="https://github.com/user-attachments/assets/88b316dd-8c4f-47d0-aec1-66f3d1cd6fde" />


  ## Quick Start

  ### Option 1: Jupyter Notebook (Interactive)

  **With sample data (no API key needed):**
  ```bash
  pip install requests matplotlib
  jupyter notebook bar_charts.ipynb
  # Leave API_KEY = "" to auto-download sample data from GitHub
  ```

  **With live data:**
  ```bash
  pip install requests matplotlib
  jupyter notebook bar_charts.ipynb
  # Set API_KEY = "your-key-here" in the notebook
  # Get free API key: https://newsdatahub.com/login
  ```

  ### Option 2: Python Script (Command Line)

  **With sample data (no API key needed):**
  ```bash
  pip install requests matplotlib
  python bar_charts.py
  # Sample data auto-downloads from GitHub if not present
  ```

  **With live data:**
  ```bash
  pip install requests matplotlib
  # Edit bar_charts.py and set API_KEY = "your-key-here"
  python bar_charts.py
  ```

  ## Files

  - bar-charts.ipynb — Interactive Jupyter notebook (recommended)
  - bar_charts.py — Standalone Python script
  - data/sample-news-data.json — Sample dataset (200 articles)

  ## Generated Output

  Generates 3-4 PNG files:
  - topic-distribution-chart.png
  - language-distribution-chart.png
  - top-sources-chart.png
  - political-leaning-chart.png (if data available)

  ## Tutorial

  Complete walkthrough with explanations: https://newsdatahub.com/learning-center/article/bar-charts-in-python-using-real-news-data

  ## Resources

  - https://newsdatahub.com/docs
  - https://newsdatahub.com/login
  - https://newsdatahub.com/plans

  License

  MIT
