from node import Node

def build_tree(nodes, f):
    item = next(nodes)
    num = int(next(nodes))
    children = [build_tree(nodes, f) for _ in range(num)]
    return Node(f(item), children)