        # Time:  ctor:  O(NlogN) * O(fn)
        #        query: O(fn)
        # Space: O(NlogN)
        class SparseTable(object):
            def __init__(self, arr, fn):
                self.fn = fn
                self.bit_length = [0]
                n = len(arr)
                k = n.bit_length()-1  # log2_floor(n)
                for i in range(k+1):
                    self.bit_length.extend(i+1 for _ in range(min(1<<i, (n+1)-len(self.bit_length))))
                self.st = [[0]*n for _ in range(k+1)]
                self.st[0] = arr[:]
                for i in range(1, k+1):  # Time: O(NlogN) * O(fn)
                    for j in range((n-(1<<i))+1):
                        self.st[i][j] = fn(self.st[i-1][j], self.st[i-1][j+(1<<(i-1))])
        
            def query(self, L, R):  # Time: O(fn)
                i = self.bit_length[R-L+1]-1  # log2_floor(R-L+1)
                return self.fn(self.st[i][L], self.st[i][R-(1<<i)+1])
        
        prefix = [0]*(len(nums)+1)
        for i, x in enumerate(nums):
            prefix[i+1] = prefix[i]+x
        result = 0
        rmq = SparseTable(nums, gcd)
        for left, x in enumerate(nums):
            right = left
            while right < len(nums):  # O(logr) times
                g = rmq.query(left, right)
                right = binary_search_right(right, len(nums)-1, lambda x: rmq.query(left, x) >= g)  # Time: O(logn) * O(logr)
                if right-left+1 >= k:
                    result = max(result, (prefix[right+1]-prefix[left])*g)
                right += 1
        return result
