## Problem: Two Sum (Easy)

**Link:** https://leetcode.com/problems/two-sum/

### Approach
I used a brute-force approach with two nested loops. The first loop selects an element, and the second loop checks every element after it to find a pair whose sum is equal to the target. When the required pair is found, the function returns their indices.

### Complexity
- Time: O(n²)
- Space: O(1)

### Notes
The solution should check pairs starting from `i + 1` so that the same element is not used twice. I also tested a typical case and an edge case with duplicate values before submitting the solution to LeetCode.