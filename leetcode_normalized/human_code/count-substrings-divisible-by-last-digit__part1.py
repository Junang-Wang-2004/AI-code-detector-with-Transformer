class C1(object):

    def countSubstrings(self, a1):
        """
        """
        v1 = 0
        for v2 in range(len(a1)):
            if a1[v2] in ('1', '2', '5'):
                v1 += v2 + 1
        v3 = 0
        v4 = [0] * 3
        v4[0] = 1
        for v2 in range(len(a1)):
            v3 = (v3 + (ord(a1[v2]) - ord('0'))) % 3
            if a1[v2] in ('3', '6'):
                v1 += v4[v3]
            v4[v3] += 1
        v3 = 0
        v4 = [0] * 9
        v4[0] = 1
        for v2 in range(len(a1)):
            v3 = (v3 + (ord(a1[v2]) - ord('0'))) % 9
            if a1[v2] == '9':
                v1 += v4[v3]
            v4[v3] += 1
        for v2 in range(len(a1)):
            if a1[v2] == '4':
                v1 += 1
                if v2 - 1 >= 0 and int(a1[v2 - 1:v2 + 1]) % 4 == 0:
                    v1 += v2
        for v2 in range(len(a1)):
            if a1[v2] == '8':
                v1 += 1
                if v2 - 1 >= 0 and int(a1[v2 - 1:v2 + 1]) % 8 == 0:
                    v1 += 1
                if v2 - 2 >= 0 and int(a1[v2 - 2:v2 + 1]) % 8 == 0:
                    v1 += v2 - 1
        v5 = 1
        v3 = 0
        v4 = [0] * 7
        for v2 in range(len(a1)):
            v3 = (v3 + v5 * (ord(a1[~v2]) - ord('0'))) % 7
            v1 += v4[v3]
            if a1[~v2] == '7':
                v1 += 1
                v4[v3] += 1
            v5 = v5 * 10 % 7
        return v1
