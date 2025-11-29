import heapq

class VideoSharingPlatform:
    class _VideoData:
        def __init__(self, clip):
            self.clip = clip
            self.like_count = 0
            self.dislike_count = 0
            self.view_count = 0

    def __init__(self):
        self._free_slots = []
        self._video_store = {}
        self._next_id = 0

    def upload(self, video):
        if self._free_slots:
            slot_id = heapq.heappop(self._free_slots)
        else:
            slot_id = self._next_id
            self._next_id += 1
        self._video_store[slot_id] = self._VideoData(video)
        return slot_id

    def remove(self, video_id):
        if video_id in self._video_store:
            heapq.heappush(self._free_slots, video_id)
            del self._video_store[video_id]

    def watch(self, video_id, start_minute, end_minute):
        if video_id not in self._video_store:
            return "-1"
        data = self._video_store[video_id]
        data.view_count += 1
        return data.clip[start_minute:end_minute + 1]

    def like(self, video_id):
        if video_id in self._video_store:
            self._video_store[video_id].like_count += 1

    def dislike(self, video_id):
        if video_id in self._video_store:
            self._video_store[video_id].dislike_count += 1

    def getLikesAndDislikes(self, video_id):
        if video_id not in self._video_store:
            return [-1]
        data = self._video_store[video_id]
        return [data.like_count, data.dislike_count]

    def getViews(self, video_id):
        if video_id not in self._video_store:
            return -1
        return self._video_store[video_id].view_count
