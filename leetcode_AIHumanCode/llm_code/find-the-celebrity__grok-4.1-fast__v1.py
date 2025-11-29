class Solution(object):
    def findCelebrity(self, n):
        nominee = 0
        seeker = 1
        while seeker < n:
            if knows(nominee, seeker):
                nominee = seeker
            seeker += 1
        for other in range(n):
            if other != nominee and knows(nominee, other):
                return -1
        for other in range(n):
            if other != nominee and not knows(other, nominee):
                return -1
        return nominee
