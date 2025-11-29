class Solution:
    def minMovesToMakePalindrome(self, s: str) -> int:
        n = len(s)
        pos_lists = [[] for _ in range(26)]
        for i, ch in enumerate(s):
            pos_lists[ord(ch) - ord('a')].append(i)
        targets = [-1] * n
        pairs = []
        center_idx = n // 2
        for lst in pos_lists:
            sz = len(lst)
            for j in range(sz // 2):
                pairs.append((lst[j], lst[sz - 1 - j]))
            if sz % 2:
                targets[lst[sz // 2]] = center_idx
        pairs.sort(key=lambda x: x[0])
        np = len(pairs)
        for k in range(np):
            lft, rgt = pairs[k]
            targets[lft] = k
            targets[rgt] = n - 1 - k
        tree = [0] * (n + 2)
        def upd(idx, val):
            idx += 1
            while idx <= n:
                tree[idx] += val
                idx += idx & -idx
        def pref(idx):
            idx += 1
            res = 0
            while idx > 0:
                res += tree[idx]
                idx -= idx & -idx
            return res
        moves = 0
        for tgt in targets:
            moves += pref(n - 1) - pref(tgt)
            upd(tgt, 1)
        return moves
