import requests
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter
import json
import os

# Set your API key here (or leave empty to use sample data)
API_KEY = ""  # Replace with your NewsDataHub API key, or leave empty

# Initialize articles list
articles = []

# Check if API key is provided
if API_KEY and API_KEY != "your_api_key_here":
    print("Using live API data...")

    url = "https://api.newsdatahub.com/v1/news"
    headers = {"x-api-key": API_KEY}

    # Make 3 API calls to get more data
    for call_num in range(1, 4):
        print(f"  Fetching batch {call_num}/3...")
        params = {"per_page": 100}  # Maximum allowed on free tier

        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        batch_articles = response.json().get("data", [])
        articles.extend(batch_articles)

        print(f"  - Fetched {len(batch_articles)} articles")

    print(f"\nTotal articles fetched: {len(articles)}")

else:
    print("No API key provided. Loading sample data...")

    # Download and load 3 sample data files
    sample_files = [
        ("sample-news-data-1.json", "https://raw.githubusercontent.com/newsdatahub/newsdatahub-data-science-tutorials/5a8dc14f5c8a0e08eb9f621611b92c8e89903c4a/tutorials/circular-news-wheel/data/sample-news-data-1.json"),
        ("sample-news-data-2.json", "https://raw.githubusercontent.com/newsdatahub/newsdatahub-data-science-tutorials/5a8dc14f5c8a0e08eb9f621611b92c8e89903c4a/tutorials/circular-news-wheel/data/sample-news-data-2.json"),
        ("sample-news-data-3.json", "https://raw.githubusercontent.com/newsdatahub/newsdatahub-data-science-tutorials/5a8dc14f5c8a0e08eb9f621611b92c8e89903c4a/tutorials/circular-news-wheel/data/sample-news-data-3.json")
    ]

    for sample_file, sample_url in sample_files:
        # Download if not already present
        if not os.path.exists(sample_file):
            print(f"  Downloading {sample_file}...")
            response = requests.get(sample_url)
            response.raise_for_status()
            with open(sample_file, "w") as f:
                json.dump(response.json(), f)

        # Load sample data
        with open(sample_file, "r") as f:
            data = json.load(f)

        # Handle both formats: raw array or API response with 'data' key
        if isinstance(data, dict) and "data" in data:
            batch_articles = data["data"]
        elif isinstance(data, list):
            batch_articles = data
        else:
            raise ValueError(f"Unexpected sample data format in {sample_file}")

        articles.extend(batch_articles)
        print(f"  - Loaded {len(batch_articles)} articles from {sample_file}")

    print(f"\nTotal articles loaded: {len(articles)}")

# ============================================================================
# Extract and Count Topics
# ============================================================================
# Extract all topics from articles
all_topics = []
for article in articles:
    topics = article.get("topics", [])
    # Topics is an array - an article can have multiple topics
    if topics:
        all_topics.extend(topics)

print(f"\nTotal topic mentions: {len(all_topics)}")

# Exclude 'general' topic (articles not yet categorized)
all_topics = [t for t in all_topics if t != 'general']

# Count occurrences of each topic
topic_counts = Counter(all_topics)

# Get top 10 topics (to avoid overcrowding the chart)
top_topics = topic_counts.most_common(10)

# Separate into labels and values
labels = [topic for topic, count in top_topics]
values = [count for topic, count in top_topics]

print(f"Found {len(topic_counts)} unique topics (excluding 'general')")
print(f"Displaying top 10 topics out of {len(topic_counts)} total")
print(f"\nTop 10 topics:")
for topic, count in top_topics:
    print(f"  {topic}: {count}")

# ============================================================================
# Create Polar Area Chart
# ============================================================================
# Number of categories
num_topics = len(labels)

# Set up the polar plot
fig = plt.figure(figsize=(12, 12))
ax = fig.add_subplot(111, projection='polar')

# Define vibrant color palette
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
    '#F97316'   # Deep Orange
]

# Calculate angles for each segment (in radians)
angles = np.linspace(0, 2 * np.pi, num_topics, endpoint=False).tolist()

# Create the polar area chart
bars = ax.bar(
    angles,
    values,
    width=2*np.pi/num_topics,  # Width of each segment
    color=vibrant_colors[:num_topics],
    edgecolor='white',
    linewidth=2,
    alpha=0.8
)

# Customize the chart
ax.set_theta_zero_location('N')  # Start at top
ax.set_theta_direction(-1)  # Clockwise direction
ax.set_xticks(angles)
ax.set_xticklabels(labels, fontsize=12, fontweight='600')
ax.set_ylim(0, max(values) * 1.15)  # Add 15% padding for labels

# Style the radial grid
ax.grid(True, color='gray', alpha=0.3, linestyle='--', linewidth=0.5)

# Remove the outer circular border/spine for a cleaner look
ax.spines['polar'].set_visible(False)

ax.set_title(
    'News Topic Distribution Wheel',
    fontsize=24,
    fontweight='bold',
    pad=30,
    color='#1F2937'
)

# Add value labels on each segment
for angle, count, bar in zip(angles, values, bars):
    if count > 0:
        height = bar.get_height()
        ax.text(
            angle,
            height + max(values) * 0.06,
            str(count),
            ha='center',
            va='bottom',
            fontsize=11,
            fontweight='bold',
            color='#374151'
        )

# Add a subtitle with context
total_tags = sum(values)
fig.text(
    0.5, 0.92,
    f'Analysis of {len(articles)} recent articles • {total_tags} total topic tags',
    ha='center',
    fontsize=11,
    color='#6B7280'
)

plt.tight_layout()
plt.savefig('topic_distribution_wheel.png', dpi=300, bbox_inches='tight', facecolor='white')

print("\n" + "="*60)
print("Circular news wheel created successfully!")
print("="*60)
print("\nFile created: topic_distribution_wheel.png")
print("\nVisualization features:")
print("  - Segment size = number of articles per topic")
print("  - Colors help distinguish between different topics")
print("  - Clockwise arrangement starting from top")
