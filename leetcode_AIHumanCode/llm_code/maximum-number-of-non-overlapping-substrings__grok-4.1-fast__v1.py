class Solution:
    def maxNumOfSubstrings(self, s):
        n = len(s)
        first_occ = [n] * 26
        last_occ = [-1] * 26
        for i, ch in enumerate(s):
            idx = ord(ch) - ord('a')
            first_occ[idx] = min(first_occ[idx], i)
            last_occ[idx] = max(last_occ[idx], i)
        
        def compute_end(start):
            end = last_occ[ord(s[start]) - ord('a')]
            pos = start
            while pos <= end:
                cidx = ord(s[pos]) - ord('a')
                if first_occ[cidx] < start:
                    return -1
                end = max(end, last_occ[cidx])
                pos += 1
            return end
        
        valid_intervals = []
        for i in range(26):
            st = first_occ[i]
            if st < n:
                en = compute_end(st)
                if en != -1:
                    valid_intervals.append((en, st))
        
        valid_intervals.sort()
        result = []
        prev_end = -1
        for en, st in valid_intervals:
            if st > prev_end:
                result.append(s[st:en + 1])
                prev_end = en
        return result
