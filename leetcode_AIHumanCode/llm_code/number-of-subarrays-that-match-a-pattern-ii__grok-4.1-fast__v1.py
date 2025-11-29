class Solution:
    def countMatchingSubarrays(self, nums, pattern):
        seq_len = len(nums) - 1
        pat_len = len(pattern)
        if seq_len < pat_len:
            return 0
        seq = [0] * seq_len
        for idx in range(seq_len):
            delta = nums[idx + 1] - nums[idx]
            seq[idx] = 1 if delta > 0 else -1 if delta < 0 else 0
        
        lps = [0] * pat_len
        match_len = 0
        pos = 1
        while pos < pat_len:
            if pattern[pos] == pattern[match_len]:
                match_len += 1
                lps[pos] = match_len
                pos += 1
            else:
                if match_len != 0:
                    match_len = lps[match_len - 1]
                else:
                    lps[pos] = 0
                    pos += 1
        
        count = 0
        q = 0
        i = 0
        while i < seq_len:
            while q > 0 and seq[i] != pattern[q]:
                q = lps[q - 1]
            if seq[i] == pattern[q]:
                q += 1
            if q == pat_len:
                count += 1
                q = lps[q - 1]
            i += 1
        return count
