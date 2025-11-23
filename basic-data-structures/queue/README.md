## 🔁 Queue 



- Works on the principle: "**First In, First Out**" (FIFO). 
- It supports three operations:
  - **insert** (or "push"): putting an item into the end of the queue. 
  - **peek**: look at the first item of the queue. 
  - **remove** (or "pop"): remove the first item of the queue.


###  Implementation
- We use an array and two pointers, one pointing at the start of the queue and the other pointing at the end. 
- When inserting an item into the queue, we set the entry at the end pointer to the value and increase the end pointer. 
- When removing an item from the queue, we increase the start pointer by one.

---

## Deque - Double Ended Queue


- Imagine a bookshelf where you can add or remove books from both ends with ease.  
This concept is a practical representation of a deque (pronounced "deck"), a contraction of "Double-Ended QUEue."
- Unlike regular queues that only allow adding and removing items from one end, deque provides flexibility by letting you interact from both ends. 
- It supports six operations:
  - **insert front**(or "push front"): putting an item in the beginning of the deque.
  - **insert back**(or "push back"): putting an item in the end of the deque. 
  - **peek front**: Look at the first item of the deque. 
  - **peek back**: Look at the last item of the deque. 
  - **remove front**(or "pop front"): removing the item at the beginning of the deque.
  - **remove back**(or "pop back"): removing the item at the end of the deque.

---

