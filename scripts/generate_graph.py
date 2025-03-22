import json
from pyvis.network import Network

# Load the metadata JSON from Obsidian
with open("graphs/metadata.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Create a network graph
net = Network(notebook=False, directed=True)

# Add nodes and edges based on links in Obsidian
for page, metadata in data.items():
    net.add_node(page, label=page)
    for link in metadata.get("links", []):
        net.add_edge(page, link)

# Generate an interactive HTML graph
net.show("docs/graph.html")  # GitHub Pages will serve from docs/
