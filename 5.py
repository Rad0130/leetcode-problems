import heapq

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        # Min-heap to store nodes by their value
        heap = []
        
        # Add the head of each list to the heap
        for i in range(len(lists)):
            if lists[i]:  # Check if the list is non-empty
                heapq.heappush(heap, (lists[i].val, i, lists[i]))
        
        # Dummy node to help in merging
        dummy = ListNode()
        current = dummy
        
        # Extract the smallest node from the heap and add it to the merged list
        while heap:
            val, idx, node = heapq.heappop(heap)
            current.next = node  # Add the smallest node to the result list
            current = current.next  # Move the pointer of the result list
            
            # If the extracted node has a next node, push it to the heap
            if node.next:
                heapq.heappush(heap, (node.next.val, idx, node.next))
        
        return dummy.next
