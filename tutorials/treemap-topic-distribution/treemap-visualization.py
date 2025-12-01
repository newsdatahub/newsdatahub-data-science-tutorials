import requests
import matplotlib.pyplot as plt
import squarify
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

    # Fetch 100 articles
    params = {"per_page": 100}

    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    data = response.json()

    articles = data.get("data", [])
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
# Extract and Count Topics
# ============================================================================
# Extract topics - NewsDataHub returns 'topics' as an array
topics = []
for article in articles:
    article_topics = article.get("topics", [])
    if article_topics:
        # If topics is a list, extend our topics list
        if isinstance(article_topics, list):
            topics.extend(article_topics)
        else:
            topics.append(article_topics)

print(f"\nTotal topic mentions: {len(topics)}")

# Count topic occurrences
topic_counts = Counter(topics)
print(f"Found {len(topic_counts)} unique topics")

# Get top 20 topics for visualization
top_topics = dict(topic_counts.most_common(20))
print(f"Displaying top 20 topics out of {len(topic_counts)} total")

# ============================================================================
# Create Treemap Visualization
# ============================================================================
# Prepare data for plotting
labels = list(top_topics.keys())
sizes = list(top_topics.values())

# Vibrant color palette for visual distinction
colors = [
    '#EF4444',  # Red
    '#3B82F6',  # Blue
    '#10B981',  # Green
    '#FBBF24',  # Yellow
    '#8B5CF6',  # Purple
    '#F59E0B',  # Orange
    '#EC4899',  # Pink
    '#14B8A6',  # Teal
    '#6366F1',  # Indigo
    '#F97316',  # Orange-red
    '#FF6B6B',  # Light red
    '#4ECDC4',  # Cyan
    '#45B7D1',  # Sky blue
    '#FFA07A',  # Light salmon
    '#98D8C8',  # Mint
    '#F7DC6F',  # Light yellow
    '#BB8FCE',  # Lavender
    '#85C1E2',  # Baby blue
    '#52B788',  # Forest green
    '#34D399'   # Emerald
]

# Create figure with appropriate size
plt.figure(figsize=(16, 10))

# Create treemap using squarify
squarify.plot(
    sizes=sizes,
    label=labels,
    color=colors[:len(labels)],
    alpha=0.8,
    text_kwargs={'fontsize': 11, 'weight': 'bold', 'color': 'white'},
    edgecolor='white',
    linewidth=3
)

# Style the chart
plt.title('Topic Distribution in Current News Coverage',
          fontsize=18, fontweight='bold', pad=20)
plt.axis('off')  # Remove axes for cleaner look

plt.tight_layout()
plt.savefig('topic-distribution-treemap.png', dpi=300, bbox_inches='tight')
print("\n✓ Treemap visualization saved: topic-distribution-treemap.png")

# ============================================================================
# Create Enhanced Treemap with Value Labels
# ============================================================================
# Create labels with topic names and counts
labels_with_counts = [f"{topic}\n({count})" for topic, count in top_topics.items()]

plt.figure(figsize=(16, 10))

squarify.plot(
    sizes=sizes,
    label=labels_with_counts,
    color=colors[:len(labels)],
    alpha=0.8,
    text_kwargs={'fontsize': 10, 'weight': 'bold', 'color': 'white'},
    edgecolor='white',
    linewidth=3
)

plt.title('Topic Distribution in Current News Coverage (with counts)',
          fontsize=18, fontweight='bold', pad=20)
plt.axis('off')

plt.tight_layout()
plt.savefig('topic-distribution-treemap-with-counts.png', dpi=300, bbox_inches='tight')
print("✓ Enhanced treemap with counts saved: topic-distribution-treemap-with-counts.png")

print("\nAll visualizations generated successfully!")
print("Files created:")
print("  - topic-distribution-treemap.png")
print("  - topic-distribution-treemap-with-counts.png")
