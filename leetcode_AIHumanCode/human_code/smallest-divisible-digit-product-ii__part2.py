# Time:  O(nlogt)
# Space: O(logt)
# freq table, greedy, prefix sum, number theory
class Solution2(object):
    def smallestNumber(self, num, t):
        """
        """
        def gcd(a, b):
            while b:
                a, b = b, a%b
            return a

        def find_candidates(t, l):  # Time: O(logt)
            candidates = []
            for x in reversed(range(2, 9+1)):
                while t%x == 0:
                    t //= x
                    candidates.append(x)
                    if len(candidates) > l:
                        return []
                if t == 1:
                    candidates.reverse()
                    return candidates
            return []
    
        def format(candidates, l):
            result = [1]*l
            i = len(result)-len(candidates)
            for x in candidates:
                result[i] = x
                i += 1
            return "".join(map(str, result))

        nums = list(map(int, num))
        candidates = find_candidates(t, float("inf"))
        if t != 1 and not candidates:
            return "-1"
        i = next((i for i in range(len(nums)) if not nums[i]), len(nums))
        for j in range(i, len(nums)):
            nums[j] = 1
        prefix = [1]*(len(nums)+1)
        for i in range(len(prefix)-1):
            prefix[i+1] = (prefix[i]*nums[i])%t
        if not prefix[-1]:
            return "".join(map(str, nums))
        for i in reversed(range(len(nums))):
             target = t//gcd(t, prefix[i])
             for x in range(nums[i]+1, 9+1):
                new_target = target//gcd(target, x)
                tmp = find_candidates(new_target, len(nums)-1-i)
                if new_target != 1 and not tmp:
                    continue
                nums[i] = x
                return "".join(map(str, nums[:i+1]))+format(tmp, len(nums)-1-i)
        return format(candidates, max(len(nums)+1, len(candidates)))
