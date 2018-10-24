class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip()
        if s == '':
            return 0
        t = s.split(' ')
        if t[-1] == ' ':
            return len(t[-2])
        if len(t) > 0:
            return len(t[-1])
        return 0
