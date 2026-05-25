# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nexttwo = None
        if head:
            current = head
            if head.next:
                next = head.next
                if head.next.next:
                    nexttwo = next.next
                else:
                    current.next = None
                    next.next = current
                    return next
            else:
                return head
        else:
            return None

        prev = None

        while nexttwo:
            current.next = prev
            next.next = current
            
            prev = current
            current = next
            next = nexttwo

            if nexttwo.next == None:
                nexttwo.next = current
                return nexttwo
            else: 
                nexttwo = nexttwo.next


        

        