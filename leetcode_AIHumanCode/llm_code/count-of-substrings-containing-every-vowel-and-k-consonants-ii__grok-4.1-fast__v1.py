class Solution:
    def countOfSubstrings(self, s, k):
        def num_with_all_vowels_ge_cons(m):
            n = len(s)
            vowel_cnt = [0] * 26
            distinct_vowels = 0
            num_cons = 0
            ans = 0
            j = 0
            is_vowel = set('aeiou')
            for i in range(n):
                c_idx = ord(s[i]) - ord('a')
                if s[i] in is_vowel:
                    if vowel_cnt[c_idx] == 0:
                        distinct_vowels += 1
                    vowel_cnt[c_idx] += 1
                else:
                    num_cons += 1
                while distinct_vowels == 5 and num_cons >= m:
                    ans += n - i
                    l_idx = ord(s[j]) - ord('a')
                    if s[j] in is_vowel:
                        vowel_cnt[l_idx] -= 1
                        if vowel_cnt[l_idx] == 0:
                            distinct_vowels -= 1
                    else:
                        num_cons -= 1
                    j += 1
            return ans
        
        return num_with_all_vowels_ge_cons(k) - num_with_all_vowels_ge_cons(k + 1)
