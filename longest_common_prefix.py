class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type str: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        strs.sort()
        a = strs[0]
        b = strs[-1]
        print a + b
        minl = min(len(a), len(b))
        s = ''
        for i in range(minl):
            if a[i] != b[i]:
                break
            s = s + a[i]
        return s
