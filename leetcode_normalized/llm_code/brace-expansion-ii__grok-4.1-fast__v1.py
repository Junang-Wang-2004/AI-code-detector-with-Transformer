class C1:

    def braceExpansionII(self, a1: str) -> list[str]:

        def compute_combinations(a1):
            if not a1:
                return []
            v1 = [len(p) for v2 in a1]
            v3 = 1
            for v4 in v1:
                v3 *= v4
            v5 = []
            for v6 in range(v3):
                v7 = []
                v8 = v6
                for v9 in range(len(a1) - 1, -1, -1):
                    v7.append(a1[v9][v8 % v1[v9]])
                    v8 //= v1[v9]
                v7.reverse()
                v5.append(''.join(v7))
            v5.sort()
            return v5

        def parse_sequence(a1, a2):
            v1 = []
            while a2 < len(a1) and a1[a2] not in ',}':
                if a1[a2] == '{':
                    v2, a2 = parse_brace(a1, a2)
                    v1.append(v2)
                elif a1[a2].isalnum():
                    v1.append([a1[a2]])
                    a2 += 1
                else:
                    a2 += 1
            return (compute_combinations(v1), a2)

        def parse_brace(a1, a2):
            a2 += 1
            v2 = set()
            while a2 < len(a1) and a1[a2] != '}':
                v3, a2 = parse_sequence(a1, a2)
                v2.update(v3)
                if a2 < len(a1) and a1[a2] == ',':
                    a2 += 1
            a2 += 1
            return (sorted(v2), a2)
        return parse_sequence(a1, 0)[0]
