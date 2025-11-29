class C1:

    def __init__(self, a1=0):
        self.val = a1
        self.key_set = set()
        self.prev_b = None
        self.next_b = None

class C2:

    def __init__(self):
        self.key_to_bucket = {}
        self.sentinel_min = C1(-1)
        self.sentinel_max = C1(float('inf'))
        self.sentinel_min.next_b = self.sentinel_max
        self.sentinel_max.prev_b = self.sentinel_min

    def _insert_before(self, a1, a2):
        a2.prev_b = a1.prev_b
        a2.next_b = a1
        a1.prev_b.next_b = a2
        a1.prev_b = a2

    def _unlink(self, a1):
        a1.prev_b.next_b = a1.next_b
        a1.next_b.prev_b = a1.prev_b

    def _get_first(self):
        return self.sentinel_min.next_b

    def _get_last(self):
        return self.sentinel_max.prev_b

    def _is_empty(self):
        return self.sentinel_min.next_b == self.sentinel_max

    def inc(self, a1):
        if a1 not in self.key_to_bucket:
            v1 = C1(0)
            v1.key_set.add(a1)
            self._insert_before(self._get_first(), v1)
            self.key_to_bucket[a1] = v1
        v2 = self.key_to_bucket[a1]
        v3 = v2.next_b
        if v3 == self.sentinel_max or v3.val > v2.val + 1:
            v3 = C1(v2.val + 1)
            self._insert_before(v2.next_b, v3)
        v3.key_set.add(a1)
        self.key_to_bucket[a1] = v3
        v2.key_set.remove(a1)
        if not v2.key_set:
            self._unlink(v2)

    def dec(self, a1):
        if a1 not in self.key_to_bucket:
            return
        v1 = self.key_to_bucket.pop(a1)
        if v1.val > 1:
            v2 = v1.prev_b
            if v2 == self.sentinel_min or v2.val < v1.val - 1:
                v2 = C1(v1.val - 1)
                self._insert_before(v1, v2)
            v2.key_set.add(a1)
            self.key_to_bucket[a1] = v2
        v1.key_set.remove(a1)
        if not v1.key_set:
            self._unlink(v1)

    def getMaxKey(self):
        if self._is_empty():
            return ''
        return next(iter(self._get_last().key_set))

    def getMinKey(self):
        if self._is_empty():
            return ''
        return next(iter(self._get_first().key_set))
