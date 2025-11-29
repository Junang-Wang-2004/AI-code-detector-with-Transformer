# Time:  O(n + 26 * log(26))
# Space: O(26)
# freq table, sort, two pointers
class Solution2(object):
    def minimumDeletions(self, word, k):
        """
        """
        cnt = [0]*26
        for x in word:
            cnt[ord(x)-ord('a')] += 1
        arr = sorted(x for x in cnt if x)
        result = float("inf")
        right = prefix = 0
        suffix = len(word)
        prev = -1
        for left in range(len(arr)):
            if left+1 < len(arr) and arr[left+1] == arr[left]:
                continue
            while right < len(arr) and arr[right] <= arr[left]+k:
                suffix -= arr[right]
                right += 1
            result = min(result, prefix+(suffix-(arr[left]+k)*(len(arr)-right)))
            prefix += arr[left]*(left-prev)
            prev = left
        return result


