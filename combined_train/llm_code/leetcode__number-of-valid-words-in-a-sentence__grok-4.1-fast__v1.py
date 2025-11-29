class C1:

    def countValidWords(self, a1):

        def is_valid(a1):
            if not a1:
                return False
            v1 = len(a1)
            v2 = False
            for v3 in range(v1):
                v4 = a1[v3]
                if v4.isdigit():
                    return False
                if v4 == '-':
                    if v2 or v3 == 0 or v3 == v1 - 1 or (not (a1[v3 - 1].isalpha() and a1[v3 + 1].isalpha())):
                        return False
                    v2 = True
                elif v4 in '!,.':
                    if v3 != v1 - 1:
                        return False
                elif not v4.isalpha():
                    return False
            return True
        return sum((1 for v1 in a1.split() if is_valid(v1)))
