import sys
sys.path.append('./utils')
from utils.node import Node
from utils.create_binary_tree import create_basic_binary_tree

def dfs_iterative(root: Node, target):
    if root is None:
        return False

    stack = [root]
    while len(stack) > 0:
        current_element = stack.pop()
        if current_element.item == target:
            return True

        if current_element.right:
            stack.append(current_element.right)
        if current_element.left:
            stack.append(current_element.left)
    return False

if __name__ == '__main__':
    binary_tree = create_basic_binary_tree()
    print(dfs_iterative(binary_tree, 'd'))
    print(dfs_iterative(binary_tree, 'z'))
