## Problem: Valid Anagram (Easy)

**Link:** https://leetcode.com/problems/valid-anagram/

### Approach
I used Python's `sorted()` function to sort both strings alphabetically. If the sorted versions of both strings are equal, they contain the same characters with the same frequencies, so they are anagrams. Otherwise, they are not anagrams.

### Complexity
- Time: O(n log n)
- Space: O(n)

### Notes
The solution compares the sorted characters of both strings. If the strings have different lengths or different characters, the sorted lists will not be equal. I tested the solution using string inputs entered through the terminal.