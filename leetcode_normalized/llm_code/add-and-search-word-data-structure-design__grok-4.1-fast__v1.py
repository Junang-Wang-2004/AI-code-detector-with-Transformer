class C1:

    def __init__(self):
        self.root = {}

    def addWord(self, a1):
        v1 = self.root
        for v2 in a1:
            if v2 not in v1:
                v1[v2] = {}
            v1 = v1[v2]
        v1['end'] = True

    def search(self, a1):
        v1 = [(0, self.root)]
        while v1:
            v2, v3 = v1.pop()
            if v2 == len(a1):
                return v3.get('end', False)
            v4 = a1[v2]
            if v4 == '.':
                for v5 in v3:
                    if v5 != 'end':
                        v1.append((v2 + 1, v3[v5]))
            elif v4 in v3:
                v1.append((v2 + 1, v3[v4]))
        return False
