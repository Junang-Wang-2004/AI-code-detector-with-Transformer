class C1:

    def interpret(self, a1):
        v1 = []
        v2 = 0
        v3 = len(a1)
        while v2 < v3:
            if a1[v2] == 'G':
                v1.append('G')
                v2 += 1
            elif a1[v2:v2 + 2] == '()':
                v1.append('o')
                v2 += 2
            elif a1[v2:v2 + 4] == '(al)':
                v1.append('al')
                v2 += 4
        return ''.join(v1)
