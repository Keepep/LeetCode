from Medium.AddTwoNumbers.Solution import Solution,ListNode


if __name__ == "__main__":
    l1_1 = ListNode(2)
    l1_2 = ListNode(4)
    l1_3 = ListNode(1)


    l1_1.next = l1_2
    l1_2.next = l1_3


    l2_1 = ListNode(5)
    l2_2 = ListNode(6)
    l2_3 = ListNode(4)


    l2_1.next = l2_2
    l2_2.next = l2_3

    sol = Solution()
    sum = sol.addTwoNumbers(l1_1, l2_1)

    while True:
        print(sum.val)
        if (sum.next == None):
            break
        sum = sum.next
