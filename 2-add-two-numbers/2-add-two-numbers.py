# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        l1_curr = l1
        l2_curr = l2
        
        l3 = ListNode()
        l3_curr = l3
        
        l1_is_end = False
        l2_is_end = False
        
        while not l1_is_end or not l2_is_end:
            
            node_added = False
            
            if not l1_is_end and not l2_is_end:
                
                l3_curr.val += (l1_curr.val + l2_curr.val)
                
                if l3_curr.val >= 10:
                    l3_curr.val -= 10
                    new_node = ListNode(1,None)
                    l3_curr.next = new_node
                    node_added = True
                    
            if l1_is_end and not l2_is_end:
                
                l3_curr.val += l2_curr.val
                
                if l3_curr.val >= 10:
                    l3_curr.val -= 10
                    new_node = ListNode(1,None)
                    l3_curr.next = new_node
                    node_added = True
            
            if not l1_is_end and l2_is_end:
                
                l3_curr.val += l1_curr.val
                
                if l3_curr.val >= 10:
                    l3_curr.val -= 10
                    new_node = ListNode(1,None)
                    l3_curr.next = new_node
                    node_added = True
            
            if l1_curr.next != None:
                l1_curr = l1_curr.next
            else:
                l1_is_end = True
                
            if l2_curr.next != None:
                l2_curr = l2_curr.next
            else:
                l2_is_end = True
                
            if (not l1_is_end or not l2_is_end) and not node_added:
                new_node = ListNode()
                l3_curr.next = new_node
                l3_curr = l3_curr.next
            
            if (not l1_is_end or not l2_is_end) and node_added:
                l3_curr = l3_curr.next
                
        return l3
        
        