class Solution:
    def beautifulIndices(self, s, a, b, k):
        def compute_failure(pattern):
            n = len(pattern)
            failure = [0] * n
            match_len = 0
            pos = 1
            while pos < n:
                if pattern[pos] == pattern[match_len]:
                    match_len += 1
                    failure[pos] = match_len
                    pos += 1
                else:
                    if match_len > 0:
                        match_len = failure[match_len - 1]
                    else:
                        failure[pos] = 0
                        pos += 1
            return failure

        def extract_starts(haystack, needle):
            starts = []
            if len(needle) > len(haystack):
                return starts
            failure = compute_failure(needle)
            state = 0
            for idx in range(len(haystack)):
                while state > 0 and needle[state] != haystack[idx]:
                    state = failure[state - 1]
                if needle[state] == haystack[idx]:
                    state += 1
                if state == len(needle):
                    starts.append(idx - len(needle) + 1)
                    state = failure[state - 1]
            return starts

        indices_a = extract_starts(s, a)
        indices_b = extract_starts(s, b)
        ans = []
        ptr = 0
        for start_a in indices_a:
            while ptr < len(indices_b) and indices_b[ptr] < start_a - k:
                ptr += 1
            if ptr < len(indices_b) and indices_b[ptr] <= start_a + k:
                ans.append(start_a)
        return ans
