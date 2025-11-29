class C1(object):

    def deserialize(self, a1):

        def parse(a1):
            if a1[a1] != '[':
                v1 = a1
                while v1 < len(a1) and a1[v1].isdigit():
                    v1 += 1
                return (NestedInteger(int(a1[a1:v1])), v1)
            v2 = NestedInteger()
            a1 += 1
            while a1 < len(a1) and a1[a1] != ']':
                v4, a1 = parse(a1)
                v2.add(v4)
                if a1 < len(a1) and a1[a1] == ',':
                    a1 += 1
            a1 += 1
            return (v2, a1)
        if not a1:
            return NestedInteger()
        v1, v2 = parse(0)
        return v1
