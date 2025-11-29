class Solution:
    def nextGreaterElement(self, n):
        arr = [int(c) for c in str(n)]
        length = len(arr)
        pivot = -1
        for i in range(length - 2, -1, -1):
            if arr[i] < arr[i + 1]:
                pivot = i
                break
        if pivot == -1:
            return -1
        successor = -1
        for j in range(length - 1, pivot, -1):
            if arr[j] > arr[pivot]:
                successor = j
                break
        arr[pivot], arr[successor] = arr[successor], arr[pivot]
        arr[pivot + 1:] = reversed(arr[pivot + 1:])
        num = 0
        for d in arr:
            num = num * 10 + d
        return num if num <= 2147483647 else -1
