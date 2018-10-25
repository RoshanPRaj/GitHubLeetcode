class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        a = len(nums2)
        #print a
        while a >= 1:
            nums1.remove(0)
            a -= 1
        #print nums1
        for i in nums2:
            #print i
            nums1.append(i)
        #print nums1
        nums1 = nums1.sort()
