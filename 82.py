class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
     
        newHead = ListNode()
        newHead.next = head
        prev = newHead
        while head:
            if(head.next and head.val == head.next.val):
                while(head.next and head.val == head.next.val):
                    head = head.next
                prev.next = head.next
            else:
                prev = prev.next
            head = head.next
    

        return newHead.next
                
        # version 2
        # newHead = ListNode()
        # duplicates = {}
        # temp = head
        # while(temp!=None):
        #     if temp.val not in duplicates.keys():
        #         duplicates[temp.val] = 1
        #     else:
        #         duplicates[temp.val] += 1
        #     temp = temp.next
            
        # temp = head
        # newHead = ListNode()
        # prev = newHead
        # while(temp!=None):
        #     if(duplicates[temp.val]!=1):
        #         for i in range(duplicates[temp.val]):
        #             temp = temp.next    
        #     else:
        #         prev.next = temp
        #         prev = prev.next
        #         temp = temp.next
        # prev.next = None
        
        # return newHead.next