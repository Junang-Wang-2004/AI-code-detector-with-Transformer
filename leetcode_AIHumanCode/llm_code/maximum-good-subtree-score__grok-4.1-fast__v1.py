class Solution:
    def goodSubtreeSum(self, vals, par):
        MOD = 10**9 + 7
        n = len(vals)
        tree = [[] for _ in range(n)]
        for i in range(1, n):
            tree[par[i]].append(i)
        total = [0]

        def get_digits(num):
            bits = 0
            while num:
                dig, num = divmod(num, 10)
                if bits & (1 << dig):
                    return -1
                bits |= (1 << dig)
            return bits

        def process(u):
            states = {0: 0}
            m = get_digits(vals[u])
            if m != -1:
                states[m] = vals[u]
            for v in tree[u]:
                sub_states = process(v)
                updated = states.copy()
                for s1_mask, s1_val in states.items():
                    for s2_mask, s2_val in sub_states.items():
                        if s1_mask & s2_mask == 0:
                            combined_mask = s1_mask | s2_mask
                            combined_val = s1_val + s2_val
                            if combined_mask not in updated or updated[combined_mask] < combined_val:
                                updated[combined_mask] = combined_val
                states = updated
            total[0] = (total[0] + max(states.values())) % MOD
            return states

        process(0)
        return total[0]
