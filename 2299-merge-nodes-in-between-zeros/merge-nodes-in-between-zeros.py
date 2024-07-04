# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeNodes(self, head: ListNode) -> ListNode:
        # Initialize pointers
        current = head.next  # skip the initial zero
        new_head = ListNode(0)  # dummy node for the new list
        new_current = new_head
        sum_nodes = 0
        
        while current:
            if current.val != 0:
                # Accumulate the sum between zeros
                sum_nodes += current.val
            else:
                # When we encounter a zero, create a new node with the accumulated sum
                if sum_nodes != 0:
                    new_current.next = ListNode(sum_nodes)
                    new_current = new_current.next
                    sum_nodes = 0  # reset the sum for the next segment
            current = current.next
        
        return new_head.next
