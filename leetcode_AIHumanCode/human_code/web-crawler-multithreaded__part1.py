# Time:  O(|V| + |E|)
# Space: O(|V|)

import threading
import queue


# """
# This is HtmlParser's API interface.
# You should not implement it, or speculate about its implementation
# """
class HtmlParser(object):
   def getUrls(self, url):
       """
       """
       pass


class Solution(object):
    NUMBER_OF_WORKERS = 8
    
    def __init__(self):
        self.__cv = threading.Condition()
        self.__q = queue.Queue()

    def crawl(self, startUrl, htmlParser):
        """
        """
        SCHEME = "http://"
        def hostname(url):
            pos = url.find('/', len(SCHEME))
            if pos == -1:
                return url
            return url[:pos]

        def worker(htmlParser, lookup):
            while True:
                from_url = self.__q.get()
                if from_url is None:
                    break
                name = hostname(from_url)
                for to_url in htmlParser.getUrls(from_url):
                    if name != hostname(to_url):
                        continue
                    with self.__cv:
                        if to_url not in lookup:
                           lookup.add(to_url)
                           self.__q.put(to_url)
                self.__q.task_done()

        workers = []
        self.__q = queue.Queue()
        self.__q.put(startUrl)
        lookup = set([startUrl])
        for i in range(self.NUMBER_OF_WORKERS):
            t = threading.Thread(target=worker, args=(htmlParser, lookup))
            t.start()
            workers.append(t)
        self.__q.join()
        for t in workers:
            self.__q.put(None)
        for t in workers:
            t.join()
        return list(lookup)


