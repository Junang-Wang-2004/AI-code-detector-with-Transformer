class C1(object):

    def __init__(self, a1):
        """
        Initialize your data structure here.
        """
        self.__size = a1
        self.__rows = [[0, 0] for v1 in range(a1)]
        self.__cols = [[0, 0] for v1 in range(a1)]
        self.__diagonal = [0, 0]
        self.__anti_diagonal = [0, 0]

    def move(self, a1, a2, a3):
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """
        v1 = a3 - 1
        self.__rows[a1][v1] += 1
        self.__cols[a2][v1] += 1
        if a1 == a2:
            self.__diagonal[v1] += 1
        if a2 == len(self.__rows) - a1 - 1:
            self.__anti_diagonal[v1] += 1
        if any(self.__rows[a1][v1] == self.__size, self.__cols[a2][v1] == self.__size, self.__diagonal[v1] == self.__size, self.__anti_diagonal[v1] == self.__size):
            return a3
        return 0
