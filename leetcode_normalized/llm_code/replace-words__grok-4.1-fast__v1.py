class C1:

    def __init__(self):
        self.children = {}
        self.is_end = False

class C2:

    def replaceWords(self, a1, a2):
        v1 = C1()
        for v2 in a1:
            v3 = v1
            for v4 in v2:
                if v4 not in v3.children:
                    v3.children[v4] = C1()
                v3 = v3.children[v4]
            v3.is_end = True

        def shorten(a1):
            v1 = v1
            v2 = []
            for v3 in a1:
                if v3 not in v1.children:
                    break
                v1 = v1.children[v3]
                v2.append(v3)
                if v1.is_end:
                    return ''.join(v2)
            return a1
        v5 = a2.split()
        return ' '.join((shorten(part) for v6 in v5))
