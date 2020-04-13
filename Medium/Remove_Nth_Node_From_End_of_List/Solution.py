from Medium.Remove_Nth_Node_From_End_of_List.ListNode import ListNode
"""
Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.
Note:

Given n will always be valid.
"""

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        target=-n+1
        tmp=head
        while tmp.next != None:
            target+=1
            tmp=tmp.next

        tmp=head
        if target ==0:
            if head.next == None:
                head.val=''
                return head
            else:
                head=head.next
                return head
        for i in range(target):

            if i == target-1:
                li_tmp=tmp.next
                if li_tmp.next ==None:
                    tmp.next= None
                else:
                    tmp.next=li_tmp.next
                return head

            tmp=tmp.next
