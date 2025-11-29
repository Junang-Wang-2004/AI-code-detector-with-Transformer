class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        def compute_combinations(parts):
            if not parts:
                return []
            lengths = [len(p) for p in parts]
            total = 1
            for length in lengths:
                total *= length
            combos = []
            for num in range(total):
                current = []
                rem = num
                for k in range(len(parts) - 1, -1, -1):
                    current.append(parts[k][rem % lengths[k]])
                    rem //= lengths[k]
                current.reverse()
                combos.append(''.join(current))
            combos.sort()
            return combos

        def parse_sequence(s, pos):
            components = []
            while pos < len(s) and s[pos] not in ',}':
                if s[pos] == '{':
                    opts, pos = parse_brace(s, pos)
                    components.append(opts)
                elif s[pos].isalnum():
                    components.append([s[pos]])
                    pos += 1
                else:
                    pos += 1
            return compute_combinations(components), pos

        def parse_brace(s, pos):
            pos += 1
            uniq = set()
            while pos < len(s) and s[pos] != '}':
                subs, pos = parse_sequence(s, pos)
                uniq.update(subs)
                if pos < len(s) and s[pos] == ',':
                    pos += 1
            pos += 1
            return sorted(uniq), pos

        return parse_sequence(expression, 0)[0]
