# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        curr = dummy = ListNode(0)
        while list1 and list2: #continue in this loop as long as list1,2 has a value
            if list1.val > list2.val:
                curr.next = list2 #if list2 has a smaller value , pick that value
                list2 = list2.next #moving the list2 pointer
            else:
                curr.next = list1
                list1 = list1.next
            curr = curr.next

        if not list1: #  if no more values in list1 then add the remaing list2 values to the list
            curr.next = list2
        else:
            curr.next = list1
        return dummy.next