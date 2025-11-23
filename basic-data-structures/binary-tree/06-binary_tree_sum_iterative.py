import sys
sys.path.append('./utils')
from utils.node import Node
from utils.create_binary_tree import create_binary_tree

def binary_tree_sum(root: Node) -> int:
    if root is None:
        return 0

    stack = [root]
    tree_sum = 0

    while len(stack) > 0:
        current_element = stack.pop()
        tree_sum += current_element.item

        if current_element.right:
            stack.append(current_element.right)
        if current_element.left:
            stack.append(current_element.left)

    return tree_sum


if __name__ == '__main__':
    result = binary_tree_sum(create_binary_tree())
    print(result)

