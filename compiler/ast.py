# text-based syntax tree
def print_tree(node, indent=0):
    # create indent, more indent means deeper into tree
    prefix = "  " * indent
    ntype = node['type']

    if ntype == 'assignment':
        print(prefix + "assignment")
        for child in node['children']:
            print_tree(child, indent + 1)   # recursively process children
    elif ntype == 'id':
        print(prefix + f"id: {node['value']}")
    elif ntype == 'num':
        print(prefix + f"num: {node['value']}")
    elif ntype == 'op':
        print(prefix + f"op ({node['op']})")
        print_tree(node['left'], indent + 1)    # left operand
        print_tree(node['right'], indent + 1)   # right operand