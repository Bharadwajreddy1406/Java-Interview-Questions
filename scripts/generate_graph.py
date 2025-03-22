import json
import os

# Load Obsidian's exported metadata.json
with open("graphs/metadata.json", "r", encoding="utf-8") as file:
    data = json.load(file)

nodes = [{"id": note} for note in data["nodes"]]
edges = [{"source": link["source"], "target": link["target"]} for link in data["edges"]]

# HTML Template for D3.js Graph
html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Obsidian Graph</title>
    <script src="https://d3js.org/d3.v7.min.js"></script>
    <style>
        body {{ margin: 0; overflow: hidden; }}
        svg {{ width: 100vw; height: 100vh; }}
    </style>
</head>
<body>
    <svg></svg>
    <script>
        const nodes = {json.dumps(nodes)};
        const links = {json.dumps(edges)};

        const svg = d3.select("svg"),
              width = window.innerWidth,
              height = window.innerHeight;

        const simulation = d3.forceSimulation(nodes)
            .force("link", d3.forceLink(links).id(d => d.id))
            .force("charge", d3.forceManyBody().strength(-500))
            .force("center", d3.forceCenter(width / 2, height / 2));

        const link = svg.append("g")
            .selectAll("line")
            .data(links)
            .enter().append("line")
            .attr("stroke", "#999")
            .attr("stroke-opacity", 0.6);

        const node = svg.append("g")
            .selectAll("circle")
            .data(nodes)
            .enter().append("circle")
            .attr("r", 5)
            .attr("fill", "steelblue")
            .call(d3.drag()
                .on("start", dragStarted)
                .on("drag", dragged)
                .on("end", dragEnded));

        node.append("title").text(d => d.id);

        simulation.on("tick", () => {{
            link.attr("x1", d => d.source.x)
                .attr("y1", d => d.source.y)
                .attr("x2", d => d.target.x)
                .attr("y2", d => d.target.y);

            node.attr("cx", d => d.x).attr("cy", d => d.y);
        }});

        function dragStarted(event, d) {{
            if (!event.active) simulation.alphaTarget(0.3).restart();
            d.fx = d.x;
            d.fy = d.y;
        }}

        function dragged(event, d) {{
            d.fx = event.x;
            d.fy = event.y;
        }}

        function dragEnded(event, d) {{
            if (!event.active) simulation.alphaTarget(0);
            d.fx = null;
            d.fy = null;
        }}
    </script>
</body>
</html>
"""

# Save the generated graph
os.makedirs("graphs", exist_ok=True)
with open("graphs/index.html", "w", encoding="utf-8") as file:
    file.write(html_content)

print("✅ Graph generated: graphs/index.html")
