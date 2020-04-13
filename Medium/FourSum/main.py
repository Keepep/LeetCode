from Medium.FourSum.Solution import Solution


if __name__ == "__main__":
    input=[1, 0, -1, 0, -2, 2]
    target=0

    sol=Solution()
    print('result :{}'.format(sol.fourSum(input,target)))