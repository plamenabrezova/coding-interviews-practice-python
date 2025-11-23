# Find the middle node of a linked list.

# Input: 0 1 2 3 4
# Output: 2

# If the number of nodes is even, then return the second middle node.
# Input: 0 1 2 3 4 5
# Output: 3

class Node:
    def __init__(self, val, next_node=None):
        self.val = val
        self.next = next_node

def middle_of_linked_list(head: Node) -> int:
    mid, end = 0, 0
    while head.next:
        mid = (end + mid) // 2
        end += 1
        head.next = head.next.next

    return mid

    # slow = fast = head
    # while fast and fast.next:
    #     fast = fast.next.next
    #     slow = slow.next
    # return slow.val


def build_list(nodes, f):
    val = next(nodes, None)
    if val is None: return None
    nxt = build_list(nodes, f)
    return Node(f(val), nxt)


if __name__ == '__main__':
    test_head = build_list(iter(input().split()), int)
    res = middle_of_linked_list(test_head)
    print(res)
