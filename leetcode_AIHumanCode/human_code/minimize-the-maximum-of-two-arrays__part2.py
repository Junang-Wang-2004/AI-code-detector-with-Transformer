# Time:  O(log(min(d1, d2)) + logr)
# Space: O(1)
# binary search
class Solution2(object):
    def minimizeSet(self, divisor1, divisor2, uniqueCnt1, uniqueCnt2):
        """
        """
        def gcd(a, b):
            while b:
                a, b = b, a%b
            return a

        def lcm(a, b):
            return a//gcd(a, b)*b

        def check(cnt):
            return (cnt-cnt//divisor1 >= uniqueCnt1 and
                    cnt-cnt//divisor2 >= uniqueCnt2 and
                    cnt-cnt//l >= uniqueCnt1+uniqueCnt2)

        l = lcm(divisor1, divisor2)
        left, right = 2, 2**31-1
        while left <= right:
            mid = left+(right-left)//2
            if check(mid):
                right = mid-1
            else:
                left = mid+1
        return left
