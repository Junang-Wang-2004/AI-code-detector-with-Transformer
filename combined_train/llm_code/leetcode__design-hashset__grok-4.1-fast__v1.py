class C1:

    def __init__(self):
        self.capacity = 10007
        self.buckets = [[] for v1 in range(self.capacity)]

    def add(self, a1: int) -> None:
        v1 = a1 % self.capacity
        v2 = self.buckets[v1]
        if a1 not in v2:
            v2.append(a1)

    def remove(self, a1: int) -> None:
        v1 = a1 % self.capacity
        v2 = self.buckets[v1]
        for v3 in range(len(v2)):
            if v2[v3] == a1:
                del v2[v3]
                return

    def contains(self, a1: int) -> bool:
        v1 = a1 % self.capacity
        v2 = self.buckets[v1]
        return a1 in v2
