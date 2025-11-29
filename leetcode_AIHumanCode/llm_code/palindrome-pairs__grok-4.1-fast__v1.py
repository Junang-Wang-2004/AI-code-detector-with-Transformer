from collections import defaultdict

class Solution:
    def palindromePairs(self, words):
        idx_by_word = defaultdict(list)
        for idx, word in enumerate(words):
            idx_by_word[word].append(idx)

        def check_palindrome(st):
            l, r = 0, len(st) - 1
            while l < r:
                if st[l] != st[r]:
                    return False
                l += 1
                r -= 1
            return True

        ans = []
        for i in range(len(words)):
            curr = words[i]
            length = len(curr)
            # words[i] + words[j] where prefix reverse matches words[j], suffix pal
            for p_len in range(length + 1):
                prefix_part = curr[:p_len]
                suffix_part = curr[p_len:]
                if check_palindrome(suffix_part):
                    rev_prefix = prefix_part[::-1]
                    for jdx in idx_by_word[rev_prefix]:
                        if jdx != i:
                            ans.append([i, jdx])
            # words[j] + words[i] where suffix reverse matches words[j], prefix pal
            # skip p_len=0 to avoid duplicate with symmetric case1
            for p_len in range(1, length + 1):
                prefix_part = curr[:p_len]
                suffix_part = curr[p_len:]
                if check_palindrome(prefix_part):
                    rev_suffix = suffix_part[::-1]
                    for jdx in idx_by_word[rev_suffix]:
                        if jdx != i:
                            ans.append([jdx, i])
        return ans
