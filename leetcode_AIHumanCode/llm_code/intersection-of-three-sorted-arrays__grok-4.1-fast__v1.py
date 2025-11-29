class Solution:
    def arraysIntersection(self, arr1, arr2, arr3):
        res = []
        p, q, r = 0, 0, 0
        while p < len(arr1) and q < len(arr2) and r < len(arr3):
            if arr1[p] == arr2[q] == arr3[r]:
                res.append(arr1[p])
                p += 1
                q += 1
                r += 1
            else:
                mn = min(arr1[p], arr2[q], arr3[r])
                if arr1[p] == mn:
                    p += 1
                if arr2[q] == mn:
                    q += 1
                if arr3[r] == mn:
                    r += 1
        return res
