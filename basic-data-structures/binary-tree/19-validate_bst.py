import sys
sys.path.append('./utils')
from utils.node import Node
from utils.create_binary_tree import create_binary_search_tree, create_binary_tree

def is_valid_bst(tree: Node) -> bool:
    def in_order_dfs(root: Node, result=None):
        if result is None:
            result = list()
        if root is not None:
            in_order_dfs(root.left, result)
            result.append(root.item)
            in_order_dfs(root.right, result)
        return result
    in_order_tree = in_order_dfs(tree)
    return True if in_order_tree == sorted(in_order_tree) else False

def is_valid_bts_second(tree: Node) -> bool:
    def dfs(root: Node, min_value, max_value):
        if not root:
            return True
        if not (min_value < root.item < max_value):
            return False
        return dfs(root.left, min_value, root.item) and dfs(root.right, root.item, max_value)
    return dfs(tree, float('-inf'), float('inf'))


if __name__ == '__main__':
    binary_search_tree = create_binary_search_tree()
    binary_tree = create_binary_tree()

    print(is_valid_bst(binary_search_tree))
    print(is_valid_bst(binary_tree))