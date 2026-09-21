import ast

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = ""

        for chars in zip(*strs):
            if len(set(chars)) != 1:
                break
            prefix += chars[0]

        return prefix

strs=ast.literal_eval(input())
res=Solution().longestCommonPrefix(strs)
print(res)