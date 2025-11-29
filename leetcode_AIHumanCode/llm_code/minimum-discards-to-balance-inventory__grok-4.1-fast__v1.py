class Solution:
    def minArrivalsToDiscard(self, arrivals, w, m):
        freq = {}
        discards = 0
        n = len(arrivals)
        for i in range(n):
            t = arrivals[i]
            freq[t] = freq.get(t, 0) + 1
            if freq[t] > m:
                freq[t] -= 1
                arrivals[i] = -1
                discards += 1
            l = i - w + 1
            if l >= 0:
                lt = arrivals[l]
                if lt != -1:
                    freq[lt] -= 1
                    if freq[lt] == 0:
                        del freq[lt]
        return discards
