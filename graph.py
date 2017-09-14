import networkx as nx
import matplotlib.pyplot as plt

g = nx.DiGraph()
#g.add_nodes_from([1,2,3,4,5])
g.add_edges_from([(1,2),(2,5)], weight=2)
g.add_edge(1,2)
g.add_edge(4,2)
g.add_edge(3,5)
g.add_edge(2,3)
g.add_edge(5,4)


nx.draw(g,with_labels=True)
plt.draw()
plt.show()