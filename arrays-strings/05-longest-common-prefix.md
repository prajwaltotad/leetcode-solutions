# 🔤 Longest Common Prefix

**LeetCode #14 — Easy**

### 💡 Approach
Use `zip(*strs)` to compare characters at the same position across all strings.

- `zip(*strs)` groups characters column-wise.
- `set(chars)` checks if all characters are identical.
- Stop when a mismatch is found.
- Add matching characters to `prefix`.

### ⏱️ Complexity
- **Time:** `O(n × m)`
- **Space:** `O(n)`

### 🧠 Key Idea
> Compare each character position across all strings and stop at the first mismatch.