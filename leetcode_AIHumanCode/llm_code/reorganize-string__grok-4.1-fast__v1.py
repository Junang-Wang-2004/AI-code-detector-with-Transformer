class Solution:
    def reorganizeString(self, s):
        n = len(s)
        freq = [0] * 26
        for ch in s:
            freq[ord(ch) - ord('a')] += 1
        if max(freq) > (n + 1) // 2:
            return ""
        result = []
        last = None
        for _ in range(n):
            max_cnt = -1
            idx = -1
            for i in range(26):
                c = chr(i + ord('a'))
                if freq[i] > max_cnt and (last is None or c != last):
                    max_cnt = freq[i]
                    idx = i
            ch = chr(idx + ord('a'))
            result.append(ch)
            freq[idx] -= 1
            last = ch
        return ''.join(result)
