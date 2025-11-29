import collections
import heapq
from typing import List


class Twitter:

    def __init__(self):
        self.tweet_lists = collections.defaultdict(list)
        self.followers_map = collections.defaultdict(set)
        self.global_time = 0

    def postTweet(self, user_id: int, tweet_id: int) -> None:
        self.global_time += 1
        self.tweet_lists[user_id].append((self.global_time, tweet_id))

    def getNewsFeed(self, user_id: int) -> List[int]:
        priority_queue = []
        users_to_check = list(self.followers_map[user_id]) + [user_id]
        for uid in users_to_check:
            if self.tweet_lists[uid]:
                latest_time, _ = self.tweet_lists[uid][-1]
                heapq.heappush(priority_queue, (-latest_time, uid, len(self.tweet_lists[uid]) - 1))
        news_feed = []
        while priority_queue and len(news_feed) < 10:
            _, uid, tweet_idx = heapq.heappop(priority_queue)
            news_feed.append(self.tweet_lists[uid][tweet_idx][1])
            if tweet_idx > 0:
                next_time, _ = self.tweet_lists[uid][tweet_idx - 1]
                heapq.heappush(priority_queue, (-next_time, uid, tweet_idx - 1))
        return news_feed

    def follow(self, follower_id: int, followee_id: int) -> None:
        if follower_id != followee_id:
            self.followers_map[follower_id].add(followee_id)

    def unfollow(self, follower_id: int, followee_id: int) -> None:
        self.followers_map[follower_id].discard(followee_id)
