class Solution:
    def maxDotProduct(self, seq1, seq2):
        if len(seq1) < len(seq2):
            seq1, seq2 = seq2, seq1
        rows = len(seq1)
        cols = len(seq2)
        previous = [0] * cols
        for x in range(rows):
            current = [0] * cols
            for y in range(cols):
                product = seq1[x] * seq2[y]
                extra = 0
                if x > 0 and y > 0:
                    extra = max(previous[y - 1], 0)
                option = product + extra
                current[y] = option
                if x > 0:
                    current[y] = max(current[y], previous[y])
                if y > 0:
                    current[y] = max(current[y], current[y - 1])
            previous = current
        return previous[-1]
