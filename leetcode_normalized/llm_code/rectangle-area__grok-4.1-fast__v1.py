class C1(object):

    def computeArea(self, a1, a2, a3, a4, a5, a6, a7, a8):
        v1, v2, v3, v4 = (a1, a3, a2, a4)
        v5, v6, v7, v8 = (a5, a7, a6, a8)
        v9 = (v2 - v1) * (v4 - v3)
        v10 = (v6 - v5) * (v8 - v7)
        v11 = max(v1, v5)
        v12 = min(v2, v6)
        v13 = max(v3, v7)
        v14 = min(v4, v8)
        v15 = max(0, v12 - v11)
        v16 = max(0, v14 - v13)
        return v9 + v10 - v15 * v16
