class Node:
    def __init__(self, item, left=None, right=None):
        self.item = item
        self.left = left
        self.right = right

    def __str__(self):
        return 'item: {}, left child: {}, right child: {}'.format(self.item, self.left, self.right)