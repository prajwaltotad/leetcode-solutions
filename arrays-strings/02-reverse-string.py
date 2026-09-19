import ast

class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        srt=0
        end=len(s)-1
        while srt<end:
            s[srt], s[end] = s[end], s[srt]
            srt+=1
            end-=1
        return s

s= ast.literal_eval(input())
print(Solution().reverseString(s))