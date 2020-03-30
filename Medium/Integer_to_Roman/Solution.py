class Solution:
    def intToRoman(self, num: int) -> str:
        dict={}
        dict['M']=1000
        dict['CM']=900
        dict['D'] = 500
        dict['CD'] = 400
        dict['C'] = 100
        dict['XC'] = 90
        dict['L']= 50
        dict['XL'] = 40
        dict['X'] = 10
        dict['IX'] = 9
        dict['V'] = 5
        dict['IV'] = 4
        dict['I']=1


        result=''
        for i in dict:
            while num>=dict[i]:
                result+=i
                num-=dict[i]

        return result