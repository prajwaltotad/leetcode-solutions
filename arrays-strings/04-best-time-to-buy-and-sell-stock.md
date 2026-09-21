# 📈 Best Time to Buy and Sell Stock

**LeetCode #121 — Easy**

### 💡 Approach
Keep track of the **minimum price** seen so far and calculate the profit if we sell at the current price.

- `min_price` → lowest price encountered
- `max_profit` → maximum profit found
- Traverse the array only once

### ⏱️ Complexity
- **Time:** `O(n)`
- **Space:** `O(1)`

### 🧠 Key Idea
> Buy at the lowest price seen so far and sell at the current price.