# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        root = ListNode(val=-9999, next=head)
        
        pos = head
        
        while pos.next:
            if pos.next.val < pos.val:
                find = False
                prev = None
                curr = root
                while not find:
                    if curr.val > pos.next.val:
                        find = True
                        tmp = pos.next
                        prev.next = pos.next
                        pos.next = pos.next.next
                        tmp.next = curr
                    else:
                        prev = curr
                        curr = curr.next
            else:
                pos = pos.next
        
        return root.next