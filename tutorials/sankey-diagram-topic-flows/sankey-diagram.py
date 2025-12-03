import requests
import plotly.graph_objects as go
from collections import defaultdict, Counter
import json
import os

# Note: To save static images (PNG/SVG), you need kaleido installed:
# pip install kaleido

# Set your API key here (or leave empty to use sample data)
API_KEY = ""  # Replace with your NewsDataHub API key, or leave empty

# Check if API key is provided
if API_KEY and API_KEY != "your_api_key_here":
    print("Using live API data...")
    # language=en would ensure we are getting articles in English
    url = "https://api.newsdatahub.com/v1/news?language=en"
    headers = {"x-api-key": API_KEY}
    params = {"per_page": 100}

    # Fetch articles
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
# Extract Source-Topic Relationships
# ============================================================================
flows = defaultdict(int)

for article in articles:
    # Get source name from article level
    source_name = article.get("source_title")

    # Get topics - NewsDataHub returns topics as array
    article_topics = article.get("topics", [])

    # Count each source-topic combination
    if source_name and article_topics:
        if isinstance(article_topics, list):
            for topic in article_topics:
                if topic and topic != "general":  # Exclude uncategorized
                    flows[(source_name, topic)] += 1
        else:
            if article_topics != "general":
                flows[(source_name, article_topics)] += 1

# Convert to list of dictionaries
flow_data = [
    {"source": src, "target": tgt, "value": val}
    for (src, tgt), val in flows.items()
]

print(f"\nFound {len(flow_data)} unique source-topic combinations")

# Preview some flows
print("\nSample flows:")
for item in sorted(flow_data, key=lambda x: x["value"], reverse=True)[:5]:
    print(f"  {item['source']} → {item['target']}: {item['value']} articles")

# ============================================================================
# Filter to Top Sources for Clarity
# ============================================================================
# Count total articles per source
source_counts = Counter()
for item in flow_data:
    source_counts[item["source"]] += item["value"]

# Get top 10 sources by article count
top_sources = [source for source, _ in source_counts.most_common(10)]
print(f"\nTop 10 sources by article count:")
for i, source in enumerate(top_sources, 1):
    print(f"  {i}. {source}: {source_counts[source]} articles")

# Keep only flows from top sources
flow_data = [
    item for item in flow_data
    if item["source"] in top_sources
]
print(f"\nFiltered to {len(flow_data)} flows from top 10 sources")

# ============================================================================
# Prepare Data for Plotly Sankey
# ============================================================================
# Create lists of unique sources and topics
sources_list = sorted(set(item["source"] for item in flow_data))
topics_list = sorted(set(item["target"] for item in flow_data))

print(f"\nVisualization summary:")
print(f"  Sources: {len(sources_list)}")
print(f"  Topics: {len(topics_list)}")

# Create combined node list (sources first, then topics)
all_nodes = sources_list + topics_list

# Create mapping from names to indices
node_dict = {node: idx for idx, node in enumerate(all_nodes)}

print(f"  Total nodes: {len(all_nodes)}")

# Prepare three parallel lists for Plotly
source_indices = [node_dict[item["source"]] for item in flow_data]
target_indices = [node_dict[item["target"]] for item in flow_data]
values = [item["value"] for item in flow_data]

print(f"  Total flows: {len(values)}")

# ============================================================================
# Create Interactive Sankey Diagram
# ============================================================================
# Bright, vivid color palette for sources
source_colors = [
    '#FF1744',  # Bright Red
    '#2979FF',  # Bright Blue
    '#00E676',  # Bright Green
    '#FF9100',  # Bright Orange
    '#D500F9',  # Bright Purple
    '#FF4081',  # Bright Pink
    '#00E5FF',  # Bright Cyan
    '#FFEA00',  # Bright Yellow
    '#651FFF',  # Bright Indigo
    '#FF6E40',  # Bright Deep Orange
]

# Bright, saturated color palette for topics
topic_colors = [
    '#FF5252',  # Bright Light Red
    '#448AFF',  # Bright Light Blue
    '#69F0AE',  # Bright Light Green
    '#FFD740',  # Bright Light Yellow
    '#E040FB',  # Bright Light Purple
    '#FF80AB',  # Bright Light Pink
    '#18FFFF',  # Bright Light Cyan
    '#FFAB40',  # Bright Light Orange
]

# Assign colors: sources get vibrant colors, topics get pastel colors
node_colors = []
for node in all_nodes:
    if node in sources_list:
        idx = sources_list.index(node)
        node_colors.append(source_colors[idx % len(source_colors)])
    else:
        # Topic node - use topic colors
        idx = topics_list.index(node)
        node_colors.append(topic_colors[idx % len(topic_colors)])

# Create custom hover labels
customdata = [
    f"{all_nodes[src]} → {all_nodes[tgt]}: {val} articles"
    for src, tgt, val in zip(source_indices, target_indices, values)
]

# Create colored flows that inherit from source colors
link_colors = []
for src_idx in source_indices:
    source_color = node_colors[src_idx]
    # Convert hex to rgba with 50% opacity
    if source_color.startswith('#'):
        r = int(source_color[1:3], 16)
        g = int(source_color[3:5], 16)
        b = int(source_color[5:7], 16)
        link_colors.append(f'rgba({r}, {g}, {b}, 0.5)')
    else:
        link_colors.append('rgba(200, 200, 200, 0.5)')

# Create Sankey diagram
fig = go.Figure(data=[go.Sankey(
    node=dict(
        pad=15,               # Vertical space between nodes
        thickness=20,         # Node width in pixels
        line=dict(
            color="black",    # Node border color
            width=0.5         # Node border width
        ),
        label=all_nodes,      # Node text labels
        color=node_colors     # Node fill colors
    ),
    link=dict(
        source=source_indices,        # Starting node indices
        target=target_indices,        # Ending node indices
        value=values,                 # Flow magnitudes
        color=link_colors,            # Colored flows matching sources
        customdata=customdata,
        hovertemplate='%{customdata}<extra></extra>'
    )
)])

# Add professional styling
fig.update_layout(
    title={
        'text': "News Sources to Topic Coverage Flow Analysis",
        'font': {'size': 20, 'family': 'Arial, sans-serif', 'color': '#2C3E50'},
        'x': 0.5,  # Center title
        'xanchor': 'center'
    },
    font=dict(size=16, family='Arial Black, sans-serif'),
    plot_bgcolor='white',
    paper_bgcolor='white',
    height=700,
    margin=dict(l=20, r=20, t=80, b=20)
)

# Save as static PNG image
output_file = 'news_source_topic_sankey.png'
fig.write_image(output_file, width=1200, height=700, scale=2)
print(f"\n✓ Sankey diagram saved to {output_file}")

print("\nVisualization complete!")
print(f"Open '{output_file}' to view the diagram")
