from node import Node
from create_tree import build_tree
from typing import List

def ternary_tree_paths(root: Node) -> List[str]:
    def dfs(root: Node, path, result):
        if all(child is None for child in root.children):
            result.append('->'.join(path) + '->' + str(root.item))
            return

        for child in root.children:
            if child is not None:
                dfs(child, path + [str(root.item)], result)
    res = []
    if root:
        dfs(root, [], res)
    return res


if __name__ == '__main__':
    tree = build_tree(iter('1 3 2 1 5 0 3 0 4 0'.split()), int)
    result = ternary_tree_paths(tree)
    for line in result:
        print(line)
