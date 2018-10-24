class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        s = ''
        s = s.join(str(i) for i in digits)
        t = int(s) + 1
        return [int(a) for a in str(t)]
