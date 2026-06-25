# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        mid=head
        tail=head.next
        while tail and tail.next:
            mid=mid.next
            tail=tail.next.next
        
        prev=None
        while mid:
            nextNode=mid.next
            mid.next=prev
            prev=mid
            mid=nextNode
        tail=prev
        first=head
        while first and tail:
            f_next=first.next
            first.next=tail
            first=f_next

            t_next=tail.next
            tail.next=first
            tail=t_next
        
