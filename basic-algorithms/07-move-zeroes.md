# 🟢 Move Zeroes

**LeetCode #283 — Easy**

### 💡 Approach
Use two pointers to move all non-zero elements to the front while keeping their order.

- `i` scans through the array.
- `j` tracks the position for the next non-zero element.
- Swap `nums[i]` with `nums[j]` whenever a non-zero element is found.
- Zeros naturally move towards the end.

### ⏱️ Complexity
- **Time:** `O(n)`
- **Space:** `O(1)`

### 🧠 Key Idea
> Move non-zero elements forward in-place while preserving their relative order.