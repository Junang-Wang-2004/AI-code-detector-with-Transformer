import collections
import itertools
from sortedcontainers import SortedList

class C1(object):

    def __init__(self, a1, a2, a3):
        """
        """
        self.__food_to_cuisine = {}
        self.__food_to_rating = {}
        self.__cusine_to_rating_foods = collections.defaultdict(SortedList)
        for v1, v2, v3 in zip(a1, a2, a3):
            self.__food_to_cuisine[v1] = v2
            self.__food_to_rating[v1] = v3
            self.__cusine_to_rating_foods[v2].add((-v3, v1))

    def changeRating(self, a1, a2):
        """
        """
        v1 = self.__food_to_rating[a1]
        v2 = self.__food_to_cuisine[a1]
        self.__cusine_to_rating_foods[v2].remove((-v1, a1))
        self.__food_to_rating[a1] = a2
        self.__cusine_to_rating_foods[v2].add((-a2, a1))

    def highestRated(self, a1):
        """
        """
        return self.__cusine_to_rating_foods[a1][0][1]
