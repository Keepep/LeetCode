class Solution:
    def convert(self, s: str, numRows: int) -> str:
        size=len(s)

        if numRows <=1:
            return s
        else:
            interval=numRows-2

        iter=interval+numRows
        result=list()
        for i in range(numRows):
            for j in range(i,size,iter):
                result.append(s[j])
                if i!=0 and i!=numRows-1 and iter+j-2*i < size:
                    result.append(s[iter+j-2*i])


        return ''.join(result)