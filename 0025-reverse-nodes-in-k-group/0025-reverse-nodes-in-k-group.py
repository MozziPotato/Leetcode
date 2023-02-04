# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# time consumed: an hour (PM 4:14 ~ PM 5:14)
# approach: recursion
# Follow-up: Can you solve the problem in O(1) extra memory space?

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        # exception: nothing to reverse
        if k == 1 or not head:
            return head

        def recursion(head: Optional[ListNode], prev: Optional[ListNode], k: int, n: int) -> Optional[ListNode]:
            # base case: all nodes are reversed
            if not head:
                return None

            probe = head
            count = 0

            # get end node of a k-group
            while probe and count < k:
                probe = probe.next
                count += 1

            # base case: less than k nodes
            if count < k:
                return None

            following = current = head
            following = following.next

            # reversing with triple pointers (probe, current, following)
            while True:
                current.next = probe
                if count == 1:
                    break
                else:
                    probe = current
                    current = following
                    following = following.next
                    count -= 1
            
            # last k-group's head points the current node
            prev.next = current

            # do recursively
            recursion(following, head, k, n+1)
            
            # get the head from first try and return it
            if n == 1:
                return current
        
        return recursion(head, ListNode(), k, 1)