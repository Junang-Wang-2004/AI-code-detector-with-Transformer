class Solution(object):
    def getMinSwaps(self, num, k):
        arr = list(num)
        length = len(arr)
        for _ in range(k):
            pivot = length - 2
            while pivot >= 0 and arr[pivot] >= arr[pivot + 1]:
                pivot -= 1
            if pivot >= 0:
                succ = length - 1
                while arr[succ] <= arr[pivot]:
                    succ -= 1
                arr[pivot], arr[succ] = arr[succ], arr[pivot]
                lo, hi = pivot + 1, length - 1
                while lo < hi:
                    arr[lo], arr[hi] = arr[hi], arr[lo]
                    lo += 1
                    hi -= 1
        goal = arr[:]
        curr = list(num)
        total = 0
        for idx in range(length):
            if curr[idx] == goal[idx]:
                continue
            tgt_pos = idx
            while curr[tgt_pos] != goal[idx]:
                tgt_pos += 1
            total += tgt_pos - idx
            for shift in range(tgt_pos, idx, -1):
                curr[shift], curr[shift - 1] = curr[shift - 1], curr[shift]
        return total
