# max depth of a binary tree is the longest root-to-leaf path
import sys
sys.path.append('./utils')
from utils.node import Node
from utils.create_binary_tree import create_binary_tree

def max_depth(root: Node):
    def dfs(dfs_root: Node):
        if dfs_root is None:
            return 0
        return max(dfs(dfs_root.left), dfs(dfs_root.right)) + 1
    return dfs(root) - 1 if root else 0



if __name__ == '__main__':
    binary_tree_root = create_binary_tree()
    print(max_depth(binary_tree_root))