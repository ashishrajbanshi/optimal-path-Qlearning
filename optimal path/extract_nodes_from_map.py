import osmnx as ox

city = ox.geocode_to_gdf('Kathmandu, Bagmati, Nepal')

# Defining the map boundaries

north, east, south, west = 27.7071, 85.3230, 27.6982, 85.3133
# Downloading the map as a graph object
G = ox.graph_from_bbox(north, south, east, west, network_type='drive')
# Plotting the map graph
ox.plot_graph(G)

with open("nodes_map.txt", "w") as text_file:
    for i in G.nodes:
        text_file.write("%s\n" % i)

with open("edges_map.txt", "w") as text_file:
    for i in G.edges:
        text_file.write("%s %s\n" % (i[0], i[1]))

print("The nodes and edges are extracted into nodes_map.txt and edges_map.txt respectively.")
