class Solution(object):
    def myAtoi(self, s):
        n_s = ''
        i = 0


        while i < len(s) and s[i] == ' ':
            i += 1

        if i < len(s) and (s[i] == '-' or s[i] == '+'):
            n_s += s[i]
            i += 1

        while i < len(s) and s[i].isdigit():
            n_s += s[i]
            i += 1

        if len(n_s) == 0 or (len(n_s) == 1 and not n_s.isdigit()):
            return 0
        elif int(n_s) < -2 ** 31:
            return -2 ** 31
        elif int(n_s) > 2 ** 31 - 1:
            return 2 ** 31 - 1
        else:
            return int(n_s)


# Test the function
s = "-91283472332"
object = Solution()
print(object.myAtoi(s))
