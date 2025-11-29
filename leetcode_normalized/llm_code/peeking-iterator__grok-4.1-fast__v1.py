class C1:

    def __init__(self, a1):
        self._iter = a1
        self._buffer = None

    def peek(self):
        if self._buffer is None:
            self._buffer = next(self._iter)
        return self._buffer

    def next(self):
        v1 = self._buffer if self._buffer is not None else next(self._iter)
        self._buffer = None
        return v1

    def hasNext(self):
        return self._buffer is not None or self._iter.hasNext()
