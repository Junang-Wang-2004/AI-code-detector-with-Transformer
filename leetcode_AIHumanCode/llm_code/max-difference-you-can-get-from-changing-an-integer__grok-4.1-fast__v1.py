class Solution:
    def maxDiff(self, num):
        s = str(num)
        d1 = '0'
        for i in range(len(s)):
            if s[i] != '9':
                d1 = s[i]
                break
        big = s.replace(d1, '9')
        d2 = '0'
        r = '0'
        for i in range(len(s)):
            if s[i] > '1':
                d2 = s[i]
                r = '1' if i == 0 else '0'
                break
        small = s.replace(d2, r)
        return int(big) - int(small)
