class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: ListNode
        :type list2: ListNode
        :rtype: ListNode
        """
        # Create a dummy node to start the merged list
        dummy = ListNode(-1)
        # Tail will point to the last node in the merged list
        tail = dummy
        
        # Iterate while both lists are non-empty
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1  # Link to the smaller node (list1)
                list1 = list1.next  # Move to the next node in list1
            else:
                tail.next = list2  # Link to the smaller node (list2)
                list2 = list2.next  # Move to the next node in list2
            tail = tail.next  # Move tail to the newly added node
        
        # At this point, at least one of the lists is empty.
        # Attach the remaining part of the non-empty list.
        if list1:
            tail.next = list1
        if list2:
            tail.next = list2
        
        # The merged list starts at dummy.next (skip the dummy node)
        return dummy.next
        
