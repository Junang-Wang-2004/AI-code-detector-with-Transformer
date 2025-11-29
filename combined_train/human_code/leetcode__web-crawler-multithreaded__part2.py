import threading
import collections

class C1(object):
    v1 = 8

    def __init__(self):
        self.__cv = threading.Condition()
        self.__q = collections.deque()
        self.__working_count = 0

    def crawl(self, a1, a2):
        """
        """
        v1 = 'http://'

        def hostname(a1):
            v1 = a1.find('/', len(v1))
            if v1 == -1:
                return a1
            return a1[:v1]

        def worker(a1, a2):
            while True:
                with self.__cv:
                    while not self.__q:
                        self.__cv.wait()
                    v1 = self.__q.popleft()
                    if v1 is None:
                        break
                    self.__working_count += 1
                v2 = hostname(v1)
                for v3 in a1.getUrls(v1):
                    if v2 != hostname(v3):
                        continue
                    with self.__cv:
                        if v3 not in a2:
                            a2.add(v3)
                            self.__q.append(v3)
                            self.__cv.notifyAll()
                with self.__cv:
                    self.__working_count -= 1
                    if not self.__q and (not self.__working_count):
                        self.__cv.notifyAll()
        v2 = []
        self.__q = collections.deque([a1])
        v3 = set([a1])
        for v4 in range(self.NUMBER_OF_WORKERS):
            v5 = threading.Thread(target=worker, args=(a2, v3))
            v5.start()
            v2.append(v5)
        with self.__cv:
            while self.__q or self.__working_count:
                self.__cv.wait()
            for v4 in range(self.NUMBER_OF_WORKERS):
                self.__q.append(None)
            self.__cv.notifyAll()
        for v5 in v2:
            v5.join()
        return list(v3)
