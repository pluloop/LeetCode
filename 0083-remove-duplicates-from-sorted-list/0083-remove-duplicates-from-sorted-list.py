# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        current = head
        after = head
        
        if after is None or after.next is None:
            return head
        if after.next.next is None:
            after = after.next
            if current.val == after.val:
                current.next = None
                return head
            return head
        
        head = temp
        while(after.next is not None):
            after = after.next
            current.next = after
            if current.val == after.val:
                current.next = None
            else:
                current = current.next
        return temp
                