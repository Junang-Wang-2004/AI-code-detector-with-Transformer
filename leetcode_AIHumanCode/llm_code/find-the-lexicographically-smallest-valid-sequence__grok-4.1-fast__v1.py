class Solution(object):
    def validSequence(self, word1, word2):
        n, m = len(word1), len(word2)
        suf_pos = [-1] * m
        tgt = m - 1
        for idx in range(n - 1, -1, -1):
            if tgt >= 0 and word1[idx] == word2[tgt]:
                suf_pos[tgt] = idx
                tgt -= 1
        seq = []
        errs = 0
        for pos in range(n):
            if len(seq) == m:
                break
            slot = len(seq)
            char_match = word1[pos] == word2[slot]
            err_allowed = (errs == 0 and
                           (slot == m - 1 or suf_pos[slot + 1] > pos))
            if char_match or err_allowed:
                if not char_match:
                    errs += 1
                seq.append(pos)
        return seq if len(seq) == m else []
