# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        final = []
        while l1 != None:
            final.append(l1.val)
            l1 = l1.next
        while l2 != None:
            final.append(l2.val)
            l2 = l2.next
        return sorted(final)
        
