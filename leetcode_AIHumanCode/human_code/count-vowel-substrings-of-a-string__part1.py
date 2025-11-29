# Time:  O(n)
# Space: O(1)

import collections


class Solution(object):
    def countVowelSubstrings(self, word):
        """
        """
        VOWELS = set("aeiou")
        k = 5
        def atLeastK(word, k):
            cnt = collections.Counter()
            result = left = right = 0
            for i, c in enumerate(word):
                if c not in VOWELS:
                    cnt = collections.Counter()
                    left = right = i+1
                    continue
                cnt[c] += 1
                while len(cnt) > k-1:
                    cnt[word[right]] -= 1
                    if not cnt[word[right]]:
                        del cnt[word[right]]
                    right += 1
                result += right-left
            return result

        return atLeastK(word, k)


