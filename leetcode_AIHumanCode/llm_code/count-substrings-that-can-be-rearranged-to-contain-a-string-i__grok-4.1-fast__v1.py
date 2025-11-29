class Solution:
    def validSubstringCount(self, word1, word2):
        n = len(word1)
        req = [0] * 26
        for ch in word2:
            req[ord(ch) - ord('a')] += 1
        num_req = sum(v > 0 for v in req)
        window = [0] * 26
        match = 0
        r = 0
        total = 0
        for l in range(n):
            while r < n and match < num_req:
                i = ord(word1[r]) - ord('a')
                prev = window[i]
                window[i] += 1
                if req[i] > 0 and prev < req[i] <= window[i]:
                    match += 1
                r += 1
            if match == num_req:
                end = max(l, r - 1)
                total += n - end
            i = ord(word1[l]) - ord('a')
            prev = window[i]
            window[i] -= 1
            if req[i] > 0 and prev == req[i]:
                match -= 1
        return total
