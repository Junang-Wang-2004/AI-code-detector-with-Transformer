import collections

class Solution:
    def beautifulNumbers(self, l, r):
        def count(n):
            if n < 0:
                return 0
            digits = [int(ch) for ch in str(n)]
            states = {(1, 1, 0): 1}
            for i in range(len(digits)):
                lim = digits[i]
                next_states = collections.defaultdict(int)
                for (is_tight, prod, suma), count in states.items():
                    max_d = lim if is_tight else 9
                    for d in range(max_d + 1):
                        ntight = 1 if is_tight and d == lim else 0
                        nprod = prod * (1 if suma == 0 and d == 0 else d)
                        nsuma = suma + d
                        next_states[(ntight, nprod, nsuma)] += count
                states = next_states
            total = 0
            for (is_tight, prod, suma), count in states.items():
                if suma > 0 and prod % suma == 0:
                    total += count
            return total

        return count(r) - count(l - 1)
