import math

class Solution:
    def idealArrays(self, n, maxValue):
        MOD = 10**9 + 7
        m = maxValue
        maxn = n + 30
        factorial = [1] * (maxn + 1)
        for i in range(1, maxn + 1):
            factorial[i] = factorial[i - 1] * i % MOD
        inv_factorial = [0] * (maxn + 1)
        inv_factorial[maxn] = pow(factorial[maxn], MOD - 2, MOD)
        for i in range(maxn - 1, -1, -1):
            inv_factorial[i] = inv_factorial[i + 1] * (i + 1) % MOD
        def binomial(total, choose):
            if choose < 0 or choose > total:
                return 0
            return factorial[total] * inv_factorial[choose] % MOD * inv_factorial[total - choose] % MOD
        sqrtm = int(math.sqrt(m)) + 1
        prime_flag = [True] * (sqrtm + 1)
        prime_flag[0] = prime_flag[1] = False
        prime_list = []
        for i in range(2, sqrtm + 1):
            if prime_flag[i]:
                prime_list.append(i)
                for multiple in range(i * i, sqrtm + 1, i):
                    prime_flag[multiple] = False
        def get_exponents(num):
            exponent_map = {}
            for p in prime_list:
                if p * p > num:
                    break
                count = 0
                while num % p == 0:
                    count += 1
                    num //= p
                if count:
                    exponent_map[p] = count
            if num > 1:
                exponent_map[num] = 1
            return exponent_map
        answer = 0
        for val in range(1, m + 1):
            exponents = get_exponents(val)
            ways = 1
            for cnt in exponents.values():
                ways = ways * binomial(n + cnt - 1, cnt) % MOD
            answer = (answer + ways) % MOD
        return answer
