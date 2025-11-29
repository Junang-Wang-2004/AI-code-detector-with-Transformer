class Solution:
    def expand(self, s: str) -> list[str]:
        def get_combinations(parts: list[list[str]]) -> list[str]:
            if not parts:
                return ['']
            combos = []
            prod_size = 1
            for part in parts:
                prod_size *= len(part)
            for num in range(prod_size):
                current = []
                remainder = num
                for group in reversed(parts):
                    index, remainder = divmod(remainder, len(group))
                    current.append(group[index])
                combos.append(''.join(reversed(current)))
            combos.sort()
            return combos

        def parse_sequence(pos: int) -> tuple[list[list[str]], int]:
            segments: list[list[str]] = []
            i = pos
            while i < len(s) and s[i] not in ',}':
                if s[i] == '{':
                    opts, i = parse_group(i)
                    segments.append(opts)
                else:
                    segments.append([s[i]])
                    i += 1
            return segments, i

        def parse_group(pos: int) -> tuple[list[str], int]:
            i = pos + 1
            alt_set: set[str] = set()
            while i < len(s) and s[i] != '}':
                segs, i = parse_sequence(i)
                alt_expansions = get_combinations(segs)
                alt_set.update(alt_expansions)
                if i < len(s) and s[i] == ',':
                    i += 1
            i += 1
            return sorted(alt_set), i

        parts, _ = parse_sequence(0)
        return get_combinations(parts)
