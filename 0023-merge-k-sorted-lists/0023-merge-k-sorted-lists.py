# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        # # initialization
        # head = None
        # curr = None
        # length = len(lists)
        # compare = {i:None for i in range(length)}

        # # exception: all of linkedlist are empty
        # if Counter(compare)[None] == length:
        #     return head

        # # exception: no list
        # if not lists:
        #     return head
        
        # # exception: single list
        # if len(lists) == 1:
        #     return lists[0]

        # # save first nodes
        # for i, linkedlist in enumerate(lists):
        #     if linkedlist:
        #         # get value of nodes
        #         compare[i] = linkedlist.val
        #         # point the next node
        #         lists[i] = linkedlist.next
        #     else:
        #         compare[i] = None

        # # approach : BFS
        # while set(compare.values())-{None}:
            
        #     # find min value
        #     min_val = min(set(compare.values())-{None})
        #     # get key of min value
        #     key = [k for k,v in compare.items() if v == min_val]
        #     # exception for duplicate and list type data(e.g., ['0'])
        #     key = key[0]
            
        #     if lists[key]:
        #         # set value in dictionary
        #         compare[key] = lists[key].val
        #         # point the next node
        #         lists[key] = lists[key].next
        #     else:
        #         compare[key] = None

        #     if curr:
        #         tmp = ListNode(min_val)
        #         curr.next = tmp
        #         curr = curr.next
        #     else:
        #         head = ListNode(min_val)
        #         curr = head
            
        # return head

        # simple solution -> get all nodes -> sort -> make linkedlist

        head = None
        curr = None
        node_vals = []

        # exception: no list
        if not lists:
            return head
        
        # exception: single list
        if len(lists) == 1:
            return lists[0]
        
        for linkedlist in lists:
            while linkedlist:
                node_vals.append(linkedlist.val)
                linkedlist = linkedlist.next

        node_vals.sort()
        
        for value in node_vals:
            if curr:
                tmp = ListNode(value)
                curr.next = tmp
                curr = curr.next
            else:
                head = ListNode(value)
                curr = head

        return head