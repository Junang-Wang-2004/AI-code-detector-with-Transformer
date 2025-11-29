from sortedcontainers import SortedList

class C1(object):

    def __init__(self):
        self.__tasks = []
        self.__user_task_ids = collections.defaultdict(SortedList)

    def addTask(self, a1, a2, a3, a4):
        """
        """
        self.__tasks.append([a3, a2, set(a4)])
        self.__user_task_ids[a1].add((a3, len(self.__tasks)))
        return len(self.__tasks)

    def getAllTasks(self, a1):
        """
        """
        if a1 not in self.__user_task_ids:
            return []
        return [self.__tasks[i - 1][1] for v1, v2 in self.__user_task_ids[a1]]

    def getTasksForTag(self, a1, a2):
        """
        """
        if a1 not in self.__user_task_ids:
            return []
        return [self.__tasks[i - 1][1] for v1, v2 in self.__user_task_ids[a1] if a2 in self.__tasks[v2 - 1][-1]]

    def completeTask(self, a1, a2):
        """
        """
        if not (a2 - 1 < len(self.__tasks) and a1 in self.__user_task_ids):
            return
        self.__user_task_ids[a1].discard((self.__tasks[a2 - 1][0], a2))
