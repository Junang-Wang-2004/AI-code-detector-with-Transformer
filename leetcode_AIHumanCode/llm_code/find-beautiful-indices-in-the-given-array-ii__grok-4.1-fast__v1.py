class Solution:
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> list[int]:
        def extract_starts(needle: str) -> list[int]:
            starts = []
            pos = 0
            while True:
                pos = s.find(needle, pos)
                if pos < 0:
                    break
                starts.append(pos)
                pos += 1
            return starts

        a_starts = extract_starts(a)
        b_starts = extract_starts(b)
        outcome = []
        cursor = 0
        for start_a in a_starts:
            while cursor < len(b_starts) and b_starts[cursor] < start_a - k:
                cursor += 1
            if cursor < len(b_starts) and b_starts[cursor] <= start_a + k:
                outcome.append(start_a)
        return outcome
