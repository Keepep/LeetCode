from Medium.Remove_Nth_Node_From_End_of_List.ListNode import ListNode

"""
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
"""


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not (l1 and l2):
            return l1 or l2

        if l1.val > l2.val:
            l1, l2 = l2, l1

        l1.next = self.mergeTwoLists(l1.next, l2)

        return l1