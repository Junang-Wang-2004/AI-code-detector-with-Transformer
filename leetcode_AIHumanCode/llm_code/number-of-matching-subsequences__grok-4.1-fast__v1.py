import collections

class Solution(object):
    def numMatchingSubseq(self, S, words):
        wait = collections.defaultdict(list)
        result = 0
        for idx, seq in enumerate(words):
            if seq:
                wait[seq[0]].append((idx, 0))
            else:
                result += 1
        for ch in S:
            current = wait[ch]
            wait[ch] = []
            for idx, ptr in current:
                nxt_ptr = ptr + 1
                if nxt_ptr == len(words[idx]):
                    result += 1
                else:
                    nxt_ch = words[idx][nxt_ptr]
                    wait[nxt_ch].append((idx, nxt_ptr))
        return result
