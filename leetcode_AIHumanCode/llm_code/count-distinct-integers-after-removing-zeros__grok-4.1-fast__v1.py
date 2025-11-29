class Solution(object):
    def countDistinct(self, n):
        s = str(n)
        length = len(s)
        cnt = 0
        pw = 1
        for _ in range(1, length):
            pw *= 9
            cnt += pw
        cur_pw = pw
        for i in range(length):
            dig = int(s[i])
            if dig == 0:
                break
            cnt += (dig - 1) * cur_pw
            cur_pw //= 9
        else:
            cnt += 1
        return cnt
