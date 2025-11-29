class C1(object):

    def reconstructQueue(self, a1):
        """
        """
        a1.sort(key=lambda h_k1: (-h_k1[0], h_k1[1]))
        v1 = []
        for v2 in a1:
            v1.insert(v2[1], v2)
        return v1
