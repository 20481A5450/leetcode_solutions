# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def splitListToParts(self, head: ListNode, k: int) -> List[ListNode]:
        # Step 1: Find the length of the linked list
        length = 0
        current = head
        while current:
            length += 1
            current = current.next
        
        # Calculate the size of each part and the number of larger parts
        part_size = length // k
        larger_parts = length % k
        
        # Initialize variables
        current = head
        parts = []
        
        # Step 2: Split the linked list into parts
        for i in range(k):
            part_head = current
            part_length = part_size + (1 if i < larger_parts else 0)
            
            # Move to the end of the part
            for j in range(part_length - 1):
                if current:
                    current = current.next
            
            # If the current node exists, detach it from the next part
            if current:
                next_node = current.next
                current.next = None
                current = next_node
            
            parts.append(part_head)
        
        return parts