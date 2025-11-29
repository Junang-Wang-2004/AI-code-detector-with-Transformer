class Solution(object):
    def countCompleteSubstrings(self, word, k):
        n = len(word)
        answer = 0
        pos = 0
        while pos < n:
            start_seg = pos
            while pos < n - 1 and abs(ord(word[pos + 1]) - ord(word[pos])) <= 2:
                pos += 1
            end_seg = pos
            m = end_seg - start_seg + 1
            for distinct in range(1, 27):
                length = distinct * k
                if length > m:
                    break
                counts = [0] * 26
                perfect_count = 0
                l = start_seg
                for r in range(start_seg, end_seg + 1):
                    ch = ord(word[r]) - ord('a')
                    counts[ch] += 1
                    if counts[ch] == k:
                        perfect_count += 1
                    elif counts[ch] == k + 1:
                        perfect_count -= 1
                    while r - l + 1 > length:
                        chl = ord(word[l]) - ord('a')
                        if counts[chl] == k:
                            perfect_count -= 1
                        elif counts[chl] == k + 1:
                            perfect_count += 1
                        counts[chl] -= 1
                        l += 1
                    if r - l + 1 == length and perfect_count == distinct:
                        answer += 1
            pos += 1
        return answer
