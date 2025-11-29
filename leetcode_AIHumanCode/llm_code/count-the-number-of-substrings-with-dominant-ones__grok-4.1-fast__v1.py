class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        zero_pos = [-1]
        for i in range(n):
            if s[i] == '0':
                zero_pos.append(i)
        zero_pos.append(n)
        num_zeros = len(zero_pos) - 2
        answer = 0

        # Count substrings with zero '0's (all '1's segments)
        for j in range(len(zero_pos) - 1):
            seg_beg = zero_pos[j] + 1
            seg_end = zero_pos[j + 1] - 1
            seg_len = seg_end - seg_beg + 1
            if seg_len > 0:
                answer += seg_len * (seg_len + 1) // 2

        # Find max possible c
        max_c = 0
        while max_c * (max_c + 1) <= n:
            max_c += 1
        max_c -= 1

        # Count for each c >= 1
        for c in range(1, min(num_zeros, max_c) + 1):
            min_len = c * c + c
            k = min_len - 1
            for grp_start in range(1, num_zeros - c + 2):
                left_beg = zero_pos[grp_start - 1] + 1
                left_end = zero_pos[grp_start]
                right_beg = zero_pos[grp_start + c - 1]
                right_end = zero_pos[grp_start + c] - 1
                num_left = left_end - left_beg + 1
                num_right = right_end - right_beg + 1
                if num_left <= 0 or num_right <= 0:
                    continue

                # Full contributions where st + k <= right_beg
                split_pt = right_beg - k
                full_end = min(left_end, split_pt)
                full_beg = left_beg
                num_full = max(0, full_end - full_beg + 1)
                answer += num_full * num_right

                # Partial contributions
                part_beg = max(left_beg, split_pt + 1)
                part_end = left_end
                if part_beg <= part_end:
                    m_val = right_end - k + 1
                    to_st = min(part_end, m_val)
                    if to_st >= part_beg:
                        terms = to_st - part_beg + 1
                        f_term = m_val - part_beg
                        l_term = m_val - to_st
                        answer += terms * (f_term + l_term) // 2

        return answer
