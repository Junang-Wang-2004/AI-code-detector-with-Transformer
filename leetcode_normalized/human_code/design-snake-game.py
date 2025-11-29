from collections import deque

class C1(object):

    def __init__(self, a1, a2, a3):
        """
        Initialize your data structure here.
        @param width - screen width
        @param height - screen height
        @param food - A list of food positions
        E.g food = [[1,1], [1,0]] means the first food is positioned at [1,1], the second is at [1,0].
        """
        self.__width = a1
        self.__height = a2
        self.__score = 0
        self.__f = 0
        self.__food = a3
        self.__snake = deque([(0, 0)])
        self.__direction = {'U': (-1, 0), 'L': (0, -1), 'R': (0, 1), 'D': (1, 0)}
        self.__lookup = {(0, 0)}

    def move(self, a1):
        """
        Moves the snake.
        @param direction - 'U' = Up, 'L' = Left, 'R' = Right, 'D' = Down
        @return The game's score after the move. Return -1 if game over.
        Game over when snake crosses the screen boundary or bites its body.
        """

        def valid(a1, a2):
            return 0 <= a1 < self.__height and 0 <= a2 < self.__width and ((a1, a2) not in self.__lookup)
        v1 = self.__direction[a1]
        v2, v3 = (self.__snake[-1][0] + v1[0], self.__snake[-1][1] + v1[1])
        self.__lookup.remove(self.__snake[0])
        v4 = self.__snake.popleft()
        if not valid(v2, v3):
            return -1
        elif self.__f != len(self.__food) and (self.__food[self.__f][0], self.__food[self.__f][1]) == (v2, v3):
            self.__score += 1
            self.__f += 1
            self.__snake.appendleft(v4)
            self.__lookup.add(v4)
        self.__snake.append((v2, v3))
        self.__lookup.add((v2, v3))
        return self.__score
