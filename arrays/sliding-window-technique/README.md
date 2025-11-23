# 🪟 Sliding Window technique
**Window Sliding Technique is a computational technique that aims to reduce the use of nested loops and replace it with a single loop, thereby reducing the time complexity.**

---

### What is a Sliding Window?

Consider a long chain connected together. 

Suppose you want to apply oil in the complete chain with your hands, without pouring the oil from above.

 
One way to do so is to: 

- pick some oil, 
- apply onto a section of the chain, 
- then again pick some oil 
- then apply it to the next section where oil is not applied yet 
- and so on till the complete chain is oiled.

Another way to do so is to:

- use a cloth, dip it in oil, and then hold onto one end of the chain with this cloth. 
- then instead of re-dipping it again and again, just slide the cloth with your hand onto the next section, and next, and so on till the other end.

The second way is known as the Sliding window technique and the portion which is slid from one end to end is known as Sliding Window.

---

### Prerequisite to use the Sliding window technique

The use of the Sliding Window technique can be done in a **very specific scenario**, where the size of the window for computation is fixed throughout the complete nested loop. Only then the time complexity can be reduced. 

---

### How to use Sliding Window Technique?

The general use of the Sliding window technique can be demonstrated as follows:

1. Find the size of the window required. 
2. Compute the result for 1st window, i.e. from the start of the data structure. 
3. Then use a loop to slide the window by 1, and keep computing the result window by window.

---

### How to know where we use the Sliding Window?


To know where we use the Sliding Window then we remember the following terms which is mentioned below:

`Array, String, Sub Array, Sub String, Largest Sum, Maximum Sum, Minimum Sum`

---

### Examples

- **Given an array of integers of size ‘n’, our aim is to calculate the maximum sum of ‘k’ consecutive elements in the array.**


```
Input  : arr[] = {100, 200, 300, 400}, k = 2
Output : 700

Input  : arr[] = {1, 4, 2, 10, 23, 3, 1, 0, 20}, k = 4 
Output : 39
We get maximum sum by adding subarray {4, 2, 10, 23} of size 4.

Input  : arr[] = {2, 3}, k = 3
Output : Invalid
There is no subarray of size 3 as size of whole array is 2.
```

**Brute force approach:**

```pycon
import sys

INT_MIN = -sys.maxsize - 1

def maxSum(arr, n, k):
    max_sum = INT_MIN

    for i in range(n - k + 1):
        current_sum = 0
        for j in range(k):
            current_sum = current_sum + arr[i + j]
        max_sum = max(current_sum, max_sum)
    return max_sum
 
arr = [1, 4, 2, 10, 2, 3, 1, 0, 20]
k = 4
n = len(arr)
print(maxSum(arr, n, k))
```

**Sliding window approach**
```pycon
def maxSum(arr, n, k):
    window_sum = sum(arr[:k])
    max_sum = window_sum

    for i in range(n - k):
        window_sum = window_sum - arr[i] + arr[i + k]
        max_sum = max(window_sum, max_sum)
 
    return max_sum
 
 
# Driver code
arr = [1, 4, 2, 10, 2, 3, 1, 0, 20]
k = 4
n = len(arr)
print(maxSum(arr, n, k))
```