# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited_set = set()
        while head:
            if head in visited_set:
                return True
            
            visited_set.add(head)
            head = head.next
        
        return False