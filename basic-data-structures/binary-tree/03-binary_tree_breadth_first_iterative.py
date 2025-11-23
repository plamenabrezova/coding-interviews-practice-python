# Binary tree:
# at most 2 children per node
# exactly one root
# exactly 1 path between root and any node (no cycles)
# empty trees can also be considered binary trees

# In bread first approach we will use queue
# Time complexity: O(n)
# Space complexity: O(n)
import sys
sys.path.append('./utils')
from utils.node import Node
from utils.create_binary_tree import create_basic_binary_tree

def bread_first_iterative(root: Node) -> list:
    if root is None:
        return []
    queue = [root]
    result = []

    # while my queue is not empty
    while len(queue) > 0:
        # will get my current element by removing it from the front of my queue
        current_element = queue.pop(0)
        # will append it to the result list
        result.append(current_element.item)

        # will check my current element's children and if they are present, will add them to the queue
        if current_element.left:
            queue.append(current_element.left)
        if current_element.right:
            queue.append(current_element.right)
    return result

if __name__ == '__main__':
    print(bread_first_iterative(create_basic_binary_tree()))
    # should be - a b c d e f
