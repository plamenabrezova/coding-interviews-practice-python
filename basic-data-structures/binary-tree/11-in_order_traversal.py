# in-order traversal
# left -> root -> right
import sys
sys.path.append('./utils')
from utils.node import Node
from utils.create_binary_tree import create_binary_tree

def in_order(root: Node, result=None):
    if result is None:
        result = list()
    if root is not None:
        in_order(root.left, result)
        result.append(root.item)
        in_order(root.right, result)
    return result

if __name__ == '__main__':
    tree_root_node = create_binary_tree()
    print(in_order(tree_root_node))