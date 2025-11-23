class Node:
    def __init__(self, item, children=None):
        if children is None:
            children = []
        self.item = item
        self.children = children