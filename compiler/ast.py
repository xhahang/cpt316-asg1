def print_tree(node, indent=0):
    prefix = "  " * indent
    ntype = node['type']
    if ntype == 'stmt':
        print(prefix + "stmt")
        for child in node['children']:
            print_tree(child, indent + 1)
    elif ntype == 'id':
        print(prefix + f"id: {node['value']}")
    elif ntype == 'num':
        print(prefix + f"num: {node['value']}")
    elif ntype == 'binop':
        print(prefix + f"binop ({node['op']})")
        print_tree(node['left'], indent + 1)
        print_tree(node['right'], indent + 1)