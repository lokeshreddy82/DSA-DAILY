# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import sys
sys.set_int_max_str_digits(0)
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        countt=0
        st=""
        curr=head
        while curr:
            countt +=1
            st +=str(curr.val)
            curr=curr.next
        s=str(int(st)*2)
        curr=ListNode(int(s[0]))
        temp=curr
        l=1
        while temp:
            if l<len(s):
                temp.next=ListNode(int(s[l]))
                l+=1
                temp=temp.next
            else:
                break
        return curr
            

         