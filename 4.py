class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        # Helper function to reverse a portion of the linked list
        def reverseLinkedList(head, k):
            new_head = None
            ptr = head
            while k > 0:
                next_node = ptr.next
                ptr.next = new_head
                new_head = ptr
                ptr = next_node
                k -= 1
            return new_head
        
        # First, check if there are at least k nodes left in the list.
        count = 0
        ptr = head
        while count < k and ptr:
            ptr = ptr.next
            count += 1
        
        # If we have k nodes, then we reverse them
        if count == k:
            # Reverse the first k nodes of the list
            reversed_head = reverseLinkedList(head, k)
            
            # Now, recurse with the remaining part of the list
            # head becomes the end of the reversed group, connect it to the next group
            head.next = self.reverseKGroup(ptr, k)
            
            return reversed_head
        
        # If we've fewer than k nodes, return the head as it is
        return head
