import sys
sys.path.append('./utils')
from utils.node import Node
from utils.create_binary_tree import create_binary_tree

def serialize(root: Node) -> str:
    if root is None:
        return 'x'
    return '{} {} {}'.format(root.item, serialize(root.left), serialize(root.right))

def deserialize(tree_string: str) -> Node:
    def dfs(nodes):
        value = next(nodes)
        if value == 'x': return
        current_node = Node(int(value))
        current_node.left = dfs(nodes)
        current_node.right = dfs(nodes)
        return current_node
    return dfs(iter(tree_string.split()))

if __name__ == '__main__':
    my_var = 'hello'
    print(my_var[1:2])
    print(my_var)
    my_var = my_var[1:]
    print(my_var)
    binary_tree_root = create_binary_tree()
    print(serialize(binary_tree_root))
    print(serialize(binary_tree_root).split(' '))
    serialized_tree = serialize(binary_tree_root)

    print(deserialize(serialized_tree))