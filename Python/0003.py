'''
3. Longest Substring Without Repeating Characters
'''

def lengthOfLongestSubstring(self, s: str) -> int:
    if not s:
        return 0
    if len(s) == 1:
        return 1
    temp = []

    for i in range(len(s) - 1):
        start = i
        end = i + 1
        while end < len(s) and s[end] not in s[start:end]:
            end += 1
        temp.append(end - start)

    return max(temp)