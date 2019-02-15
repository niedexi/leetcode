'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', 
determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.
'''

def isValid(self, s):
    """
    :type s: str
    :rtype: bool
    """
    stack = []
    mapping = {"(": ")", "[": "]", "{": "}"}

    for item in s:
    	if item in mapping:
    		stack.append(item)
    	elif len(stack) == 0 or mapping[stack.pop()] !=item:
    		return False
    return not stack

