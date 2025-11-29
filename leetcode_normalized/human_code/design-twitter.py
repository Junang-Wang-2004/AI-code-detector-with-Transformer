import collections
import heapq
import random

class C1(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.__number_of_most_recent_tweets = 10
        self.__followings = collections.defaultdict(set)
        self.__messages = collections.defaultdict(list)
        self.__time = 0

    def postTweet(self, a1, a2):
        """
        Compose a new tweet.
        """
        self.__time += 1
        self.__messages[a1].append((self.__time, a2))

    def getNewsFeed(self, a1):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """

        def nth_element(a1, a2, a3=lambda a, b: a < b):

            def tri_partition(a1, a2, a3, a4, a5):
                v1 = a2
                while v1 <= a3:
                    if a1[v1] == a4:
                        v1 += 1
                    elif a5(a1[v1], a4):
                        a1[a2], a1[v1] = (a1[v1], a1[a2])
                        a2 += 1
                        v1 += 1
                    else:
                        a1[v1], a1[a3] = (a1[a3], a1[v1])
                        a3 -= 1
                return (a2, a3)
            v1, v2 = (0, len(a1) - 1)
            while v1 <= v2:
                v3 = random.randint(v1, v2)
                v4, v5 = tri_partition(a1, v1, v2, a1[v3], a3)
                if v4 <= a2 <= v5:
                    return
                elif v4 > a2:
                    v2 = v4 - 1
                else:
                    v1 = v5 + 1
        v1 = []
        if self.__messages[a1]:
            v1.append((-self.__messages[a1][-1][0], a1, 0))
        for v2 in self.__followings[a1]:
            if self.__messages[v2]:
                v1.append((-self.__messages[v2][-1][0], v2, 0))
        nth_element(v1, self.__number_of_most_recent_tweets - 1)
        v3 = v1[:self.__number_of_most_recent_tweets]
        heapq.heapify(v3)
        v4 = []
        while v3 and len(v4) < self.__number_of_most_recent_tweets:
            v5, v2, v6 = heapq.heappop(v3)
            v7 = v6 + 1
            if v7 != len(self.__messages[v2]):
                heapq.heappush(v3, (-self.__messages[v2][-(v7 + 1)][0], v2, v7))
            v4.append(self.__messages[v2][-(v6 + 1)][1])
        return v4

    def follow(self, a1, a2):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        if a1 != a2:
            self.__followings[a1].add(a2)

    def unfollow(self, a1, a2):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        self.__followings[a1].discard(a2)
