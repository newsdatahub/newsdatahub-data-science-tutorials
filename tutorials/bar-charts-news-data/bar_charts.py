import requests
import matplotlib.pyplot as plt
from collections import Counter
import json
import os

# Set your API key here (or leave empty to use sample data)
API_KEY = ""  # Replace with your NewsDataHub API key, or leave empty

# Check if API key is provided
if API_KEY and API_KEY != "your_api_key_here":
    print("Using live API data...")

    url = "https://api.newsdatahub.com/v1/news"
    headers = {"x-api-key": API_KEY}

    articles = []
    cursor = None

    # Fetch 2 pages (up to 200 articles)
    for _ in range(2):
        params = {"per_page": 100, "country": "US,FR,DE,ES,BR", "source_type": "mainstream_news,digital_native"}
        if cursor:
            params["cursor"] = cursor

        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        data = response.json()

        articles.extend(data.get("data", []))
        cursor = data.get("next_cursor")
        if not cursor:
            break

    print(f"Fetched {len(articles)} articles from API")

else:
    print("No API key provided. Loading sample data...")

    # Download sample data if not already present
    sample_file = "sample-news-data.json"

    if not os.path.exists(sample_file):
        print("Downloading sample data...")
        sample_url = "https://raw.githubusercontent.com/newsdatahub/newsdatahub-data-science-tutorials/main/tutorials/bar-charts-news-data/data/sample-news-data.json"
        response = requests.get(sample_url)
        with open(sample_file, "w") as f:
            json.dump(response.json(), f)
        print(f"Sample data saved to {sample_file}")

    # Load sample data
    with open(sample_file, "r") as f:
        data = json.load(f)

    # Handle both formats: raw array or API response with 'data' key
    if isinstance(data, dict) and "data" in data:
        articles = data["data"]
    elif isinstance(data, list):
        articles = data
    else:
        raise ValueError("Unexpected sample data format")

    print(f"Loaded {len(articles)} articles from sample data")

# ============================================================================
# 1. Topic Distribution
# ============================================================================
# Extract topics - NewsDataHub returns 'topics' as an array, not 'topic' as a string
topics = []
for article in articles:
    article_topics = article.get("topics", [])
    if article_topics:
        # If topics is a list, extend our topics list
        if isinstance(article_topics, list):
            topics.extend(article_topics)
        else:
            topics.append(article_topics)

# Exclude 'general' topic (articles not yet categorized)
topics = [t for t in topics if t != 'general']

topic_counts = Counter(topics)
print(f"\nFound {len(topic_counts)} unique topics (excluding 'general')")

# Get top 15 topics to avoid chart clutter
top_topics = dict(topic_counts.most_common(15))
print(f"Displaying top 15 topics out of {len(topic_counts)} total")

# Vibrant color palette
vibrant_colors = [
    '#EF4444',  # Red
    '#3B82F6',  # Blue
    '#10B981',  # Green
    '#FBBF24',  # Yellow
    '#8B5CF6',  # Purple
    '#F59E0B',  # Orange
    '#EC4899',  # Pink
    '#14B8A6',  # Teal
    '#6366F1',  # Indigo
    '#F97316'   # Orange-red
]

plt.figure(figsize=(12, 6))
categories = list(top_topics.keys())
values = list(top_topics.values())
colors = [vibrant_colors[i % len(vibrant_colors)] for i in range(len(categories))]

bars = plt.bar(categories, values, color=colors, edgecolor='white', linewidth=2)

plt.title("Top 15 Topics in News Coverage", fontsize=16, fontweight="bold", pad=20)
plt.xlabel("Topic", fontsize=12, fontweight="bold")
plt.ylabel("Article Count", fontsize=12, fontweight="bold")
plt.xticks(rotation=45, ha="right", fontsize=11)
plt.yticks(fontsize=11)
plt.grid(axis="y", linestyle="--", alpha=0.3)

# Add value labels on bars
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height,
             f'{int(height)}', ha='center', va='bottom', fontsize=11, fontweight='bold')

plt.tight_layout()
plt.savefig("topic-distribution-chart.png", dpi=300, bbox_inches="tight")
print("✓ Topic distribution chart saved")

# ============================================================================
# 2. Language Distribution (Horizontal)
# ============================================================================
languages = [a.get("language") for a in articles if a.get("language")]
lang_counts = Counter(languages)

plt.figure(figsize=(10, 6))
categories = list(lang_counts.keys())
values = list(lang_counts.values())
colors = [vibrant_colors[i % len(vibrant_colors)] for i in range(len(categories))]

bars = plt.barh(categories, values, color=colors, edgecolor='white', linewidth=2)

plt.title("Language Distribution in News Coverage", fontsize=16, fontweight="bold", pad=20)
plt.xlabel("Article Count", fontsize=12, fontweight="bold")
plt.ylabel("Language", fontsize=12, fontweight="bold")
plt.xticks(fontsize=11)
plt.yticks(fontsize=11)
plt.grid(axis="x", alpha=0.3, linestyle="--")

# Add value labels
for bar in bars:
    width = bar.get_width()
    plt.text(width, bar.get_y() + bar.get_height()/2.,
             f'{int(width)}', ha='left', va='center', fontsize=11, fontweight='bold',
             bbox=dict(boxstyle='round,pad=0.3', facecolor='white', alpha=0.7, edgecolor='none'))

plt.tight_layout()
plt.savefig("language-distribution-chart.png", dpi=300, bbox_inches="tight")
print("✓ Language distribution chart saved")

# ============================================================================
# 3. Top 10 Sources
# ============================================================================
# Extract source titles from article level
sources = []
for article in articles:
    source_title = article.get("source_title")
    if source_title:
        sources.append(source_title)

print(f"\nFound {len(sources)} articles with source information")
source_counts = Counter(sources)
top10 = source_counts.most_common(10)

plt.figure(figsize=(12, 6))
categories = [x[0] for x in top10]
values = [x[1] for x in top10]
colors = [vibrant_colors[i % len(vibrant_colors)] for i in range(len(categories))]

bars = plt.bar(categories, values, color=colors, edgecolor='white', linewidth=2)

plt.title("Top 10 Most Active News Sources", fontsize=16, fontweight="bold", pad=20)
plt.xlabel("News Source", fontsize=12, fontweight="bold")
plt.ylabel("Article Count", fontsize=12, fontweight="bold")
plt.xticks(rotation=45, ha="right", fontsize=11)
plt.yticks(fontsize=11)
plt.grid(axis="y", alpha=0.3, linestyle="--")

# Add value labels
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height,
             f'{int(height)}', ha='center', va='bottom', fontsize=11, fontweight='bold')

plt.tight_layout()
plt.savefig("top-sources-chart.png", dpi=300, bbox_inches="tight")
print("✓ Top sources chart saved")

# ============================================================================
# 4. Political Leaning
# ============================================================================

leanings = [
    article.get("source", {}).get("political_leaning")
    for article in articles
    if article.get("source", {}).get("political_leaning")
]
leaning_counts = Counter(leanings)

print(f"\nPolitical leaning: {len(leanings)} out of {len(articles)} articles have leaning data")
print(f"All leaning values found: {dict(leaning_counts)}")

# Define order: left to right political spectrum + nonpartisan
# 'nonpartisan' represents unbiased wire services (AP, Reuters, AFP) and fact-based outlets
order = ['far_left', 'left', 'center_left', 'center', 'center_right', 'right', 'far_right', 'nonpartisan']
categories = [cat for cat in order if cat in leaning_counts]
values = [leaning_counts[cat] for cat in categories]

print(f"Showing {sum(values)} articles across {len(categories)} categories (including nonpartisan)")

plt.figure(figsize=(12, 6))
colors = [vibrant_colors[i % len(vibrant_colors)] for i in range(len(categories))]
bars = plt.bar(categories, values, color=colors, edgecolor='white', linewidth=2)

plt.title('Political Leaning Distribution of News Sources (Including Nonpartisan)', fontsize=16, fontweight='bold', pad=20)
plt.xlabel('Political Leaning', fontsize=12, fontweight='bold')
plt.ylabel('Article Count', fontsize=12, fontweight='bold')
plt.xticks(fontsize=11)
plt.yticks(fontsize=11)
plt.grid(axis='y', alpha=0.3, linestyle='--')

# Add value labels
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height,
             f'{int(height)}', ha='center', va='bottom', fontsize=11, fontweight='bold')

plt.tight_layout()
plt.savefig('political-leaning-chart.png', dpi=300, bbox_inches='tight')
print("✓ Political leaning chart saved")

print("\nAll charts generated successfully!")
print("Files created:")
print("  - topic-distribution-chart.png")
print("  - language-distribution-chart.png")
print("  - top-sources-chart.png")
print("  - political-leaning-chart.png")
