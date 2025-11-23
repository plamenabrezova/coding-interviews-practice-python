# You've begun your new job to organize newspapers.
# Each morning, you are to separate the newspapers into smaller piles and assign each pile to a co-worker.
# This way, your co-workers can read through the newspapers and examine its contents simultaneously.

# Each newspaper is marked with a read time to finish all its contents.
# A worker can read one newspaper at a time, and when they finish, they can start reading the next newspaper.
# Your goal is to minimize the amount of time needed for your co-workers to finish all newspapers.
# Additionally, the newspapers came in a particular order,
# and you must not disarrange the original ordering when distributing the newspapers.
# In other words, you cannot pick and choose newspapers randomly from the whole pile to assign to a co-worker,
# but rather you must take a subsection of consecutive newspapers from the whole pile.

# What is the minimum amount of time it would take to have your coworkers go through all the newspapers?
# That is, if you optimize the distribution of newspapers, what is the longest read time among all piles?

# Example 1:
# Input: newspapers_read_times = [7,2,5,10,8], num_coworkers = 2
# Output: 18
# Explanation: Assign first 3 newspapers to one coworker then assign the rest to another.
# The time it takes for the first 3 newspapers is 7 + 2 + 5 = 14 and for the last 2 is 10 + 8 = 18.

# Example 2:
# Input: newspapers_read_times = [2,3,5,7], num_coworkers = 3
# Output: 7
# Explanation:
# Assign [2, 3], [5], and [7] separately to workers. The minimum time is 7.

# The reason binary search is applicable in this problem is because of the monotonic nature of the problem.
# What do we mean by monotonic here? If a given time t is feasible for num_coworkers to finish all the newspapers,
# then any time greater than t will also be feasible.
# This is because if coworkers can complete reading in a shorter amount of time,
# they can obviously also complete it if given more time.
# This forms a monotonic relationship, which is a crucial characteristic for binary search applicability.
#
# Essentially, our problem exhibits two sequences:
# A sequence of infeasible times, followed by
# A sequence of feasible times.
# The transition between these two sequences is what we aim to find using binary search.
#
# Observations:
# The smallest time any coworker would take is equal to the time taken to read the longest newspaper,
# i.e., max(newspapers_read_times).
# The largest time any coworker would take is if only one person reads all the newspapers,
# i.e., sum(newspapers_read_times).

# The optimal time lies between these two values.
# Feasibility Check: Intuitive Explanation
# The feasibility check is essentially a simulation of how we'd distribute newspapers to coworkers under a hypothetical
# maximum reading time, mid.
# At its core, the algorithm emulates a conveyor belt process: imagine each coworker standing ready,
# and as you pass them newspapers, a timer keeps track of the accumulated reading time.
# Once a coworker's accumulated time reaches or nearly reaches the mid-value and they don't have enough time to read
# the next newspaper, they step back, and the next coworker steps forward to continue the task.
#
# By cycling through this process, we get an effective gauge on how many coworkers would be needed to cover all
# newspapers under the stipulated time limit, mid. If the number exceeds our available coworkers,
# the time limit isn’t viable. If not, it's feasible.
#
# Let m represent sum(newspapers_read_times)
#
# Time complexity: O(n log m)
#
# Setting the initial low and high values takes O(n) to find out the maximum value and the sum of newspapers_read_times.
# Then, performing binary search is O(log m), and the helper function feasible() that is called inside
# the binary search loop is O(n). Overall, the binary search takes O(n log m),
# which is more significant than O(n), so the time complexity of our solution is O(n log m).
#
# Space Complexity: O(1)

from typing import List


def is_feasible(newspapers_read_times: List[int], num_coworkers: int, limit: int) -> bool:
    time, num_workers = 0, 0

    for i in newspapers_read_times:
        if time + i > limit:
            time = 0
            num_workers += 1
        time += i

    if time != 0:
        num_workers += 1

    return num_workers <= num_coworkers


def newspapers_split(newspapers_read_times: List[int], num_coworkers: int) -> int:
    result = -1
    low = max(newspapers_read_times)
    high = sum(newspapers_read_times)

    while low <= high:
        mid = (low + high) // 2

        if is_feasible(newspapers_read_times, num_coworkers, mid):
            result = mid
            high = mid - 1
        else:
            low = mid + 1

    return result


if __name__ == '__main__':
    # newspapers_read_times = [int(x) for x in input().split()]
    # num_coworkers = int(input())
    # res = newspapers_split(newspapers_read_times, num_coworkers)
    # print(res)
    print(newspapers_split([7, 2, 5, 10, 8], 2))

    print(newspapers_split([3, 6, 7, 11], 8))