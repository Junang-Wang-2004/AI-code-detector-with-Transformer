class C1:

    def canBeValid(self, a1: str, a2: str) -> bool:
        v1 = len(a1)
        if v1 % 2 != 0:
            return False

        def check_forward():
            v1 = 0
            v2 = 0
            for v3 in range(v1):
                if a2[v3] == '0':
                    v2 += 1
                elif a1[v3] == '(':
                    v1 += 1
                else:
                    v1 -= 1
                if v1 + v2 < 0:
                    return False
            return True

        def check_backward():
            v1 = 0
            v2 = 0
            for v3 in range(v1 - 1, -1, -1):
                if a2[v3] == '0':
                    v2 += 1
                elif a1[v3] == ')':
                    v1 += 1
                else:
                    v1 -= 1
                if v1 + v2 < 0:
                    return False
            return True
        return check_forward() and check_backward()
