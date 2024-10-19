class Solution(object):
    def reverse(self, x):
        l=str(x)
        r=''
        if l[0]=='-':
            l=l[1::]
            r='-'
        for i in range(len(l)-1,-1,-1):
            r+=l[i]

        x=int(r)
        if -2**31<x<2**31-1:
            return x
        return 0


x=-123
obj=Solution()
print(obj.reverse(x))
