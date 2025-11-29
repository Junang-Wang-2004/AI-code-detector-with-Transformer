class C1(object):

    def __init__(self, a1):
        self.parent_arr = a1
        self.children_arr = [[] for v1 in range(len(a1))]
        self.owner = {}
        for v2, v3 in enumerate(a1):
            if v3 != -1:
                self.children_arr[v3].append(v2)

    def lock(self, a1, a2):
        if a1 in self.owner:
            return False
        self.owner[a1] = a2
        return True

    def unlock(self, a1, a2):
        if a1 not in self.owner or self.owner[a1] != a2:
            return False
        del self.owner[a1]
        return True

    def upgrade(self, a1, a2):
        v1 = a1
        while v1 != -1:
            if v1 in self.owner:
                return False
            v1 = self.parent_arr[v1]
        v2 = []
        v3 = [a1]
        while v3:
            v4 = v3.pop()
            if v4 in self.owner:
                v2.append(v4)
            for v5 in self.children_arr[v4]:
                v3.append(v5)
        if v2:
            for v6 in v2:
                del self.owner[v6]
            self.owner[a1] = a2
            return True
        return False
