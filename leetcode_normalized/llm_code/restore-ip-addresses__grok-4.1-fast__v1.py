class C1:

    def restoreIpAddresses(self, a1):
        v1 = []

        def backtrack(a1, a2):
            if len(a2) == 4:
                if a1 == len(a1):
                    v1.append('.'.join(a2))
                return
            for v1 in range(a1 + 1, min(a1 + 4, len(a1) + 1)):
                v2 = a1[a1:v1]
                if v2[0] == '0' and len(v2) > 1 or int(v2) > 255:
                    continue
                a2.append(v2)
                backtrack(v1, a2)
                a2.pop()
        backtrack(0, [])
        return v1
