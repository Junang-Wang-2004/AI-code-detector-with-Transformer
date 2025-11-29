import heapq

class C1:

    class _VideoData:

        def __init__(self, a1):
            self.clip = a1
            self.like_count = 0
            self.dislike_count = 0
            self.view_count = 0

    def __init__(self):
        self._free_slots = []
        self._video_store = {}
        self._next_id = 0

    def upload(self, a1):
        if self._free_slots:
            v1 = heapq.heappop(self._free_slots)
        else:
            v1 = self._next_id
            self._next_id += 1
        self._video_store[v1] = self._VideoData(a1)
        return v1

    def remove(self, a1):
        if a1 in self._video_store:
            heapq.heappush(self._free_slots, a1)
            del self._video_store[a1]

    def watch(self, a1, a2, a3):
        if a1 not in self._video_store:
            return '-1'
        v1 = self._video_store[a1]
        v1.view_count += 1
        return v1.clip[a2:a3 + 1]

    def like(self, a1):
        if a1 in self._video_store:
            self._video_store[a1].like_count += 1

    def dislike(self, a1):
        if a1 in self._video_store:
            self._video_store[a1].dislike_count += 1

    def getLikesAndDislikes(self, a1):
        if a1 not in self._video_store:
            return [-1]
        v1 = self._video_store[a1]
        return [v1.like_count, v1.dislike_count]

    def getViews(self, a1):
        if a1 not in self._video_store:
            return -1
        return self._video_store[a1].view_count
