import collections

class C1:

    def __init__(self, a1):
        self._maxsz = a1
        self._valmap = {}
        self._freqmap = {}
        self._freqmap_to_keys = collections.defaultdict(collections.OrderedDict)
        self._lowfreq = float('inf')
        self._currsz = 0

    def _evict(self, a1):
        v1 = self._freqmap[a1]
        del self._freqmap_to_keys[v1][a1]
        if len(self._freqmap_to_keys[v1]) == 0:
            del self._freqmap_to_keys[v1]
            if v1 == self._lowfreq:
                self._lowfreq += 1
        del self._freqmap[a1]
        del self._valmap[a1]
        self._currsz -= 1

    def _bumpfreq(self, a1):
        v1 = self._freqmap.get(a1, 0)
        if v1 > 0:
            del self._freqmap_to_keys[v1][a1]
            if len(self._freqmap_to_keys[v1]) == 0:
                del self._freqmap_to_keys[v1]
                if v1 == self._lowfreq:
                    self._lowfreq += 1
        v2 = v1 + 1
        self._freqmap[a1] = v2
        self._freqmap_to_keys[v2][a1] = None
        self._lowfreq = min(self._lowfreq, v2)

    def get(self, a1):
        if a1 not in self._valmap:
            return -1
        self._bumpfreq(a1)
        return self._valmap[a1]

    def put(self, a1, a2):
        if self._maxsz <= 0:
            return
        self._valmap[a1] = a2
        if a1 in self._freqmap:
            self._bumpfreq(a1)
        else:
            if self._currsz == self._maxsz:
                v1 = next(iter(self._freqmap_to_keys[self._lowfreq]))
                self._evict(v1)
            self._bumpfreq(a1)
            self._currsz += 1
