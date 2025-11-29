class Solution:
    def maxSubstringLength(self, s: str, k: int) -> bool:
        length = len(s)
        appear_first = [-1] * 26
        appear_last = [-1] * 26
        for position in range(length):
            char_id = ord(s[position]) - ord('a')
            if appear_first[char_id] == -1:
                appear_first[char_id] = position
            appear_last[char_id] = position
        candidates = []
        starts = [appear_first[i] for i in range(26) if appear_first[i] != -1]
        for begin in starts:
            char_id = ord(s[begin]) - ord('a')
            finish = appear_last[char_id]
            scan = begin + 1
            while scan <= finish and appear_first[ord(s[scan]) - ord('a')] >= begin:
                finish = max(finish, appear_last[ord(s[scan]) - ord('a')])
                scan += 1
            if scan == finish + 1 and (begin != 0 or finish != length - 1):
                candidates.append((begin, finish))
        candidates.sort(key=lambda interval: interval[1])
        overlaps_removed = 0
        prior_finish = float('-inf')
        for start_pos, end_pos in candidates:
            if start_pos <= prior_finish:
                overlaps_removed += 1
            else:
                prior_finish = end_pos
        max_count = len(candidates) - overlaps_removed
        return max_count >= k
