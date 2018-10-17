class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        lookup = {}
        for index,value in enumerate(nums):
            if target - value in lookup:
                return lookup[target - value],index
            lookup[value] = index
     
