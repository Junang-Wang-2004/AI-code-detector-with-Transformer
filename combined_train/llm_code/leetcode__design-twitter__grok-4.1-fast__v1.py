import collections
import heapq
from typing import List

class C1:

    def __init__(self):
        self.tweet_lists = collections.defaultdict(list)
        self.followers_map = collections.defaultdict(set)
        self.global_time = 0

    def postTweet(self, a1: int, a2: int) -> None:
        self.global_time += 1
        self.tweet_lists[a1].append((self.global_time, a2))

    def getNewsFeed(self, a1: int) -> List[int]:
        v1 = []
        v2 = list(self.followers_map[a1]) + [a1]
        for v3 in v2:
            if self.tweet_lists[v3]:
                v4, v5 = self.tweet_lists[v3][-1]
                heapq.heappush(v1, (-v4, v3, len(self.tweet_lists[v3]) - 1))
        v6 = []
        while v1 and len(v6) < 10:
            v5, v3, v7 = heapq.heappop(v1)
            v6.append(self.tweet_lists[v3][v7][1])
            if v7 > 0:
                v8, v5 = self.tweet_lists[v3][v7 - 1]
                heapq.heappush(v1, (-v8, v3, v7 - 1))
        return v6

    def follow(self, a1: int, a2: int) -> None:
        if a1 != a2:
            self.followers_map[a1].add(a2)

    def unfollow(self, a1: int, a2: int) -> None:
        self.followers_map[a1].discard(a2)
