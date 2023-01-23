import networkx as nx

G = nx.Graph()

nx.add_path(G, [1, 2, 3])
nx.add_path(G, [4, 2, 5])

print('Nodes:', G.nodes)
print('Edges:', G.edges)


from algorithmx import jupyter_canvas

canvas = jupyter_canvas()

canvas.nodes(G.nodes).add()
canvas.edges(G.edges).add()

print(canvas)