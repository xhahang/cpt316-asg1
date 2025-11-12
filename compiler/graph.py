from graphviz import Digraph

#   visual diagram of syntax tree
def build_graph(node, graph=None, parent=None):
    if graph is None:
        graph = Digraph()
    node_id = str(id(node))
    # set label for node
    label = node['type']
    if node['type'] == 'id' or node['type'] == 'num':
        label += f": {node['value']}"
    elif node['type'] == 'op':
        label += f" ({node['op']})"

    # add node with label to graph
    graph.node(node_id, label)

    # create edge from parent to node if parent exists
    if parent:
        graph.edge(parent, node_id)

    # children nodes
    if node['type'] == 'assignment':
        for child in node['children']:
            build_graph(child, graph, node_id)
    elif node['type'] == 'op':
        build_graph(node['left'], graph, node_id)
        build_graph(node['right'], graph, node_id)

    return graph