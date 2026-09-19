## Problem: Reverse String (Easy)

**Link:** https://leetcode.com/problems/reverse-string/

### Approach
I used the two-pointer approach to reverse the list in-place. One pointer starts from the beginning of the list and the other starts from the end. The elements at these positions are swapped, and both pointers move toward the center until the entire list is reversed.

### Complexity
- Time: O(n)
- Space: O(1)

### Notes
The solution modifies the original list instead of creating a new list. I tested the solution using a list input in the terminal and used `ast.literal_eval()` to read the input as a Python list.