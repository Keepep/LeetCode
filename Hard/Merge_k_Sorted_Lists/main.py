from Hard.Merge_k_Sorted_Lists.Solution import Solution
from Hard.Merge_k_Sorted_Lists.ListNode import ListNode

if __name__ == "__main__":
    list=list()

    l1_1 = ListNode(1)
    l1_2 = ListNode(4)
    l1_3 = ListNode(5)

    l1_1.next=l1_2
    l1_2.next=l1_3

    l2_1 = ListNode(1)
    l2_2 = ListNode(3)
    l2_3 = ListNode(4)

    l2_1.next=l2_2
    l2_2.next=l2_3

    l3_1 = ListNode(2)
    l3_2 = ListNode(6)

    l3_1.next=l3_2


    list.append(l1_1)
    list.append(l2_1)
    list.append(l3_1)


    sol=Solution()
    print('result :{}'.format(sol.mergeKLists(list)))