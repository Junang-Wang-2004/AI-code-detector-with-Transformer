import threading
import collections

class BoundedBlockingQueue:
    def __init__(self, capacity):
        """
        """
        self._limit = capacity
        self._store = collections.deque()
        self._guard = threading.Lock()
        self._full_slots = threading.Semaphore(capacity)
        self._ready_items = threading.Semaphore(0)

    def enqueue(self, element):
        """
        """
        self._full_slots.acquire()
        with self._guard:
            self._store.append(element)
        self._ready_items.release()

    def dequeue(self):
        """
        """
        self._ready_items.acquire()
        with self._guard:
            val = self._store.popleft()
        self._full_slots.release()
        return val

    def size(self):
        """
        """
        with self._guard:
            return len(self._store)
