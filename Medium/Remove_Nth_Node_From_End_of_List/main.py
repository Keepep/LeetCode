from Medium.Remove_Nth_Node_From_End_of_List.Solution import Solution
from Medium.Remove_Nth_Node_From_End_of_List.ListNode import ListNode

if __name__ == "__main__":
    li_1 = ListNode(1)
    li_2 = ListNode(2)
    """
    li_3 = ListNode(3)
    li_4 = ListNode(4)
    li_5 = ListNode(5)
    """

    li_1.next=li_2
    """
    li_2.next=li_3
    li_3.next=li_4
    li_4.next=li_5
    """

    n=2

    sol=Solution()
    print('result :{}'.format(sol.removeNthFromEnd(li_1,n)))