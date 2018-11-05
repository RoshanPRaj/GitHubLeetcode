class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool.
        """
        if x < 0:
            return False
        else:
            y = float(str(x)[::-1].strip('0'))
        if y == x:
            return True
        else:
            return False
