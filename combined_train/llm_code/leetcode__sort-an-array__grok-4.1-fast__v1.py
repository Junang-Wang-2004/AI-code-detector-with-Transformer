class C1:

    def sortArray(self, a1):

        def push_down(a1, a2):
            v1 = 2 * a1 + 1
            while v1 <= a2:
                if v1 + 1 <= a2 and a1[v1 + 1] > a1[v1]:
                    v1 += 1
                if a1[a1] < a1[v1]:
                    a1[a1], a1[v1] = (a1[v1], a1[a1])
                    a1 = v1
                    v1 = 2 * a1 + 1
                else:
                    break
        v1 = len(a1)
        for v2 in range(v1 // 2 - 1, -1, -1):
            push_down(v2, v1 - 1)
        for v2 in range(v1 - 1, 0, -1):
            a1[0], a1[v2] = (a1[v2], a1[0])
            push_down(0, v2 - 1)
        return a1
