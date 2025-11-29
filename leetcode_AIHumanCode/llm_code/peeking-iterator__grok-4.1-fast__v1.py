class PeekingIterator:
    def __init__(self, iterator):
        self._iter = iterator
        self._buffer = None

    def peek(self):
        if self._buffer is None:
            self._buffer = next(self._iter)
        return self._buffer

    def next(self):
        val = self._buffer if self._buffer is not None else next(self._iter)
        self._buffer = None
        return val

    def hasNext(self):
        return self._buffer is not None or self._iter.hasNext()
