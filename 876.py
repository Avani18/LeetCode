# Middle of the Linked List
# https://leetcode.com/problems/middle-of-the-linked-list/
# Given a non-empty, singly linked list with head node head, return a middle node of linked list. If there are two middle nodes, return the second middle node.

def middleNode(self, head: ListNode) -> ListNode:
        p1= head
        p2= head
        while (p2!=None and p2.next!=None):
            p1= p1.next
            p2= p2.next.next
        return p1

#This will run only in the Leetcode compiler because of the Linked List class in that
