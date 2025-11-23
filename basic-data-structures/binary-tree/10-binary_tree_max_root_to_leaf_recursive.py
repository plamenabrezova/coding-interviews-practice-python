import sys
sys.path.append('./utils')
from utils.node import Node
from utils.create_binary_tree import create_binary_tree

def max_root_to_leaf(root: Node):
    if root is None:
        return float('-inf')

    if root.left is None and root.right is None:
        return root.item

    max_child = max(max_root_to_leaf(root.left), max_root_to_leaf(root.right))
    return root.item + max_child

if __name__ == '__main__':
    result = max_root_to_leaf(create_binary_tree())
    print(result)