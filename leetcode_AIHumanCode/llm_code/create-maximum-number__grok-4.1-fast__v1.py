class Solution:
    def maxNumber(self, nums1, nums2, k):
        def pick_best(digits, size):
            stack = []
            drops = len(digits) - size
            for d in digits:
                while stack and drops and stack[-1] < d:
                    stack.pop()
                    drops -= 1
                stack.append(d)
            return stack[:size]

        def merge_max(first, second):
            result = []
            i = j = 0
            while i < len(first) and j < len(second):
                if first[i:] > second[j:]:
                    result.append(first[i])
                    i += 1
                else:
                    result.append(second[j])
                    j += 1
            result += first[i:]
            result += second[j:]
            return result

        m, n = len(nums1), len(nums2)
        largest = []
        for cnt1 in range(max(0, k - n), min(k, m) + 1):
            cnt2 = k - cnt1
            candidate = merge_max(pick_best(nums1, cnt1), pick_best(nums2, cnt2))
            if candidate > largest:
                largest = candidate
        return largest
