# 🧩 Valid Parentheses

**LeetCode #20 — Easy**

### 💡 Approach
Use a stack to keep track of opening brackets.

- Push every opening bracket onto the stack.
- For a closing bracket, check if it matches the top of the stack.
- If it doesn't match or the stack is empty, return `False`.
- At the end, the stack must be empty for the parentheses to be valid.

### ⏱️ Complexity
- **Time:** `O(n)`
- **Space:** `O(n)`

### 🧠 Key Idea
> Every closing bracket must match the most recently opened bracket.