class C1(object):

    def __init__(self):
        self.__logs = []
        self.__granularity = {'Year': 4, 'Month': 7, 'Day': 10, 'Hour': 13, 'Minute': 16, 'Second': 19}

    def put(self, a1, a2):
        """
        """
        self.__logs.append((a1, a2))

    def retrieve(self, a1, a2, a3):
        """
        """
        v1 = self.__granularity[a3]
        v2 = a1[:v1]
        v3 = a2[:v1]
        return sorted((id for id, v4 in self.__logs if v2 <= v4[:v1] <= v3))
