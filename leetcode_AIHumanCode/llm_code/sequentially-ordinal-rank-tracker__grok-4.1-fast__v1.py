import heapq

class SORTracker:
    def __init__(self):
        self.top = []
        self.bottom = []
        self.idx = 0
        self.tick = 0

    def _reverse_str(self, s):
        return ''.join(chr(ord('a') + ord('z') - ord(c)) for c in s)

    def add(self, name, score):
        self.tick += 1
        rname = self._reverse_str(name)
        top_key = (score, rname, self.tick)
        bot_key = (-score, name, self.tick)
        go_top = True
        if self.top:
            ws, wrn, _ = self.top[0]
            wname = self._reverse_str(wrn)
            wkey = (-ws, wname)
            nkey = (-score, name)
            go_top = nkey <= wkey
        if go_top:
            heapq.heappush(self.top, top_key)
        else:
            heapq.heappush(self.bottom, bot_key)
        while len(self.top) > self.idx:
            ts, trn, tt = heapq.heappop(self.top)
            tname = self._reverse_str(trn)
            heapq.heappush(self.bottom, (-ts, tname, tt))

    def get(self):
        self.idx += 1
        while len(self.top) < self.idx and self.bottom:
            bs, bn, bt = heapq.heappop(self.bottom)
            brname = self._reverse_str(bn)
            heapq.heappush(self.top, (-bs, brname, bt))
        ts, trn, _ = self.top[0]
        return self._reverse_str(trn)
