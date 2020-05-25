# Odd Even Linked List
# https://leetcode.com/problems/odd-even-linked-list/
''' Given a singly linked list, group all odd nodes together followed by the even nodes. Please note here we are talking about the node number and not the value in the nodes.

You should try to do it in place. The program should run in O(1) space complexity and O(nodes) time complexity.'''

def oddEvenList(self, head: ListNode) -> ListNode:
        
        oddt = ListNode(0)
        event = ListNode(0)
        odd = oddt
        even = event
        o = 1
        while (head):
            if (o % 2 != 0):
                oddt.next = head
                oddt = oddt.next
            else:
                event.next = head
                event = event.next
                
            o += 1
            head = head.next
            
        event.next = None
        oddt.next = even.next
        
        return odd.next
        
#This will run only in the Leetcode compiler because of the ListNode class in that
