class Solution:
    def simulationResult(self, windows, queries):
        seen = set()
        output = []
        for idx in range(len(queries) - 1, -1, -1):
            val = queries[idx]
            if val not in seen:
                seen.add(val)
                output.append(val)
        for elem in windows:
            if elem not in seen:
                output.append(elem)
        return output
