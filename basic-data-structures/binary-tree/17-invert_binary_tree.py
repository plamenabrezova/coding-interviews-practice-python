import sys
sys.path.append('./utils')
from utils.node import Node
from utils.create_binary_tree import create_binary_tree

def invert_tree(root: Node):
    if root is None:
        return None
    left = invert_tree(root.left)
    right = invert_tree(root.right)
    left, right = right, left
    return Node(root.item, left, right)

def invert_tree_short_version(root: Node):
    if root is None:
        return None
    return Node(root.item, invert_tree(root.right), invert_tree(root.left))

if __name__ == '__main__':
    binary_tree_root = create_binary_tree()
    print(invert_tree(binary_tree_root))
    print(invert_tree_short_version(binary_tree_root))