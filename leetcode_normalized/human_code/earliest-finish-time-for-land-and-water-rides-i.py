class C1(object):

    def earliestFinishTime(self, a1, a2, a3, a4):
        """
        """
        v1 = min((a1[i] + a2[i] for v2 in range(len(a1))))
        v3 = min((a3[v2] + a4[v2] for v2 in range(len(a3))))
        return min(min((max(a1[v2], v3) + a2[v2] for v2 in range(len(a1)))), min((max(a3[v2], v1) + a4[v2] for v2 in range(len(a3)))))
