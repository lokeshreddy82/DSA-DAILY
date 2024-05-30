# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev,curr=head,head.next
        while curr:
            if curr.val>prev.val:
                prev=head
                while prev:
                    if prev.next==curr.next:
                        break
                    elif curr.val>prev.val:
                        prev.val=prev.next.val
                        prev.next=prev.next.next
                    else:
                        prev=prev.next
                curr=curr.next
            else:
                curr=curr.next
                prev=prev.next
        return head
        