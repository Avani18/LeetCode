# Add Two Numbers

def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
    num1 = ''
    num2 = ''
    while(l1 != None or l2 != None):
        if l1:
            num1 += str(l1.val)
            l1 = l1.next
        if l2:
            num2 += str(l2.val)
            l2 = l2.next
           
        
    num1 = num1[::-1]
    num2 = num2[::-1]
    print (num1)
    print (num2)
    ans = str(int(num1) + int(num2))
    head = ListNode(val = ans[-1])
    temp = head
    for i in range(len(ans)-2, -1, -1):
        ans_node = ListNode(val = ans[i])
        temp.next = ans_node
        temp = temp.next
    return head
            