class Solution(object):
    def countOfSubstrings(self, word, k):
        vowel_set = set('aeiou')
        FULL = 5
        def at_least(m):
            n = len(word)
            freq = [0] * 26
            num_cons = 0
            num_distinct = 0
            total = 0
            start = 0
            for end in range(n):
                i = ord(word[end]) - ord('a')
                if word[end] in vowel_set:
                    if freq[i] == 0:
                        num_distinct += 1
                    freq[i] += 1
                else:
                    num_cons += 1
                while num_distinct == FULL and num_cons >= m:
                    total += n - end
                    j = ord(word[start]) - ord('a')
                    if word[start] in vowel_set:
                        freq[j] -= 1
                        if freq[j] == 0:
                            num_distinct -= 1
                    else:
                        num_cons -= 1
                    start += 1
            return total
        return at_least(k) - at_least(k + 1)
