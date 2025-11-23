from utils import *

class MaxHeap:
    def __init__(self, items=None):
        if items is None:
            items = list()
        self.items = items

    def has_left_child(self, idx) -> bool:
        return get_left_child_index(idx) < len(self.items)

    def has_right_child(self, idx) -> bool:
        return get_right_child_index(idx) < len(self.items)

    def left_child(self, idx):
        return self.items[get_left_child_index(idx)]

    def right_child(self, idx):
        return self.items[get_right_child_index(idx)]

    def parent(self, idx):
        return self.items[get_parent_index(idx)]

    # get the maximum item
    def peek(self):
        if len(self.items) == 0:
            raise Exception('Cannot retrieve peek from an empty heap.')
        return self.items[0]

    # remove from the top
    def poll(self):
        if len(self.items) == 0:
            raise Exception('Cannot remove from an empty heap.')

        item = self.items[0]
        self.items[0] = self.items[-1]
        self.items.pop()
        self.heapify_down()
        return item

    def add(self, item):
        self.items.append(item)
        self.heapify_up()

    def swap(self, left_idx, right_idx):
        (self.items[left_idx], self.items[right_idx]) = (self.items[right_idx], self.items[left_idx])

    def heapify_down(self):
        idx = 0
        while self.has_left_child(idx):
            bigger_child_idx = get_left_child_index(idx)
            if get_right_child_index(idx) and get_left_child_index(idx) > bigger_child_idx:
                bigger_child_idx = get_right_child_index(idx)

            if self.items[idx] > self.items[bigger_child_idx]:
                break
            else:
                self.swap(idx, bigger_child_idx)

            idx = bigger_child_idx

    def heapify_up(self):
        idx = len(self.items) - 1
        while has_parent(idx) and self.parent(idx) < self.items[idx]:
            self.swap(idx, get_parent_index(idx))
            idx = get_parent_index(idx)


if __name__ == '__main__':
    max_heap = MaxHeap([44, 42, 35, 33, 31, 19, 27, 10, 26])
    print(max_heap.items)
    max_heap.poll()
    print(max_heap.items)
    max_heap.add(38)
    print(max_heap.items)
