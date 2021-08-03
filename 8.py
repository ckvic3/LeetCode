# Reverse Nodes in k-Group
# Definition for singly-linked list.
from typing import List

# memory : O(K) 
# time: O(N)
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseKGroup(self, head:ListNode, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        tempStack = []
        temp = head
        
        newHead = None
        tempHead = None
        while(temp!=None):
            tempStack.append(temp)
            temp = temp.next
            
            if(len(tempStack)==k):
                
                if(newHead==None):
                    newHead = tempStack[k-1]
                    tempHead = newHead
                    for i in range(1,k):
                        tempHead.next = tempStack[k-i-1]
                        tempHead = tempHead.next
                else:
                    for i in range(k):
                        tempHead.next = tempStack[k-i-1]
                        tempHead = tempHead.next
                tempStack =[]
         
        if(len(tempStack)!=0):
            tempHead.next = tempStack[0]
        else:
            tempHead.next = None
        return newHead        


# version 2
class Solution(object):
    def reverseKGroup(self, head:ListNode, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        # reverse all of the list   
        temp = head
        prev = None
        tempNode = None
        length = 0
        while(temp!=None):
            tempNode = temp.next
            temp.next = prev
            prev = temp
            temp = tempNode
            length = length + 1
        
        new_head = prev
        

        # reverse tail list
        tail_length = length % k
        tail = None
        if(tail_length!=0):
            temp = new_head
            prev = None
            tempNode = None
            while(tail_length!=0):
                tempNode = temp.next
                temp.next = prev
                prev = temp
                temp = tempNode
                tail_length = tail_length - 1
            
            tail = prev
            new_head = temp

        temp = new_head
        prev = tail
        tempNodeHead = None
        tempNodeNext = None
        while(temp!=None):
            tempNodeHead = temp
            for i in range(k-1):
                temp = temp.next
            tempNodeNext = temp.next
            temp.next = prev
            prev = tempNodeHead
            temp = tempNodeNext

        new_head = prev
        return new_head   
            
            
                        
            
        
             