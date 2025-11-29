class C1(object):

    def reconstructQueue(self, a1):
        """
        """
        a1.sort(key=lambda h_k: (-h_k[0], h_k[1]))
        v1 = [[]]
        for v2 in a1:
            v3 = v2[1]
            for v4, v5 in enumerate(v1):
                if v3 <= len(v5):
                    break
                v3 -= len(v5)
            v5.insert(v3, v2)
            if len(v5) * len(v5) > len(a1):
                v1.insert(v4 + 1, v5[len(v5) / 2:])
                del v5[len(v5) / 2:]
        return [v2 for v5 in v1 for v2 in v5]
