class C1(object):

    def validateCoupons(self, a1, a2, a3):
        v1 = ['electronics', 'grocery', 'pharmacy', 'restaurant']
        v2 = []
        v3 = len(a1)
        for v4 in range(v3):
            v5 = a1[v4]
            v6 = a2[v4]
            v7 = a3[v4]
            if v7 and v5 and (v6 in v1) and all((char.isalnum() or char == '_' for v8 in v5)):
                v9 = v1.index(v6)
                v2.append((v9, v5))
        v2.sort()
        return [item[1] for v10 in v2]
