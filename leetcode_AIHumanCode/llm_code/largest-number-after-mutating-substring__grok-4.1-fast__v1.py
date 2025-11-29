class Solution(object):
    def maximumNumber(self, num, change):
        n = len(num)
        begin = -1
        for p in range(n):
            digit = int(num[p])
            if change[digit] > digit:
                begin = p
                break
        if begin == -1:
            return num
        end = n
        for p in range(begin, n):
            digit = int(num[p])
            if change[digit] < digit:
                end = p
                break
        ans = []
        for p in range(n):
            digit = int(num[p])
            if begin <= p < end:
                ans.append(str(change[digit]))
            else:
                ans.append(num[p])
        return ''.join(ans)
