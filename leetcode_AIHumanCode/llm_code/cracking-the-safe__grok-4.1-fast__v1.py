class Solution:
    def crackSafe(self, n: int, k: int) -> str:
        target = k ** n
        marks = set()
        seq = [str(k - 1)] * (n - 1)
        while len(marks) < target:
            tail = ''.join(seq[-(n - 1):])
            for num in range(k):
                trial = tail + str(num)
                if trial not in marks:
                    marks.add(trial)
                    seq.append(str(num))
                    break
        return ''.join(seq)
