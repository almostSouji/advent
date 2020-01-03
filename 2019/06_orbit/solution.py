import networkx as nx

with open("input.txt", "r") as file:
	input = file.read().splitlines()
	edges = map(lambda x : tuple(x.split(")")), input)
G = nx.DiGraph()
G.add_edges_from(edges)

print("Part 1: Orbit Count Checksum: {}".format(sum([nx.shortest_path_length(G, "COM", n) for n in G])))

U = nx.Graph(G)
for you_orbit in U.neighbors("YOU"):
	for san_orbit in U.neighbors("SAN"):
		print("Part 2: Orbital transfers required: {}".format(nx.shortest_path_length(U, you_orbit, san_orbit)))

nx.write_graphml(G, "orbitmap.graphml");