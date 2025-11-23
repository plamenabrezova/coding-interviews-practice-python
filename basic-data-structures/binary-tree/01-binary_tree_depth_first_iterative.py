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

def depth_first(root: Node) -> list:
    if root is None:
        return []

    stack = [root]
    result = []
    while len(stack) > 0:
        current_element = stack.pop()
        result.append(current_element.item)

        if current_element.right:
            stack.append(current_element.right)
        if current_element.left:
            stack.append(current_element.left)
    return result

if __name__ == '__main__':
    print(depth_first(create_basic_binary_tree()))
    # should be - a b d e c f
