import sys
sys.path.append('./utils')
from utils.node import Node
from utils.create_binary_tree import create_binary_tree

def is_balanced(root: Node):
    def dfs(dfs_root: Node):
        if dfs_root is None:
            return 0
        left = dfs(dfs_root.left)
        right = dfs(dfs_root.right)
        if left == -1 or right == -1 or abs(left - right) > 1:
            return -1
        else:
            return max(left, right) + 1

    return True if (dfs(root) !=
                    -1) else False



if __name__ == '__main__':
    binary_tree_root = create_binary_tree()
    print(is_balanced(binary_tree_root))