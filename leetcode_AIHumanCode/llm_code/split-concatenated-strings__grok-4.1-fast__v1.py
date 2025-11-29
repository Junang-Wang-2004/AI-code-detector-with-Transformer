class Solution(object):
    def splitLoopedString(self, strs):
        opts = [max(s, s[::-1]) for s in strs]
        ring = ''.join(opts)
        length = len(ring)
        best = "a"
        offsets = [0]
        for s in strs:
            offsets.append(offsets[-1] + len(s))
        count = len(strs)
        for pos in range(count):
            start = offsets[pos]
            finish = offsets[pos + 1]
            tail = ring[finish:] + ring[:start]
            size = finish - start
            piece = strs[pos]
            for variant in (piece, piece[::-1]):
                for cut in range(size):
                    if variant[cut] >= best[0]:
                        trial = variant[cut:] + tail + variant[:cut]
                        best = max(best, trial)
        return best
