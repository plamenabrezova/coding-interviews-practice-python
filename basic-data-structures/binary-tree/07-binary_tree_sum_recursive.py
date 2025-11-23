import sys
sys.path.append('./utils')
from utils.node import Node
from utils.create_binary_tree import create_binary_tree

def binary_tree_sum_recursive(root: Node) -> int:
    if root is None:
        return 0
    left_sum = binary_tree_sum_recursive(root.left)
    right_sum = binary_tree_sum_recursive(root.right)
    return root.item + left_sum + right_sum

if __name__ == '__main__':
    result = binary_tree_sum_recursive(create_binary_tree())
    print(result)
