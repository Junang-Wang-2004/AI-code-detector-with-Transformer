import random
import math

class C1(object):

    def __init__(self, a1, a2, a3):
        """
        """
        self.__radius = a1
        self.__x_center = a2
        self.__y_center = a3

    def randPoint(self):
        """
        """
        v1 = self.__radius * math.sqrt(random.uniform(0, 1))
        v2 = 2 * math.pi * random.uniform(0, 1)
        return (v1 * math.cos(v2) + self.__x_center, v1 * math.sin(v2) + self.__y_center)
