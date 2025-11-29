class C1(object):

    def numDecodings(self, a1):
        """
        """
        v1, v2 = (1000000007, 3)
        v3 = [0] * v2
        v3[0] = 1
        v3[1] = 9 if a1[0] == '*' else v3[0] if a1[0] != '0' else 0
        for v4 in range(1, len(a1)):
            if a1[v4] == '*':
                v3[(v4 + 1) % v2] = 9 * v3[v4 % v2]
                if a1[v4 - 1] == '1':
                    v3[(v4 + 1) % v2] = (v3[(v4 + 1) % v2] + 9 * v3[(v4 - 1) % v2]) % v1
                elif a1[v4 - 1] == '2':
                    v3[(v4 + 1) % v2] = (v3[(v4 + 1) % v2] + 6 * v3[(v4 - 1) % v2]) % v1
                elif a1[v4 - 1] == '*':
                    v3[(v4 + 1) % v2] = (v3[(v4 + 1) % v2] + 15 * v3[(v4 - 1) % v2]) % v1
            else:
                v3[(v4 + 1) % v2] = v3[v4 % v2] if a1[v4] != '0' else 0
                if a1[v4 - 1] == '1':
                    v3[(v4 + 1) % v2] = (v3[(v4 + 1) % v2] + v3[(v4 - 1) % v2]) % v1
                elif a1[v4 - 1] == '2' and a1[v4] <= '6':
                    v3[(v4 + 1) % v2] = (v3[(v4 + 1) % v2] + v3[(v4 - 1) % v2]) % v1
                elif a1[v4 - 1] == '*':
                    v3[(v4 + 1) % v2] = (v3[(v4 + 1) % v2] + (2 if a1[v4] <= '6' else 1) * v3[(v4 - 1) % v2]) % v1
        return v3[len(a1) % v2]
