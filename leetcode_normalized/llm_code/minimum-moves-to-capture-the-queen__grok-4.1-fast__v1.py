class C1(object):

    def minMovesToCaptureTheQueen(self, a1, a2, a3, a4, a5, a6):
        v1 = a1 == a5
        v2 = a3 == a1
        v3 = (a2 - a4) * (a6 - a4) < 0
        v4 = v1 and (not (v2 and v3))
        v5 = a2 == a6
        v6 = a4 == a2
        v7 = (a1 - a3) * (a5 - a3) < 0
        v8 = v5 and (not (v6 and v7))
        v9 = a3 + a4 == a5 + a6
        v10 = a1 + a2 == a3 + a4
        v11 = (a3 - a1) * (a5 - a1) < 0
        v12 = v9 and (not (v10 and v11))
        v13 = a3 - a4 == a5 - a6
        v14 = a1 - a2 == a3 - a4
        v15 = (a4 - a2) * (a6 - a2) < 0
        v16 = v13 and (not (v14 and v15))
        if v4 or v8 or v12 or v16:
            return 1
        return 2
