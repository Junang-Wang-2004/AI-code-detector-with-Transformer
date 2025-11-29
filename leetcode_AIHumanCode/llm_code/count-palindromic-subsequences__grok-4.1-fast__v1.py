class Solution(object):
    def countPalindromes(self, s):
        MOD = 10**9 + 7
        n = len(s)
        occurrences = [[] for _ in range(10)]
        for idx in range(n):
            occurrences[int(s[idx])].append(idx)
        total = 0
        for inner in range(10):
            px_list = occurrences[inner]
            px_len = len(px_list)
            if px_len < 2:
                continue
            for outer in range(10):
                py_list = occurrences[outer]
                py_len = len(py_list)
                before = [0] * px_len
                after = [0] * px_len
                py_ptr1 = 0
                for r in range(px_len):
                    while py_ptr1 < py_len and py_list[py_ptr1] < px_list[r]:
                        py_ptr1 += 1
                    before[r] = py_ptr1
                py_ptr2 = 0
                for r in range(px_len):
                    while py_ptr2 < py_len and py_list[py_ptr2] <= px_list[r]:
                        py_ptr2 += 1
                    after[r] = py_len - py_ptr2
                suffix_sums = [0] * (px_len + 1)
                for b in range(px_len - 1, -1, -1):
                    suffix_sums[b] = (suffix_sums[b + 1] + after[b]) % MOD
                for a in range(px_len - 1):
                    contrib = (before[a] * suffix_sums[a + 1]) % MOD
                    total = (total + contrib) % MOD
        return total
