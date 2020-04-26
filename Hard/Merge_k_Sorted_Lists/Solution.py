"""
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
"""

from Hard.Merge_k_Sorted_Lists.ListNode import ListNode
import heapq

class Solution:
    def mergeKLists(self, lists) -> ListNode:
        h= [ (li.val , index)  for index, li in  enumerate(lists) if li]
        result=start=ListNode(None)


        #time complexity: O(log k)
        heapq.heapify(h)

        #time complexity: O(N*logk), where N is total number of node in lists
        while h:
            val, index =heapq.heappop(h)


            start.next=ListNode(val)
            start=start.next

            lists[index] = lists[index].next
            if lists[index]:
                heapq.heappush(h, (lists[index].val, index))

        return result.next