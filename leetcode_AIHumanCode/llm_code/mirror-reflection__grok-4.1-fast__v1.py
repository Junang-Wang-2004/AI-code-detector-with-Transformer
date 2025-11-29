class Solution:
    def mirrorReflection(self, p, q):
        def valuation(num):
            count = 0
            while num % 2 == 0:
                num //= 2
                count += 1
            return count
        
        vp = valuation(p)
        vq = valuation(q)
        if vp > vq:
            return 2
        elif vp < vq:
            return 0
        else:
            return 1
