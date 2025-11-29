class Solution:
    def threeSum(self, nums):
        ans = []
        arr = sorted(nums)
        length = len(arr)
        for p in range(length - 2):
            if p > 0 and arr[p] == arr[p - 1]:
                continue
            start = p + 1
            end = length - 1
            while start < end:
                total = arr[p] + arr[start] + arr[end]
                if total == 0:
                    ans.append([arr[p], arr[start], arr[end]])
                    start += 1
                    end -= 1
                    while start < end and arr[start] == arr[start - 1]:
                        start += 1
                    while start < end and arr[end] == arr[end + 1]:
                        end -= 1
                elif total < 0:
                    start += 1
                else:
                    end -= 1
        return ans
