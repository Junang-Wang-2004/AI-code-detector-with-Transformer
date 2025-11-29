class Solution:
    def minAbbreviation(self, target, dictionary):
        def compute_length(s, mask):
            res = 0
            skips = 0
            for i in range(len(s)):
                if mask & (1 << i):
                    if skips:
                        res += len(str(skips))
                    skips = 0
                    res += 1
                else:
                    skips += 1
            if skips:
                res += len(str(skips))
            return res

        def construct_abbr(s, mask):
            pieces = []
            skips = 0
            for i in range(len(s)):
                if mask & (1 << i):
                    if skips:
                        pieces.append(str(skips))
                    skips = 0
                    pieces.append(s[i])
                else:
                    skips += 1
            if skips:
                pieces.append(str(skips))
            return ''.join(pieces)

        length = len(target)
        mismatch_masks = [
            sum((1 << j) for j in range(length) if target[j] != entry[j])
            for entry in dictionary if len(entry) == length
        ]
        complete_mask = (1 << length) - 1
        shortest = length
        optimal_mask = complete_mask
        for candidate in range(1 << length):
            if all((candidate & diff) != 0 for diff in mismatch_masks):
                this_length = compute_length(target, candidate)
                if this_length < shortest:
                    shortest = this_length
                    optimal_mask = candidate
        return construct_abbr(target, optimal_mask)
