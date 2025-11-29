class Solution:
    def longestPalindrome(self, words):
        freq = {}
        for w in words:
            freq[w] = freq.get(w, 0) + 1
        
        length = 0
        can_center = False
        
        for w in freq:
            rev = w[::-1]
            if w == rev:
                length += (freq[w] // 2) * 4
                if freq[w] % 2:
                    can_center = True
        
        seen = set()
        for w in freq:
            if w in seen or w == w[::-1]:
                continue
            rev = w[::-1]
            if rev in freq:
                num_pairs = min(freq[w], freq[rev])
                length += num_pairs * 4
                seen.add(w)
                seen.add(rev)
        
        if can_center:
            length += 2
        return length
