import heapq

class C1(object):

    def __init__(self):
        self.__avails = []
        self.__videos = []
        self.__likes = []
        self.__dislikes = []
        self.__views = []

    def upload(self, a1):
        """
        """
        if self.__avails:
            v1 = heapq.heappop(self.__avails)
        else:
            v1 = len(self.__videos)
            self.__videos.append(None)
            self.__likes.append(0)
            self.__dislikes.append(0)
            self.__views.append(0)
        self.__videos[v1] = a1
        return v1

    def remove(self, a1):
        """
        """
        if a1 >= len(self.__videos) or not self.__videos[a1]:
            return
        heapq.heappush(self.__avails, a1)
        self.__videos[a1] = None
        self.__likes[a1] = self.__dislikes[a1] = self.__views[a1] = 0

    def watch(self, a1, a2, a3):
        """
        """
        if a1 >= len(self.__videos) or not self.__videos[a1]:
            return '-1'
        self.__views[a1] += 1
        return self.__videos[a1][a2:a3 + 1]

    def like(self, a1):
        """
        """
        if a1 >= len(self.__videos) or not self.__videos[a1]:
            return
        self.__likes[a1] += 1

    def dislike(self, a1):
        """
        """
        if a1 >= len(self.__videos) or not self.__videos[a1]:
            return
        self.__dislikes[a1] += 1

    def getLikesAndDislikes(self, a1):
        """
        """
        if a1 >= len(self.__videos) or not self.__videos[a1]:
            return [-1]
        return [self.__likes[a1], self.__dislikes[a1]]

    def getViews(self, a1):
        """
        """
        if a1 >= len(self.__videos) or not self.__videos[a1]:
            return -1
        return self.__views[a1]
