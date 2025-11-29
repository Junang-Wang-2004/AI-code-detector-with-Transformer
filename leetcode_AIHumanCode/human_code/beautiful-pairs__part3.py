# Time:  O(nlogn)
# Space: O(n)
import itertools


# divide and conquer, merge sort, variant of closest pair
# reference: https://www.baeldung.com/cs/minimal-manhattan-distance
class Solution3(object):
    def beautifulPair(self, nums1, nums2):
        """
        """
        INF = float("inf")
        MAX_NEIGHBOR_COUNT = 8
        def dist(a, b):
            if a > b:
                a, b = b, a
            return [abs(points[a][0]-points[b][0])+abs(points[a][1]-points[b][1]), a, b]

        def merge_sort(left, right):
            if left == right:
                return
            mid = left + (right-left)//2
            x = points[order[mid]][0]  # added
            merge_sort(left, mid)
            merge_sort(mid+1, right)
            r = mid+1
            tmp = []
            for l in range(left, mid+1):
                while r <= right and points[order[r]][1] < points[order[l]][1]:  # modified
                    tmp.append(order[r])
                    r += 1
                tmp.append(order[l])
            order[left:left+len(tmp)] = tmp

            # added below
            stripe = [order[i] for i in range(left, right+1) if abs(points[order[i]][0]-x) <= result[0]]
            for i in range(len(stripe)-1):
                for j in range(i+1, len(stripe)):
                    x, y = stripe[i], stripe[j]
                    if points[y][1]-points[x][1] > result[0]:
                        break
                    result[:] = min(result, dist(x, y))
                else:
                    j = len(stripe)
                assert(j-(i+1) <= MAX_NEIGHBOR_COUNT)

        points = [(i, j) for i, j in zip(nums1, nums2)]
        result = [INF]*3
        lookup = {}
        for i in reversed(range(len(points))):
            if points[i] in lookup:
                result = [0, (i, lookup[points[i]])]
            lookup[points[i]] = i
        if result[0] == 0:
            return result[1]
        order = list(range(len(points)))
        order.sort(key=lambda x: points[x][0])
        merge_sort(0, len(points)-1)
        return result[1:]


