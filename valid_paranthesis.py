class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        lookup_dict = {')':'(','}':'{',']':'['}
        stack = []
        for char in s:
            if char in lookup_dict.values():
                stack.append(char)
            elif char in lookup_dict.keys():
                if stack == [] or lookup_dict[char] != stack.pop():
                    return False
            else:
                return False
        return stack == []
