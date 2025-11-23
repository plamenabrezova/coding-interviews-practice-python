# - SnapshotArray(int length) initializes an array-like data structure with the given length.
#   Initially, each element equals 0.
# - void set(index, val) sets the element at the given index to be equal to val
# - int snap() takes a snapshot of the array and returns the snap_id: the total number of times we called snap() minus 1
# - int get(index,snap_id) returns the value at the given index, at the time we took the snapshot with the given snap_id

# Example 1:
# Input: ["SnapshotArray","set","snap","set","get"]
# [[3],[0,5],[],[0,6],[0,0]]
# Output: [null,null,0,null,5]
# Explanation:
# SnapshotArray snapshotArr = new SnapshotArray(3); // set the length to be 3
# snapshotArr.set(0,5);  // Set array[0] = 5
# snapshotArr.snap();  // Take a snapshot, return snap_id = 0
# snapshotArr.set(0,6);
# snapshotArr.get(0,0);  // Get the value of array[0] with snap_id = 0, return 5

# Instead of copying the entire array each time we take a snapshot, we wish to only store the changes to each index.
# We keep track of an array histories of size n where histories[i] is an array that stores
# the history of the changes of array[i]'s values.
# We use the pair (snap_id, value) to indicate that we have updated array[i]=value at the time we took the snapshot
# with the given snap_id.
# So when implementing get(snap_id) for index i, we will do binary search on histories[i] to find the index pos in
# histories[i] that contains the most recent value up to the time we took the snapshot with the given snap_id.

# We wish to find the pos for the most recent value at the time we took the snapshot with the given snap_id,
# we are trying to find the rightmost index in history=histories[i] such that the snap_id at history[pos]
# is less or equal to the target snap_id (a[i][0] <= snap_id).

# This means that the feasible function is a[i][0] <= snap_id, whenever this is true, we must check the positions
# on its right to find the rightmost position that makes this condition hold.

# https://leetcode.com/problems/snapshot-array/

class SnapshotArray:

    def __init__(self, length: int):
        self.histories = [ [[-1, 0]] for _ in range(length) ]
        self.snap_id = 0

    def set(self, index: int, val: int) -> None:
        self.histories[index].append([self.snap_id, val])

    def snap(self) -> int:
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index: int, snap_id: int) -> int:
        left, right, result = 0, len(self.histories[index]) - 1, -1
        while left <= right:
            mid = (left + right) // 2

            if self.histories[index][mid][0] < snap_id:
                left = mid + 1
                result = mid
            else:
                right = mid - 1

        return self.histories[index][result][1]


if __name__ == '__main__':
    hello = SnapshotArray(4)
    # histories[i] is an array that stores the history of the changes of array[i]'s values
    print(hello.histories[0])
    hello.set(0, 5)
    print(hello.histories[0])
    hello.set(0, 4)
    hello.snap()
    hello.set(0, 9)

    print(hello.histories[0])
    # holds the value for the history of the 0th element when the snap id was 0
    print(hello.histories[0][0])
    # holds the value for the history of the 0th element when the snap id was 1
    print(hello.histories[0][1])
    # holds the value for the history of the 0th element when the snap id was 2
    print(hello.histories[0][2])
    print(hello.get(0, 1))

    print('------------')

    leet_code_test = SnapshotArray(1)
    leet_code_test.set(0, 4)
    print(leet_code_test.histories[0])
    leet_code_test.set(0, 16)
    print(leet_code_test.histories[0])
    leet_code_test.set(0, 13)
    print(leet_code_test.histories[0])

    leet_code_test.snap()

    print(leet_code_test.histories[0])
    # leet_code_test.get(0, 0)
    print(leet_code_test.get(0,0))
    print(leet_code_test.histories[0])
    leet_code_test.snap()


