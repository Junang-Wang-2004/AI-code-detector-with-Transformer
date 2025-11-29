class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        MOD = 10**9 + 7
        ways = [[0] * rollMax[i] for i in range(6)]
        for i in range(6):
            if rollMax[i] > 0:
                ways[i][0] = 1
        for _ in range(n - 1):
            face_totals = [sum(ways[i]) % MOD for i in range(6)]
            overall = sum(face_totals) % MOD
            fresh_ways = [[0] * rollMax[i] for i in range(6)]
            for j in range(6):
                incoming = (overall - face_totals[j] + MOD) % MOD
                fresh_ways[j][0] = incoming
                for s in range(1, rollMax[j]):
                    fresh_ways[j][s] = ways[j][s - 1]
            ways = fresh_ways
        return sum(sum(row) for row in ways) % MOD
