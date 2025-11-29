import collections

class Solution(object):
    def longestDupSubstring(self, s):
        n = len(s)
        if n < 2:
            return ""
        mod = 1000000009
        base = 29
        pows = [1] * (n + 1)
        for i in range(1, n + 1):
            pows[i] = pows[i - 1] * base % mod
        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = (pref[i] * base + ord(s[i]) - ord('a')) % mod
        def find_pos(length):
            hash_map = collections.defaultdict(list)
            for i in range(n - length + 1):
                h = (pref[i + length] - pref[i] * pows[length] % mod + mod) % mod
                for j in hash_map[h]:
                    if s[j:j + length] == s[i:i + length]:
                        return j
                hash_map[h].append(i)
            return -1
        left = 1
        right = n - 1
        while left <= right:
            mid = left + (right - left) // 2
            if find_pos(mid) != -1:
                left = mid + 1
            else:
                right = mid - 1
        max_len = right
        pos = find_pos(max_len)
        return s[pos:pos + max_len]
