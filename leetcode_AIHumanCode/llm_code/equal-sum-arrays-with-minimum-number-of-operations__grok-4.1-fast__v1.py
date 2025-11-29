class Solution:
    def minOperations(self, arr1, arr2):
        n1, n2 = len(arr1), len(arr2)
        if n1 > 6 * n2 or n2 > 6 * n1:
            return -1
        total1 = sum(arr1)
        total2 = sum(arr2)
        if total1 > total2:
            arr1, arr2 = arr2, arr1
            total1, total2 = total2, total1
        gap = total2 - total1
        adjustments = []
        for val in arr1:
            adjustments.append(6 - val)
        for val in arr2:
            adjustments.append(val - 1)
        adjustments.sort(reverse=True)
        steps = 0
        for max_adj in adjustments:
            if gap <= 0:
                break
            if max_adj > 0:
                reduce_by = min(max_adj, gap)
                gap -= reduce_by
                steps += 1
        return steps
