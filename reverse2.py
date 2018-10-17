class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            num = int('-'+str(x)[::-1].strip('0').replace('-',''))
        else:
            num = int(str(x)[::-1])
        if (num < (-2)**31) or (num >= (((2)**31)-1)):
            return 0
        else:
            return num
