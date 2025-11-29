def f1(a1):
    global file_content
    v1 = 0
    while v1 < len(file_content) and v1 < 4:
        a1[v1] = file_content[v1]
        v1 += 1
    if len(file_content) > 4:
        v2 = v2[4:]
    else:
        v2 = ''
    return v1

class C1(object):

    def __init__(self):
        self.__buf4 = [''] * 4
        self.__i4 = 0
        self.__n4 = 0

    def read(self, a1, a2):
        """
        """
        v1 = 0
        while v1 < a2:
            if self.__i4 < self.__n4:
                a1[v1] = self.__buf4[self.__i4]
                v1 += 1
                self.__i4 += 1
            else:
                self.__n4 = f1(self.__buf4)
                if self.__n4:
                    self.__i4 = 0
                else:
                    break
        return v1
