class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        lookup_dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        previous = 0
        running_total = 0

        for i in range(len(s)-1, -1, -1):
            initial_value = lookup_dict[s[i]]
            if initial_value < previous:
                running_total -= initial_value
            else:
                running_total += initial_value
            previous = initial_value
        return running_total

        
