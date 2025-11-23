# pre-order traversal
# root -> left -> right
import sys
sys.path.append('./utils')
from utils.node import Node
from utils.create_binary_tree import create_binary_tree

def pre_order(root: Node, result=None):
    if result is None:
        result = list()
    if root is not None:
        result.append(root.item)
        pre_order(root.left,result)
        pre_order(root.right, result)
    return result

if __name__ == '__main__':
    tree_root_node = create_binary_tree()
    print(pre_order(tree_root_node))