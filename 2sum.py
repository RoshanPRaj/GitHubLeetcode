class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums : List[int]
        :type target: int
        :rtype: List[int]
        """
        search_dict = {}
        for index,value in enumerate(nums):
            if target - value in search_dict:
                return search_dict[target-value], index
            search_dict[value] = index
