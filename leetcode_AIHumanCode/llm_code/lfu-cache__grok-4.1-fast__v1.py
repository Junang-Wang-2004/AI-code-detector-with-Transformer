import collections

class LFUCache:
    def __init__(self, capacity):
        self._maxsz = capacity
        self._valmap = {}
        self._freqmap = {}
        self._freqmap_to_keys = collections.defaultdict(collections.OrderedDict)
        self._lowfreq = float('inf')
        self._currsz = 0

    def _evict(self, ky):
        fr = self._freqmap[ky]
        del self._freqmap_to_keys[fr][ky]
        if len(self._freqmap_to_keys[fr]) == 0:
            del self._freqmap_to_keys[fr]
            if fr == self._lowfreq:
                self._lowfreq += 1
        del self._freqmap[ky]
        del self._valmap[ky]
        self._currsz -= 1

    def _bumpfreq(self, ky):
        prevfr = self._freqmap.get(ky, 0)
        if prevfr > 0:
            del self._freqmap_to_keys[prevfr][ky]
            if len(self._freqmap_to_keys[prevfr]) == 0:
                del self._freqmap_to_keys[prevfr]
                if prevfr == self._lowfreq:
                    self._lowfreq += 1
        nxtfr = prevfr + 1
        self._freqmap[ky] = nxtfr
        self._freqmap_to_keys[nxtfr][ky] = None
        self._lowfreq = min(self._lowfreq, nxtfr)

    def get(self, ky):
        if ky not in self._valmap:
            return -1
        self._bumpfreq(ky)
        return self._valmap[ky]

    def put(self, ky, vl):
        if self._maxsz <= 0:
            return
        self._valmap[ky] = vl
        if ky in self._freqmap:
            self._bumpfreq(ky)
        else:
            if self._currsz == self._maxsz:
                rmky = next(iter(self._freqmap_to_keys[self._lowfreq]))
                self._evict(rmky)
            self._bumpfreq(ky)
            self._currsz += 1
