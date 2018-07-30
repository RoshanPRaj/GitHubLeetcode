class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        temp = x
        rev = 0
        final = 0
        while (temp > 0):
            final = temp % 10
            rev = (rev * 10) + final
            temp = temp / 10
        if rev == x:
            return True
        else:
            return False
