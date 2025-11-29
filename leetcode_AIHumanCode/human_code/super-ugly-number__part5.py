# Time:  O(n * logk) ~ O(n * klogk)
# Space: O(k^2)
# TLE due to the last test case, but it passess and performs well in C++.
class Solution5(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        """
        ugly_number = 0

        heap = []
        heapq.heappush(heap, 1)
        for p in primes:
            heapq.heappush(heap, p)
        for _ in range(n):
            ugly_number = heapq.heappop(heap)
            for i in range(len(primes)):
                if ugly_number % primes[i] == 0:
                    for j in range(i + 1):
                        heapq.heappush(heap, ugly_number * primes[j])
                    break

        return ugly_number

