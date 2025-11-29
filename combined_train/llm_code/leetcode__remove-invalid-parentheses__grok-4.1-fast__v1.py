class C1:

    def removeInvalidParentheses(self, a1):

        def is_valid(a1):
            v1 = 0
            for v2 in a1:
                if v2 == '(':
                    v1 += 1
                elif v2 == ')':
                    v1 -= 1
                if v1 < 0:
                    return False
            return v1 == 0
        from collections import deque
        v1 = deque([a1])
        v2 = {a1}
        while v1:
            v3 = len(v1)
            v4 = []
            for v5 in range(v3):
                v6 = v1.popleft()
                if is_valid(v6):
                    v4.append(v6)
                    continue
                for v7 in range(len(v6)):
                    if v6[v7] not in '()':
                        continue
                    if v7 > 0 and v6[v7] == v6[v7 - 1]:
                        continue
                    v8 = v6[:v7] + v6[v7 + 1:]
                    if v8 not in v2:
                        v2.add(v8)
                        v1.append(v8)
            if v4:
                return v4
        return []
