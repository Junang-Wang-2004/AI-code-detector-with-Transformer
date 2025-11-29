import collections
import math

MAX_VAL = 100010

def compute_spf():
    spf = list(range(MAX_VAL))
    for i in range(2, int(math.sqrt(MAX_VAL)) + 1):
        if spf[i] == i:
            for j in range(i * i, MAX_VAL, i):
                if spf[j] == j:
                    spf[j] = i
    return spf

SPF = compute_spf()

class Solution:
    def sumOfAncestors(self, n, edges, nums):
        def squfree(num):
            if num <= 1:
                return num
            prod = 1
            temp = num
            while temp > 1:
                p = SPF[temp]
                count = 0
                while temp % p == 0:
                    temp //= p
                    count += 1
                if count % 2:
                    prod *= p
            return prod

        tree = [[] for _ in range(n)]
        for x, y in edges:
            tree[x].append(y)
            tree[y].append(x)

        node_key = [squfree(val) for val in nums]

        count_map = collections.Counter()

        def explore(curr, prev):
            accum = count_map[node_key[curr]]
            count_map[node_key[curr]] += 1
            for nxt in tree[curr]:
                if nxt != prev:
                    accum += explore(nxt, curr)
            count_map[node_key[curr]] -= 1
            return accum

        return explore(0, -1)
