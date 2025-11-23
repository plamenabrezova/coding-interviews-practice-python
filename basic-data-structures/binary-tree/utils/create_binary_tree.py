from node import Node

def create_binary_tree() -> Node:
    a = Node(3)
    b = Node(11)
    c = Node(4)
    d = Node(4)
    e = Node(2)
    f = Node(1)

    a.left = b          #     a             #     3
    a.right = c         #    / \            #    / \
    b.left = d          #   b   c           #   11   4
    b.right = e         #  / \   \          #  / \   \
    c.right = f         # d   e   f         # 4   2   1

    return a

def create_basic_binary_tree() -> Node:
    a = Node('a')
    b = Node('b')
    c = Node('c')
    d = Node('d')
    e = Node('e')
    f = Node('f')

    a.left = b          #     a
    a.right = c         #    / \
    b.left = d          #   b   c
    b.right = e         #  / \   \
    c.right = f         # d   e   f

    return a

def create_binary_search_tree() -> Node:
    a = Node(7)
    b = Node(2)
    c = Node(5)
    d = Node(3)
    e = Node(6)
    f = Node(11)
    g = Node(9)
    h = Node(10)
    i = Node(14)
    j = Node(13)

    a.left = b          #       7
    a.right = f         #    /     \
    b.right = c         #   2       11
    c.left = d          #    \     /  \
    c.right = e         #     5   9    14
    f.left = g          #    / \   \   /
    f.right = i         #   3   6  10 13
    g.right = h
    i.left = j

    return a