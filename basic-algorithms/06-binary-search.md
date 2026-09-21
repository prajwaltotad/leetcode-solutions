# 🔍 Binary Search

**LeetCode #704 — Easy**

### 💡 Approach
Use two pointers, `left` and `right`, to repeatedly divide the sorted array in half.

- Calculate the middle index.
- If `nums[mid] == target`, return the index.
- If the middle value is greater, search the left half.
- Otherwise, search the right half.
- Return `-1` if the target is not found.

### ⏱️ Complexity
- **Time:** `O(log n)`
- **Space:** `O(1)`

### 🧠 Key Idea
> Eliminate half of the search space after every comparison.