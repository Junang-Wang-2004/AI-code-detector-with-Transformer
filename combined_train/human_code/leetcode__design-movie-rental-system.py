import collections
from sortedcontainers import SortedList

class C1(object):

    def __init__(self, a1, a2):
        """
        """
        self.__movie_to_ordered_price_shop = collections.defaultdict(SortedList)
        self.__shop_movie_to_price = {}
        self.__rented_ordered_price_shop_movie = SortedList()
        for v1, v2, v3 in a2:
            self.__movie_to_ordered_price_shop[v2].add((v3, v1))
            self.__shop_movie_to_price[v1, v2] = v3

    def search(self, a1):
        """
        """
        return [s for v1, v2 in self.__movie_to_ordered_price_shop[a1][:5]]

    def rent(self, a1, a2):
        """
        """
        v1 = self.__shop_movie_to_price[a1, a2]
        self.__movie_to_ordered_price_shop[a2].remove((v1, a1))
        self.__rented_ordered_price_shop_movie.add((v1, a1, a2))

    def drop(self, a1, a2):
        """
        """
        v1 = self.__shop_movie_to_price[a1, a2]
        self.__movie_to_ordered_price_shop[a2].add((v1, a1))
        self.__rented_ordered_price_shop_movie.remove((v1, a1, a2))

    def report(self):
        """
        """
        return [[s, m] for v1, v2, v3 in self.__rented_ordered_price_shop_movie[:5]]
