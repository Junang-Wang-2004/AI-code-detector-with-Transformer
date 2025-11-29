class MyHashSet:

    def __init__(self):
        self.capacity = 10007
        self.buckets = [[] for _ in range(self.capacity)]

    def add(self, key: int) -> None:
        idx = key % self.capacity
        bucket = self.buckets[idx]
        if key not in bucket:
            bucket.append(key)

    def remove(self, key: int) -> None:
        idx = key % self.capacity
        bucket = self.buckets[idx]
        for i in range(len(bucket)):
            if bucket[i] == key:
                del bucket[i]
                return

    def contains(self, key: int) -> bool:
        idx = key % self.capacity
        bucket = self.buckets[idx]
        return key in bucket
