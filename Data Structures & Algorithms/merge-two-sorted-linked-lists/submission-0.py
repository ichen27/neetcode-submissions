# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Create new linked list
        # Iterate through both lists, while loop until there is no next for both
        # compare value at each iteration, and append the smaller on to the linked list
        # append both if equal
        # once appended, iterate 
        # If not appened, stay
        list3 = ListNode(1, None)
        temp1 = list1
        temp2 = list2
        temp3 = list3

        while True:
            
            if temp1 is not None and temp2 is not None:
                if temp1.val <= temp2.val:
                    temp3.next = temp1
                    print(f"1: {temp3.val}")
                    temp3 = temp3.next
                    temp1 = temp1.next
                elif temp1.val > temp2.val:
                    temp3.next = temp2
                    print(f"2: {temp3.val}")
                    temp3 = temp3.next
                    temp2 = temp2.next   
            elif temp1 is None and temp2 is None:
                return list3.next
            elif temp2 is not None:
                temp3.next = temp2
                print(f"3: {temp3.val}")
                temp3 = temp3.next
                temp2 = temp2.next
            elif temp1 is not None:
                temp3.next = temp1
                print(f"4: {temp3.val}")
                temp3 = temp3.next
                temp1 = temp1.next


            

