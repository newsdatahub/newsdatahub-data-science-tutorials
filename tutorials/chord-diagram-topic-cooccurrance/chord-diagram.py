import requests
import matplotlib.pyplot as plt
from mpl_chord_diagram import chord_diagram
from collections import defaultdict, Counter
import json
import os

# Set your API key here (or leave empty to use sample data)
API_KEY = ""  # Replace with your NewsDataHub API key, or leave empty

# Check if API key is provided
if API_KEY and API_KEY != "your_api_key":
    print("Using live API data...")

    url = "https://api.newsdatahub.com/v1/news"
    headers = {"x-api-key": API_KEY}
    params = {"per_page": 100}

    # Fetch data
    response = requests.get(url, headers=headers, params=params)
    response.raise_for_status()
    articles = response.json().get("data", [])

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
# Extract Topics and Build Co-occurrence Matrix
# ============================================================================

# Extract topics from articles
article_topics = []
for article in articles:
    topics = article.get("topics", [])
    if topics and len(topics) >= 2:  # Need at least 2 topics for co-occurrence
        article_topics.append(topics)

print(f"\nFound {len(article_topics)} articles with 2+ topics")

# Count individual topic frequencies to get top topics
topic_counter = Counter()
for topics in article_topics:
    topic_counter.update(topics)

# Select top N topics for visualization clarity
TOP_N = 8
top_topics = [topic for topic, count in topic_counter.most_common(TOP_N)]

print(f"Top {TOP_N} topics: {top_topics}")

# Build co-occurrence matrix
cooccurrence = defaultdict(lambda: defaultdict(int))

for topics in article_topics:
    # Only count co-occurrences within our top topics
    filtered_topics = [t for t in topics if t in top_topics]

    # Count each pair
    for i, topic1 in enumerate(filtered_topics):
        for topic2 in filtered_topics[i+1:]:
            # Make matrix symmetric (topic A-B same as B-A)
            cooccurrence[topic1][topic2] += 1
            cooccurrence[topic2][topic1] += 1

print(f"Built co-occurrence matrix for {len(top_topics)} topics")

# ============================================================================
# Create Chord Diagram with mpl_chord_diagram
# ============================================================================

# Build a matrix for the chord diagram
# Create matrix with topic names and values
matrix = []
for source in top_topics:
    row = []
    for target in top_topics:
        row.append(cooccurrence[source][target])
    matrix.append(row)

print(f"Created {len(top_topics)}x{len(top_topics)} co-occurrence matrix")

# Create figure
fig, ax = plt.subplots(figsize=(10, 10))

# Create chord diagram
chord_diagram(matrix, names=top_topics, ax=ax)

# Style the visualization
ax.set_title('Topic Co-occurrence in Global News',
             fontsize=16, fontweight='bold', pad=20)

# Save the visualization
plt.tight_layout()
plt.savefig('topic_cooccurrence_chord.png', dpi=300, bbox_inches='tight')

print("\n" + "="*60)
print("Chord diagram created successfully!")
print("="*60)
print("\nFile created: topic_cooccurrence_chord.png")
print("\nVisualization features:")
print("  - Thicker ribbons = stronger topic relationships")
print("  - Arc size indicates topic's total involvement in connections")
print("  - Colors help distinguish between different topics")
