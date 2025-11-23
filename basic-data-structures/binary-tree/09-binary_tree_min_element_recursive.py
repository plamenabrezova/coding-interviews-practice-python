import sys
sys.path.append('./utils')
from utils.node import Node
from utils.create_binary_tree import create_binary_tree

def tree_min_element_rec(root: Node):
    if root is None:
        return float('inf')
    return min(root.item, tree_min_element_rec(root.left), tree_min_element_rec(root.right))

if __name__ == '__main__':
    result = tree_min_element_rec(create_binary_tree())
    print(result)