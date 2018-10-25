# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        final=[]
        while head!=None:
            if head.val not in final:
                final.append(head.val)
            head=head.next
        return final
            
