class Solution(object):
    def minAnagramLength(self, s):
        total_len = len(s)
        candidates = []
        sqrt_n = int(total_len ** 0.5) + 1
        for i in range(1, sqrt_n):
            if total_len % i == 0:
                candidates.append(i)
                quotient = total_len // i
                if i != quotient:
                    candidates.append(quotient)
        candidates.sort()
        
        def char_counts(start_pos, seg_size):
            frequencies = [0] * 26
            for pos in range(start_pos, start_pos + seg_size):
                frequencies[ord(s[pos]) - ord('a')] += 1
            return frequencies
        
        def segments_match(seg_length):
            base_count = char_counts(0, seg_length)
            next_start = seg_length
            while next_start < total_len:
                if char_counts(next_start, seg_length) != base_count:
                    return False
                next_start += seg_length
            return True
        
        for possible_len in candidates:
            if segments_match(possible_len):
                return possible_len
