from collections import Counter

class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:
        vowels = set('aeiou')
        n = len(s)
        cum = [0] * (n + 1)
        for idx in range(n):
            cum[idx + 1] = cum[idx] + (1 if s[idx] in vowels else -1)
        
        mod_val = 1
        rem = k
        exp_two = 0
        while rem % 2 == 0:
            exp_two += 1
            rem //= 2
        if exp_two > 0:
            mod_val *= 2 ** ((exp_two + 1) // 2 + 1)
        
        factor = 3
        while factor * factor <= rem:
            exp = 0
            while rem % factor == 0:
                exp += 1
                rem //= factor
            if exp > 0:
                mod_val *= factor ** ((exp + 1) // 2)
            factor += 2
        if rem > 1:
            mod_val *= rem ** ((1 + 1) // 2)
        
        freq_map = Counter()
        answer = 0
        for pos in range(n + 1):
            pair = (cum[pos], pos % mod_val)
            answer += freq_map[pair]
            freq_map[pair] += 1
        return answer
