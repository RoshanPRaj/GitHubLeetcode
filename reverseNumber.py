class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        temp_num = 0
        if x == 0:
            return 0
        if x < 0:
            x = x * -1
            while (x>0):
                temp_num = (temp_num*10) + (x % 10)
                x = x/10
            return -1 * temp_num
        else:
            while (x>0):
                temp_num = (temp_num*10) + (x % 10)
                x = x/10
            return temp_num
        x = int(str(x))
        if x not in range(-2147483648,2147483647):
            return 0
