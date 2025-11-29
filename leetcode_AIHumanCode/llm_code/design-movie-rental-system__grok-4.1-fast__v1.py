import collections
import heapq

class MovieRentingSystem:

    def __init__(self, n, entries):
        self.prices = {}
        self.avail_heaps = collections.defaultdict(list)
        self.rented_items = set()
        self.rented_heap = []
        for shop, movie, price in entries:
            key = (shop, movie)
            self.prices[key] = price
            heapq.heappush(self.avail_heaps[movie], (price, shop))

    def search(self, movie):
        heap = self.avail_heaps[movie]
        result = []
        temp = []
        while len(result) < 5 and heap:
            price, shop = heapq.heappop(heap)
            key = (shop, movie)
            if key not in self.rented_items:
                result.append(shop)
                temp.append((price, shop))
        for item in temp:
            heapq.heappush(heap, item)
        return result

    def rent(self, shop, movie):
        key = (shop, movie)
        price = self.prices[key]
        self.rented_items.add(key)
        heapq.heappush(self.rented_heap, (price, shop, movie))

    def drop(self, shop, movie):
        key = (shop, movie)
        self.rented_items.remove(key)

    def report(self):
        heap = self.rented_heap
        result = []
        temp = []
        while len(result) < 5 and heap:
            price, shop, movie = heapq.heappop(heap)
            key = (shop, movie)
            if key in self.rented_items:
                result.append([shop, movie])
                temp.append((price, shop, movie))
        for item in temp:
            heapq.heappush(heap, item)
        return result
