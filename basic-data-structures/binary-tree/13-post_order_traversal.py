# post-order traversal
# left -> right -> root
import sys
sys.path.append('./utils')
from utils.node import Node
from utils.create_binary_tree import create_binary_tree

def post_order(root: Node, result=None):
    if result is None:
        result = list()
    if root is not None:
        post_order(root.left, result)
        post_order(root.right, result)
        result.append(root.item)
    return result


if __name__ == '__main__':
    tree_root_node =create_binary_tree()
    print(post_order(tree_root_node))
