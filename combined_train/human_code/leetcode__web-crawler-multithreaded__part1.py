import threading
import queue

class C1(object):

    def getUrls(self, a1):
        """
       """
        pass

class C2(object):
    v1 = 8

    def __init__(self):
        self.__cv = threading.Condition()
        self.__q = queue.Queue()

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
                v1 = self.__q.get()
                if v1 is None:
                    break
                v2 = hostname(v1)
                for v3 in a1.getUrls(v1):
                    if v2 != hostname(v3):
                        continue
                    with self.__cv:
                        if v3 not in a2:
                            a2.add(v3)
                            self.__q.put(v3)
                self.__q.task_done()
        v2 = []
        self.__q = queue.Queue()
        self.__q.put(a1)
        v3 = set([a1])
        for v4 in range(self.NUMBER_OF_WORKERS):
            v5 = threading.Thread(target=worker, args=(a2, v3))
            v5.start()
            v2.append(v5)
        self.__q.join()
        for v5 in v2:
            self.__q.put(None)
        for v5 in v2:
            v5.join()
        return list(v3)
