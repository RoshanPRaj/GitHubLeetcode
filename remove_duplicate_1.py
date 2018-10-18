class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return len(nums)
        temp = 0
        
        for i in range(1,len(nums)):
            if nums[i] != nums[temp]:
                temp = temp + 1
                nums[temp] = nums[i]
                
        return temp + 1
