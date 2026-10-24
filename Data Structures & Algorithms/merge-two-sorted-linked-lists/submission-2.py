# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        node1 = list1
        node2 = list2

        head = ListNode()
        curr_node = head

        while node2 or node1:
            if node2 and node1:
                if node1.val > node2.val:
                    curr_node.next = node2
                    curr_node = curr_node.next
                    node2 = node2.next
                else:
                    curr_node.next = node1
                    curr_node = curr_node.next
                    node1 = node1.next
            elif node1:
                curr_node.next = node1
                curr_node = curr_node.next
                node1 = node1.next
            else:
                curr_node.next = node2
                curr_node = curr_node.next
                node2 = node2.next
        return head.next
                

