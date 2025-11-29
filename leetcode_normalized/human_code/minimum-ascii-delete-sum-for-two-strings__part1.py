class C1(object):

    def minimumDeleteSum(self, a1, a2):
        """
        """
        v1 = [[0] * (len(a2) + 1) for v2 in range(2)]
        for v3 in range(len(a2)):
            v1[0][v3 + 1] = v1[0][v3] + ord(a2[v3])
        for v4 in range(len(a1)):
            v1[(v4 + 1) % 2][0] = v1[v4 % 2][0] + ord(a1[v4])
            for v3 in range(len(a2)):
                if a1[v4] == a2[v3]:
                    v1[(v4 + 1) % 2][v3 + 1] = v1[v4 % 2][v3]
                else:
                    v1[(v4 + 1) % 2][v3 + 1] = min(v1[v4 % 2][v3 + 1] + ord(a1[v4]), v1[(v4 + 1) % 2][v3] + ord(a2[v3]))
        return v1[len(a1) % 2][-1]
