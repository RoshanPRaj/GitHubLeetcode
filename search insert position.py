class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target < nums[0]:
            return 0
        if target > nums[-1]:
            return len(nums)
        for i in range(len(nums)):
            if target == nums[i]:
                return i
            elif nums[i] > target and i!=0:
                return i
