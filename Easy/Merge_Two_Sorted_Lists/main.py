from Easy.Merge_Two_Sorted_Lists.Solution import Solution
from Medium.Remove_Nth_Node_From_End_of_List.ListNode import ListNode


if __name__ == "__main__":
    l1_1= ListNode(1)
    l1_2= ListNode(2)
    l1_3= ListNode(4)


    l2_1= ListNode(1)
    l2_2= ListNode(3)
    l2_3= ListNode(4)

    l1_1.next=l1_2
    l1_2.next=l1_3

    l2_1.next=l2_2
    l2_2.next=l2_3
    sol=Solution()
    print('result :{}'.format(sol.mergeTwoLists(l1_1,l2_1)))