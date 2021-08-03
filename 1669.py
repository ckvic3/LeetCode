# Merge In Between Linked Lists

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        
        head1 = list1
        head2 = list1
        for i in range(a-1):
            head1 = head1.next
        for i in range(b):
            head2 = head2.next

        tail = list2
        while(tail.next!=None):
            tail = tail.next
        head1.next = list2
        tail.next = head2
        return list1