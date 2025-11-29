class Solution:
    def minStickers(self, stickers, target):
        n = len(target)
        A = ord('a')
        sticker_cnts = []
        for s in stickers:
            cnt = [0] * 26
            for ch in s:
                cnt[ord(ch) - A] += 1
            sticker_cnts.append(cnt)
        memo = [-1] * (1 << n)

        def dfs(uncover):
            if uncover == 0:
                return 0
            if memo[uncover] != -1:
                return memo[uncover]
            res = 999
            for cnt in sticker_cnts:
                temp_cnt = cnt[:]
                cover = 0
                for i in range(n):
                    if (uncover & (1 << i)) != 0:
                        idx = ord(target[i]) - A
                        if temp_cnt[idx] > 0:
                            temp_cnt[idx] -= 1
                            cover |= (1 << i)
                if cover != 0:
                    sub = dfs(uncover & ~cover)
                    if sub != -1:
                        res = min(res, sub + 1)
            memo[uncover] = -1 if res == 999 else res
            return memo[uncover]

        full_mask = (1 << n) - 1
        return dfs(full_mask)
