class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # Base case: if there are fewer than two nodes, return head
        if not head or not head.next:
            return head
        
        # New head will be the second node
        new_head = head.next
        # Recursively swap the rest of the list starting from the third node
        head.next = self.swapPairs(new_head.next)
        # Make the second node point to the first node
        new_head.next = head
        
        # Return the new head, which is the second node
        return new_head
        
