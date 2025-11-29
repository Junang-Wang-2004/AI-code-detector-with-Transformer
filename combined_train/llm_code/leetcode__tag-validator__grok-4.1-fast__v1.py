class C1:

    def isValid(self, a1):
        v1 = len(a1)
        v2 = []

        def get_tag(a1):
            if a1 >= v1 or a1[a1] != '<':
                return (None, a1)
            v1 = a1.find('>', a1 + 1)
            if v1 == -1 or v1 - a1 - 1 < 1 or v1 - a1 - 1 > 9:
                return (None, a1)
            v2 = a1[a1 + 1:v1]
            if not all(('A' <= c <= 'Z' for v3 in v2)):
                return (None, a1)
            return (v2, v1 + 1)

        def chk_close(a1, a2):
            v1 = len(a2)
            v2 = a1 + v1 + 3
            if v2 > v1 or a1[a1:a1 + 2] != '</' or a1[a1 + 2:a1 + 2 + v1] != a2 or (a1[a1 + 2 + v1] != '>'):
                return (False, a1)
            return (True, v2)
        v3 = 0
        v4, v3 = get_tag(v3)
        if v4 is None:
            return False
        v2.append(v4)
        while v3 < v1:
            if a1[v3] == '<':
                if v3 + 9 <= v1 and a1[v3:v3 + 9] == '<![CDATA[':
                    v5 = a1.find(']]>', v3 + 9)
                    if v5 == -1:
                        return False
                    v3 = v5 + 3
                    continue
                if v3 + 1 < v1 and a1[v3 + 1] == '/':
                    v6, v7 = chk_close(v3, v2[-1])
                    if not v6:
                        return False
                    v3 = v7
                    v2.pop()
                    if not v2:
                        return v3 == v1
                else:
                    v4, v7 = get_tag(v3)
                    if v4 is None:
                        return False
                    v3 = v7
                    v2.append(v4)
            else:
                v8 = a1.find('<', v3)
                v3 = v1 if v8 == -1 else v8
        return False
