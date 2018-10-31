'''
Write a function to find the longest common prefix string amongst an array of 
strings.

If there is no common prefix, return an empty string "".

Note:

All given inputs are in lowercase letters a-z.
'''

class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        if not strs:
            return ""

        
