import sys
sys.path.append('./utils')
from utils.node import Node
from utils.create_binary_tree import create_binary_tree

def tree_min_dfs(root: Node):
    if root is None:
        return None
    stack = [root]
    current_min = float('inf')

    while len(stack) > 0:
        current_node = stack.pop()
        current_min = min(current_min, current_node.item)

        if current_node.right:
            stack.append(current_node.right)
        if current_node.left:
            stack.append(current_node.left)

    return current_min

if __name__ == '__main__':
    my_test = tree_min_dfs(create_binary_tree())
    print(my_test)