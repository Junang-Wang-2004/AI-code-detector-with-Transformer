# Time:  ctor:   O(1)
#        update: O(m * n)
#        get:    O(1)
# Space: O(1)
class SubrectangleQueries2(object):

    def __init__(self, rectangle):
        """
        """
        self.__rectangle = rectangle
        

    def updateSubrectangle(self, row1, col1, row2, col2, newValue):
        """
        """
        for r in range(row1, row2+1):
            for c in range(col1, col2+1):
                self.__rectangle[r][c] = newValue

    def getValue(self, row, col):
        """
        """
        return self.__rectangle[row][col]
