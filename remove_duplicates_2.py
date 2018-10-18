from collections import OrderedDict
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums[:] = OrderedDict.fromkeys(nums)
        print len(nums)
