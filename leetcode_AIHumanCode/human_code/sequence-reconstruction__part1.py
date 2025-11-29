# Time:  O(n * s), n is the size of org, s is the size of seqs
# Space: O(n)

import collections


class Solution(object):
    def sequenceReconstruction(self, org, seqs):
        """
        """
        if not seqs:
            return False
        pos = [0] * (len(org) + 1)
        for i in range(len(org)):
            pos[org[i]] = i

        is_matched = [False] * (len(org) + 1)
        cnt_to_match = len(org) - 1
        for seq in seqs:
            for i in range(len(seq)):
                if not 0 < seq[i] <= len(org):
                    return False
                if i == 0:
                    continue
                if pos[seq[i-1]] >= pos[seq[i]]:
                    return False
                if is_matched[seq[i-1]] == False and pos[seq[i-1]] + 1 == pos[seq[i]]:
                    is_matched[seq[i-1]] = True
                    cnt_to_match -= 1

        return cnt_to_match == 0


