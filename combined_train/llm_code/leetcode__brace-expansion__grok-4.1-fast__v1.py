class C1:

    def expand(self, a1: str) -> list[str]:

        def get_combinations(a1: list[list[str]]) -> list[str]:
            if not a1:
                return ['']
            v1 = []
            v2 = 1
            for v3 in a1:
                v2 *= len(v3)
            for v4 in range(v2):
                v5 = []
                v6 = v4
                for v7 in reversed(a1):
                    v8, v6 = divmod(v6, len(v7))
                    v5.append(v7[v8])
                v1.append(''.join(reversed(v5)))
            v1.sort()
            return v1

        def parse_sequence(a1: int) -> tuple[list[list[str]], int]:
            v1: list[list[str]] = []
            v2 = a1
            while v2 < len(a1) and a1[v2] not in ',}':
                if a1[v2] == '{':
                    v3, v2 = parse_group(v2)
                    v1.append(v3)
                else:
                    v1.append([a1[v2]])
                    v2 += 1
            return (v1, v2)

        def parse_group(a1: int) -> tuple[list[str], int]:
            v1 = a1 + 1
            v2: set[str] = set()
            while v1 < len(a1) and a1[v1] != '}':
                v3, v1 = parse_sequence(v1)
                v4 = get_combinations(v3)
                v2.update(v4)
                if v1 < len(a1) and a1[v1] == ',':
                    v1 += 1
            v1 += 1
            return (sorted(v2), v1)
        v1, v2 = parse_sequence(0)
        return get_combinations(v1)
