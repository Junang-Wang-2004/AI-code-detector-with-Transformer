class Solution:
    def minimumString(self, a, b, c):
        def combine(x, y):
            if x in y:
                return y
            ov = min(len(x), len(y))
            for k in range(ov, 0, -1):
                if x[-k:] == y[:k]:
                    return x + y[k:]
            return x + y

        options = []
        for seq in [[a, b, c], [a, c, b], [b, a, c], [b, c, a], [c, a, b], [c, b, a]]:
            partial = combine(seq[0], seq[1])
            total = combine(partial, seq[2])
            options.append(total)
        return min(options, key=lambda s: (len(s), s))
