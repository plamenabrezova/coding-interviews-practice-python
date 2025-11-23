from collections import deque

def rotate_left_till_zero(nums):
    # initialize a new deque out of nums
    queue = deque(nums)
    # continue the loop till front of queue is 0
    while queue[0] != 0:
        # remove the front of the queue and add it to the end
        queue.append(queue.popleft())

    return queue


if __name__ == '__main__':
    result = rotate_left_till_zero([1, 3, 5, 5, 0])
    print(' '.join(map(str, result)))
