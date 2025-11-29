class Solution:
    def findLUSlength(self, strs):
        result = -1
        num_strings = len(strs)
        for first in range(num_strings):
            pattern = strs[first]
            pat_len = len(pattern)
            is_special = True
            for second in range(num_strings):
                if first == second:
                    continue
                target = strs[second]
                if len(target) < pat_len:
                    continue
                match_idx = 0
                for char in target:
                    if match_idx < pat_len and char == pattern[match_idx]:
                        match_idx += 1
                if match_idx == pat_len:
                    is_special = False
                    break
            if is_special:
                result = max(result, pat_len)
        return result
