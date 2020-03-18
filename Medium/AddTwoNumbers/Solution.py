"""
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.


Example:
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""


# Definition for singly-linked list.
class ListNode(object):
   def __init__(self, x):
     self.val = x
     self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        sum=list()
        index=-1
        up=0
        while True:

            tmp=ListNode(l1.val+l2.val)
            if up == 1:
                tmp.val=tmp.val+1
                up=0
            if (tmp.val >=10):
                tmp.val=tmp.val-10
                up=1

            sum.append(tmp)
            if (l1.next==None and l2.next==None):
                if up==1:
                    sum.append(ListNode(1))
                    sum[index].next=sum[index+1]
                    sum[index+1].next=sum[index+2]
                    break
                else:
                    sum[index].next = sum[index + 1]
                    break
            else:
                if(index>=0):
                    sum[index].next=sum[index+1]

            index=index+1

            l1 = l1.next
            l2 = l2.next
        return sum[0]
