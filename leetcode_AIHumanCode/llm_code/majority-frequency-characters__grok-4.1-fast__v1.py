import collections

class Solution:
    def majorityFrequencyGroup(self, s):
        freq = {}
        order = []
        for ch in s:
            if ch not in freq:
                order.append(ch)
            freq[ch] = freq.get(ch, 0) + 1
        freq_cnt = collections.Counter(freq.values())
        best_cnt = -1
        best_f = -1
        for f, cnt in freq_cnt.items():
            if cnt > best_cnt or (cnt == best_cnt and f > best_f):
                best_cnt = cnt
                best_f = f
        res = [ch for ch in order if freq[ch] == best_f]
        return "".join(res)
