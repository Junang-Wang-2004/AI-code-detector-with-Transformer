class CombinationIterator:
    def __init__(self, s, m):
        self.source = s
        self.size = len(s)
        self.want = m
        self.picks = list(range(m))
        self.finished = False

    def next(self):
        result = ''.join(self.source[idx] for idx in self.picks)
        pos = self.want - 1
        while pos >= 0 and self.picks[pos] == self.size - self.want + pos:
            pos -= 1
        if pos < 0:
            self.finished = True
        else:
            self.picks[pos] += 1
            for q in range(pos + 1, self.want):
                self.picks[q] = self.picks[q - 1] + 1
        return result

    def hasNext(self):
        return not self.finished
