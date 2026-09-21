class Solution:
    def myAtoi(self, s):
        s = s.strip()

        if not s:
            return 0

        sign = 1
        i = 0

        if s[0] == '-':
            sign = -1
            i += 1
        elif s[0] == '+':
            i += 1

        ans = 0

        while i < len(s) and s[i].isdigit():
            ans = ans * 10 + int(s[i])
            i += 1

        ans = ans * sign

        if ans < -2**31:
            return -2**31

        if ans > 2**31 - 1:
            return 2**31 - 1

        return ans