import sys
sys.path.append('./utils')
from utils.node import Node
from utils.create_binary_tree import create_binary_search_tree, create_binary_tree

def insert(tree: Node, item: int):
    if tree is None:
        return Node(item)

    if tree.item > item:
        tree.left = insert(tree.left, item)
    elif tree.item < item:
        tree.right = insert(tree.right, item)

    return tree


if __name__ == '__main__':
    binary_search_tree = create_binary_search_tree()
    print(insert(binary_search_tree, 8))
