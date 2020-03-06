class Solution:
    def longestPalindrome(self, s: str) -> str:

        result=""
        resultSize=len(s)
        if resultSize==1:
            result=s[0]
        else:
            for i in range(len(s),0,-1):
                if i==1:
                    result=s[0]
                    break
                startIndex=0
                lastInedx=i
                loopNum= resultSize-i+1

                while loopNum >0:
                    tmpS = s[startIndex:lastInedx]
                    # print(tmpS)

                    if tmpS==tmpS[::-1]:
                        result = tmpS
                        return result
                    loopNum-=1
                    startIndex+=1
                    lastInedx+=1

        return result
