class Solution(object):
    def duplicateZeros(self, arr):
        n = len(arr)
        offset = 0
        for i in range(n):
            if i + offset >= n:
                last = i - 1
                break
            if arr[i] == 0:
                offset += 1
        else:
            last = n - 1
        while last >= 0:
            if last + offset < n:
                arr[last + offset] = arr[last]
            if arr[last] == 0:
                offset -= 1
                arr[last + offset] = arr[last]
            last -= 1
