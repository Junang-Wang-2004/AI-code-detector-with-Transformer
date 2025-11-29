class Solution(object):
    def uniqueXorTriplets(self, nums):
        if not nums:
            return 0
        mx = 0
        for num in nums:
            if num > mx:
                mx = num
        bits = mx.bit_length()
        N = 1 << bits
        arr = [0] * N
        for num in nums:
            arr[num] += 1

        def fwht(f, inv):
            for b in range(bits):
                for i in range(N):
                    if (i & (1 << b)) == 0:
                        j = i | (1 << b)
                        u = f[i]
                        v = f[j]
                        f[i] = u + v
                        f[j] = u - v
            if inv:
                inv_n = N
                for i in range(N):
                    f[i] //= inv_n

        fwht(arr)
        for i in range(N):
            arr[i] = arr[i] * arr[i] * arr[i]
        fwht(arr, True)
        return sum(1 for x in arr if x != 0)
