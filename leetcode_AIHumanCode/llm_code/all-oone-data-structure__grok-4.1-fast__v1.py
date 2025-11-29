class Bucket:
    def __init__(self, val=0):
        self.val = val
        self.key_set = set()
        self.prev_b = None
        self.next_b = None


class AllOne:
    def __init__(self):
        self.key_to_bucket = {}
        self.sentinel_min = Bucket(-1)
        self.sentinel_max = Bucket(float('inf'))
        self.sentinel_min.next_b = self.sentinel_max
        self.sentinel_max.prev_b = self.sentinel_min

    def _insert_before(self, pos, node):
        node.prev_b = pos.prev_b
        node.next_b = pos
        pos.prev_b.next_b = node
        pos.prev_b = node

    def _unlink(self, node):
        node.prev_b.next_b = node.next_b
        node.next_b.prev_b = node.prev_b

    def _get_first(self):
        return self.sentinel_min.next_b

    def _get_last(self):
        return self.sentinel_max.prev_b

    def _is_empty(self):
        return self.sentinel_min.next_b == self.sentinel_max

    def inc(self, key):
        if key not in self.key_to_bucket:
            temp_bucket = Bucket(0)
            temp_bucket.key_set.add(key)
            self._insert_before(self._get_first(), temp_bucket)
            self.key_to_bucket[key] = temp_bucket

        curr_bucket = self.key_to_bucket[key]
        next_bucket = curr_bucket.next_b
        if next_bucket == self.sentinel_max or next_bucket.val > curr_bucket.val + 1:
            next_bucket = Bucket(curr_bucket.val + 1)
            self._insert_before(curr_bucket.next_b, next_bucket)
        next_bucket.key_set.add(key)
        self.key_to_bucket[key] = next_bucket

        curr_bucket.key_set.remove(key)
        if not curr_bucket.key_set:
            self._unlink(curr_bucket)

    def dec(self, key):
        if key not in self.key_to_bucket:
            return
        curr_bucket = self.key_to_bucket.pop(key)
        if curr_bucket.val > 1:
            prev_bucket = curr_bucket.prev_b
            if prev_bucket == self.sentinel_min or prev_bucket.val < curr_bucket.val - 1:
                prev_bucket = Bucket(curr_bucket.val - 1)
                self._insert_before(curr_bucket, prev_bucket)
            prev_bucket.key_set.add(key)
            self.key_to_bucket[key] = prev_bucket

        curr_bucket.key_set.remove(key)
        if not curr_bucket.key_set:
            self._unlink(curr_bucket)

    def getMaxKey(self):
        if self._is_empty():
            return ""
        return next(iter(self._get_last().key_set))

    def getMinKey(self):
        if self._is_empty():
            return ""
        return next(iter(self._get_first().key_set))
