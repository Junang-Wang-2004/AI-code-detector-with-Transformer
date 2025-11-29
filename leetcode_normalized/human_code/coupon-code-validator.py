import itertools

class C1(object):

    def validateCoupons(self, a1, a2, a3):
        """
        """
        v1 = {'electronics': 0, 'grocery': 1, 'pharmacy': 2, 'restaurant': 3}
        v2 = []
        for v3, v4, v5 in zip(a1, a2, a3):
            if v5 and v3 and (v4 in v1) and all((x.isalnum() or x == '_' for v6 in v3)):
                v2.append((v1[v4], v3))
        v2.sort()
        return [v3 for v7, v3 in v2]
