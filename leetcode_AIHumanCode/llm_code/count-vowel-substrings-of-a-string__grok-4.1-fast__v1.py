class Solution:
    def countVowelSubstrings(self, word):
        vmap = {'a': 0, 'e': 1, 'i': 2, 'o': 3, 'u': 4}
        
        def subs_with_at_most(d):
            freq = [0] * 5
            uniques = 0
            l = 0
            cnt = 0
            for r in range(len(word)):
                if word[r] not in vmap:
                    freq = [0] * 5
                    uniques = 0
                    l = r + 1
                    continue
                i = vmap[word[r]]
                if freq[i] == 0:
                    uniques += 1
                freq[i] += 1
                while uniques > d and l <= r:
                    j = vmap[word[l]]
                    freq[j] -= 1
                    if freq[j] == 0:
                        uniques -= 1
                    l += 1
                cnt += r - l + 1
            return cnt
        
        return subs_with_at_most(5) - subs_with_at_most(4)
