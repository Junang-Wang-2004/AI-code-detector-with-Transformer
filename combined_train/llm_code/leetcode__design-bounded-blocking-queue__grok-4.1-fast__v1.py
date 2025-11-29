import threading
import collections

class C1:

    def __init__(self, a1):
        """
        """
        self._limit = a1
        self._store = collections.deque()
        self._guard = threading.Lock()
        self._full_slots = threading.Semaphore(a1)
        self._ready_items = threading.Semaphore(0)

    def enqueue(self, a1):
        """
        """
        self._full_slots.acquire()
        with self._guard:
            self._store.append(a1)
        self._ready_items.release()

    def dequeue(self):
        """
        """
        self._ready_items.acquire()
        with self._guard:
            v1 = self._store.popleft()
        self._full_slots.release()
        return v1

    def size(self):
        """
        """
        with self._guard:
            return len(self._store)
