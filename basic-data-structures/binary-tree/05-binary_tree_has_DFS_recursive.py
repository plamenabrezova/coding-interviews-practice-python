import sys
sys.path.append('./utils')
from utils.node import Node
from utils.create_binary_tree import create_basic_binary_tree

def dfs_recursive(root: Node, target):
    if root is None:
        return False
    if root.item == target:
        return True
    return dfs_recursive(root.left, target) or dfs_recursive(root.right, target)

if __name__ == '__main__':
    binary_tree = create_basic_binary_tree()
    print(dfs_recursive(binary_tree, 'd'))
    print(dfs_recursive(binary_tree, 'z'))