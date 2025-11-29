from collections import deque

class Solution:
    def findInteger(self, k, digit1, digit2):
        INT_MAX = (1 << 31) - 1
        digits = sorted(set([digit1, digit2]))
        q = deque()
        for d in digits:
            num = d
            if k < num <= INT_MAX and num % k == 0:
                return num
            q.append(num)
        seen = set(q)
        while q:
            curr = q.popleft()
            for d in digits:
                next_num = curr * 10 + d
                if next_num > INT_MAX:
                    continue
                if next_num in seen:
                    continue
                seen.add(next_num)
                if k < next_num and next_num % k == 0:
                    return next_num
                q.append(next_num)
        return -1
