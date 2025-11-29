class C1(object):

    def findLadders(self, a1, a2, a3):
        """
        """
        v1 = set(a3)
        v2, v3, v4, v5, v6 = ([], [a1], set([a1]), False, defaultdict(list))
        while v3 and (not v5):
            for v7 in v3:
                v4.add(v7)
            next = set()
            for v7 in v3:
                for v8 in range(len(v7)):
                    for v9 in ascii_lowercase:
                        v10 = v7[:v8] + v9 + v7[v8 + 1:]
                        if v10 not in v4 and v10 in v1:
                            if v10 == a2:
                                v5 = True
                            next.add(v10)
                            v6[v10].append(v7)
            v3 = next
        if v5:
            self.backtrack(v2, v6, [], a2)
        return v2

    def backtrack(self, a1, a2, a3, a4):
        if not a2[a4]:
            a3.append(a4)
            a1.append(a3[::-1])
            a3.pop()
        else:
            for v1 in a2[a4]:
                a3.append(a4)
                self.backtrack(a1, a2, a3, v1)
                a3.pop()
