class Solution:
    def constructDistancedSequence(self, n):
        m = 2 * n - 1
        arr = [0] * m
        taken = set()

        def search(idx):
            if idx == m:
                return True
            if arr[idx] != 0:
                return search(idx + 1)
            for val in range(n, 0, -1):
                if val in taken:
                    continue
                nxt = idx + val
                if val > 1 and (nxt >= m or arr[nxt] != 0):
                    continue
                arr[idx] = val
                if val > 1:
                    arr[nxt] = val
                taken.add(val)
                if search(idx + 1):
                    return True
                arr[idx] = 0
                if val > 1:
                    arr[nxt] = 0
                taken.remove(val)
            return False

        search(0)
        return arr
