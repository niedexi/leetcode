'''
Write a function to find the longest common prefix string amongst an array of 
strings.

If there is no common prefix, return an empty string "".

Note:

All given inputs are in lowercase letters a-z.
'''


def longestCommonPrefix(self, strs):
    """
    :type strs: List[str]
    :rtype: str
    """

    if not strs: return ""
    for i in range(len(strs[0])):
        for item in strs[1:]:
            if i >= len(item) or item[i] != strs[0][i]:
                return strs[0][:i]
    return strs[0]

