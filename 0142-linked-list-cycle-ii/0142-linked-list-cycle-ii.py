# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = head
        slow = head
        
        while(fast and fast.next and fast.next.next):
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                break
        else:
            return None
        
        temp = head
        while(temp is not fast):
            temp = temp.next
            fast = fast.next
        return temp