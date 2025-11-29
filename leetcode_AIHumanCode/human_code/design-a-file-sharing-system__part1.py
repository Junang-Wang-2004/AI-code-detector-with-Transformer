# Time:  ctor:    O(1)
#        join:    O(logu + c), u is the number of total joined users
#        leave:   O(logu + c), c is the number of chunks
#        request: O(u)
# Space: O(u * c)

import heapq


# "u ~= n" solution, n is the average number of users who own the chunk
class FileSharing(object):

    def __init__(self, m):
        """
        """
        self.__users = []
        self.__lookup = set()
        self.__min_heap = []

    def join(self, ownedChunks):
        """
        """
        if self.__min_heap:
            userID = heapq.heappop(self.__min_heap)
        else:
            userID = len(self.__users)+1
            self.__users.append(set())
        self.__users[userID-1] = set(ownedChunks)
        self.__lookup.add(userID)
        return userID

    def leave(self, userID):
        """
        """
        if userID not in self.__lookup:
            return
        self.__lookup.remove(userID)
        self.__users[userID-1] = []
        heapq.heappush(self.__min_heap, userID)

    def request(self, userID, chunkID):
        """
        """
        result = []
        for u, chunks in enumerate(self.__users, 1):
            if chunkID not in chunks:
                continue
            result.append(u)
        if not result:
            return
        self.__users[userID-1].add(chunkID)
        return result


