import sys
sys.path.append('./utils')
from utils.node import Node
from utils.create_binary_tree import create_binary_search_tree

def find(root: Node, target: int) -> bool:
    if root is None:
        return False
    if root.item == target:
        return True
    elif root.item < target:
        return find(root.right, target)
    else:
        return find(root.left, target)

def insert(root: Node, item: int):
    if root is None:
        return Node(item)
    if root.item < item:
        root.right = insert(root.right, item)
    elif root.item > item:
        root.left = insert(root.left, item)

if __name__ == '__main__':
    binary_tree_root = create_binary_search_tree()
    print(find(binary_tree_root, 9))