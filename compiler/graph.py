from graphviz import Digraph

def build_graph(node, graph=None, parent=None):
    if graph is None:
        graph = Digraph()

    node_id = str(id(node))
    label = node['type']
    if node['type'] == 'id' or node['type'] == 'num':
        label += f": {node['value']}"
    elif node['type'] == 'binop':
        label += f" ({node['op']})"

    graph.node(node_id, label)

    if parent:
        graph.edge(parent, node_id)

    # children
    if node['type'] == 'stmt':
        for child in node['children']:
            build_graph(child, graph, node_id)
    elif node['type'] == 'binop':
        build_graph(node['left'], graph, node_id)
        build_graph(node['right'], graph, node_id)

    return graph