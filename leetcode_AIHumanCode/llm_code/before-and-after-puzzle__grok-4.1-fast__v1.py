import collections

class Solution:
    def beforeAndAfterPuzzles(self, phrases):
        ends = collections.defaultdict(list)
        for idx, text in enumerate(phrases):
            parts = text.split()
            if parts:
                ends[parts[-1]].append(idx)
        combos = set()
        for i, text in enumerate(phrases):
            parts = text.split()
            if not parts:
                continue
            begin = parts[0]
            suffix = ' '.join(parts[1:])
            gap = ' ' if suffix else ''
            for prior in ends[begin]:
                if prior == i:
                    continue
                combos.add(phrases[prior] + gap + suffix)
        return sorted(combos)
