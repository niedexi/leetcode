



class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        number = 0
        length = len(s)
        for i in range(length):
            if i > 0 and roman[s[i]] > roman[s[i-1]]:
                number += roman[s[i]] - 2 * roman[s[i-1]]
            else:
                number += roman[s[i]]
        return number
