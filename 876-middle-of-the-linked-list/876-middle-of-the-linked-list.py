# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        is_end = False
        length = 0
        
        curr = head
        ans = head
        
        while not is_end:
            
            if curr.next == None:
                length += 1
                is_end = True
            else:
                curr = curr.next
                length += 1
        
        # 5 -> 2
        # 6 -> 3
        mid = length//2
        
        for i in range(mid):
            ans = ans.next
        
        return ans
        
            
        