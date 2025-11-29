class Solution:
    def countMatchingSubarrays(self, nums, pattern):
        n = len(nums)
        if n == 0 or not pattern:
            return 0
        
        diffs = []
        for i in range(n - 1):
            if nums[i + 1] > nums[i]:
                diffs.append(1)
            elif nums[i + 1] < nums[i]:
                diffs.append(-1)
            else:
                diffs.append(0)
        
        def longest_prefix_suffix(pat):
            m = len(pat)
            lps = [0] * m
            len_prefix = 0
            i = 1
            while i < m:
                if pat[i] == pat[len_prefix]:
                    len_prefix += 1
                    lps[i] = len_prefix
                    i += 1
                else:
                    if len_prefix > 0:
                        len_prefix = lps[len_prefix - 1]
                    else:
                        lps[i] = 0
                        i += 1
            return lps
        
        def count_matches(txt, pat):
            m = len(pat)
            if m == 0:
                return len(txt) + 1
            lps = longest_prefix_suffix(pat)
            matches = 0
            i = 0
            j = 0
            while i < len(txt):
                if j < m and pat[j] == txt[i]:
                    i += 1
                    j += 1
                if j == m:
                    matches += 1
                    j = lps[j - 1]
                elif i < len(txt) and (j == 0 or pat[j] != txt[i]):
                    if j > 0:
                        j = lps[j - 1]
                    else:
                        i += 1
            return matches
        
        return count_matches(diffs, pattern)
