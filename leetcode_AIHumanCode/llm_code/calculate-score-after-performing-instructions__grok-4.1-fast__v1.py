class Solution:
    def calculateScore(self, instructions, values):
        score = 0
        seen = set()
        idx = 0
        sz = len(instructions)
        while 0 <= idx < sz and idx not in seen:
            seen.add(idx)
            if instructions[idx] == "add":
                score += values[idx]
                idx += 1
            else:
                idx += values[idx]
        return score
