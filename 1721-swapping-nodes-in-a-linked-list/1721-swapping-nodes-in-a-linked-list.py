# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        traverse = head
        
        list = []
        
        while(traverse is not None):
            list.append(traverse.val)
            traverse = traverse.next
        
        first = k - 1
        second = len(list) - k
            
        list[first], list[second] = list[second], list[first]
        
        i = 0
        traverse = head
        while(traverse is not None):
            traverse.val = list[i]
            traverse = traverse.next
            i += 1
        
        return head
        