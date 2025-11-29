class C1(object):

    def maxRepeating(self, a1, a2):
        if len(a1) < len(a2):
            return 0
        v1 = 0
        v2 = 0
        while True:
            v2 = a1.find(a2, v2)
            if v2 == -1:
                break
            v3 = 1
            v4 = v2 + len(a2)
            while v4 + len(a2) <= len(a1) and a1[v4:v4 + len(a2)] == a2:
                v3 += 1
                v4 += len(a2)
            v1 = max(v1, v3)
            v2 = v4
        return v1
