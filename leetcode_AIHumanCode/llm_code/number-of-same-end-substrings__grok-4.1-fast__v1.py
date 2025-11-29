class Solution:
    def sameEndSubstringCount(self, s, queries):
        length = len(s)
        counts = [[0] * (length + 1) for _ in range(26)]
        for pos, ch in enumerate(s):
            idx = ord(ch) - ord('a')
            for alpha in range(26):
                counts[alpha][pos + 1] = counts[alpha][pos]
            counts[idx][pos + 1] += 1
        output = []
        for start, end in queries:
            subtotal = 0
            for alpha in range(26):
                occurrences = counts[alpha][end + 1] - counts[alpha][start]
                subtotal += occurrences * (occurrences + 1) // 2
            output.append(subtotal)
        return output
