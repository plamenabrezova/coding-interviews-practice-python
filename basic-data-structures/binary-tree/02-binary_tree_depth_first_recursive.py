# Binary tree:
# at most 2 children per node
# exactly one root
# exactly 1 path between root and any node (no cycles)
# empty trees can also be considered binary trees

# In depth first approach we will use data structure as a stack
# Time complexity: O(n)
# Space complexity: O(n)

import sys
sys.path.append('./utils')
from utils.node import Node
from utils.create_binary_tree import create_basic_binary_tree

def depth_first_recursive(root: Node) -> list:
    # what is the base case - empty tree
    if root is None:
        return []

    left_values = depth_first_recursive(root.left)
    right_values = depth_first_recursive(root.right)

    return [root.item, *left_values, *right_values]

if __name__ == '__main__':
    print(depth_first_recursive(create_basic_binary_tree()))
    # should be - a b d e c f
