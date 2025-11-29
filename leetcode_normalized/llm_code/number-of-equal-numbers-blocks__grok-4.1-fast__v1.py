class C1:

    def at(self, a1):
        pass

    def size(self):
        pass

class C2:

    def countBlocks(self, a1):
        v1 = 0
        v2 = 0
        v3 = a1.size()
        while v2 < v3:
            v4 = a1.at(v2)
            v5 = v2
            v6 = v3 - 1
            while v5 <= v6:
                v7 = (v5 + v6) // 2
                if a1.at(v7) == v4:
                    v5 = v7 + 1
                else:
                    v6 = v7 - 1
            v8 = v6
            v2 = v8 + 1
            v1 += 1
        return v1
