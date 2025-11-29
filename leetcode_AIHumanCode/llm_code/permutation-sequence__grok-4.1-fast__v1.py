class Solution(object):
    def getPermutation(self, n, k):
        k -= 1
        factorial = [1] * (n + 1)
        for i in range(1, n + 1):
            factorial[i] = factorial[i - 1] * i
        mask = 0
        output = []
        for remaining in range(n - 1, -1, -1):
            step = factorial[remaining]
            index = k // step
            k %= step
            cnt = 0
            for digit in range(1, n + 1):
                bit = 1 << (digit - 1)
                if (mask & bit) == 0:
                    if cnt == index:
                        output.append(str(digit))
                        mask |= bit
                        break
                    cnt += 1
        return ''.join(output)
