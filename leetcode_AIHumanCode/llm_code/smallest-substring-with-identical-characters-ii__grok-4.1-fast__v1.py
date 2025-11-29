class Solution:
    def minLength(self, s: str, numOps: int) -> int:
        def compute_run_lengths(st):
            if not st:
                return []
            lengths = []
            current_length = 1
            for idx in range(1, len(st)):
                if st[idx] == st[idx - 1]:
                    current_length += 1
                else:
                    lengths.append(current_length)
                    current_length = 1
            lengths.append(current_length)
            return lengths
        
        run_lens = compute_run_lengths(s)
        str_len = len(s)
        
        def feasible(k):
            if k == 1:
                mismatch_count = sum(1 for i in range(str_len) if int(s[i]) != (i % 2))
                return min(mismatch_count, str_len - mismatch_count) <= numOps
            ops_req = sum(ln // (k + 1) for ln in run_lens)
            return ops_req <= numOps
        
        left_bound = 1
        right_bound = str_len
        while left_bound <= right_bound:
            middle = left_bound + (right_bound - left_bound) // 2
            if feasible(middle):
                right_bound = middle - 1
            else:
                left_bound = middle + 1
        return left_bound
