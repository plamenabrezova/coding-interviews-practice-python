from utils import *

class MinHeap:
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

    # add element to the end of the heap
    def add(self, item):
        self.items.append(item)
        self.heapify_up()

    def swap(self, left_idx, right_idx):
        (self.items[left_idx], self.items[right_idx]) = (self.items[right_idx], self.items[left_idx])

    def heapify_up(self):
        idx = len(self.items) - 1
        # the heap is out of order:
        # current index has a parent
        # and parent element is bigger than element at current index
        while has_parent(idx) and self.parent(idx) > self.items[idx]:
            self.swap(get_parent_index(idx), idx)
            idx = get_parent_index(idx)

    def heapify_down(self):
        idx = 0
        # if there's no left child there is no right child as well
        while self.has_left_child(idx):
            smaller_child_index = get_left_child_index(idx)
            if self.has_right_child(idx) and self.right_child(idx) < self.left_child(idx):
                smaller_child_index = self.right_child(idx)

            if self.items[idx] < self.items[smaller_child_index]:
                break
            else:
                self.swap(idx, smaller_child_index)

            idx = smaller_child_index


if __name__ == '__main__':
    my_heap = MinHeap([10, 15, 20, 17, 25])
    print(my_heap.items)
    my_heap.add(18)
    print(my_heap.items)
    my_heap.poll()
    print(my_heap.items)