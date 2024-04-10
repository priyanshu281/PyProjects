from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val=val
        self.next= next




class Solution:
    def removeNthNodeFromEnd(self, head: Optional[ListNode], n:int) -> Optional[ListNode]:
        s=f=head
        if f.next == None:
            return None
        while n > 0:
            f = f.next
            n -= 1
        while f and f.next:
            s = s.next
            f = f.next
        s.next = s.next.next
        return head

    def list_to_linkked_list(self, nums):
        if not nums:
            return None
        dummy= head=ListNode()
        for i in nums:
            dummy.next=ListNode(i)
            dummy= dummy.next
        return head.next

if __name__ == "__main__":
    li=[1,2,3,4,5]
    s=Solution()
    cr=s.list_to_linkked_list(li)
    new_cr=s.removeNthNodeFromEnd(cr, 2)
    while new_cr:
        print(new_cr.val)
        new_cr=new_cr.next







