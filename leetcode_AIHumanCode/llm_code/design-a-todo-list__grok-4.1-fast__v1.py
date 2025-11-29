import bisect
import collections

class TodoList:
    def __init__(self):
        self.all_tasks = []
        self.by_user = collections.defaultdict(list)
        self.by_user_tag = collections.defaultdict(lambda: collections.defaultdict(list))

    def addTask(self, userId, taskDescription, dueDate, tags):
        tag_set = set(tags)
        self.all_tasks.append((dueDate, taskDescription, tag_set))
        task_id = len(self.all_tasks)
        entry = (dueDate, task_id)
        bisect.insort(self.by_user[userId], entry)
        for tag in tag_set:
            bisect.insort(self.by_user_tag[userId][tag], entry)
        return task_id

    def getAllTasks(self, userId):
        if userId not in self.by_user:
            return []
        user_list = self.by_user[userId]
        return [self.all_tasks[idx - 1][1] for _, idx in user_list]

    def getTasksForTag(self, userId, tag):
        if userId not in self.by_user_tag:
            return []
        user_tags = self.by_user_tag[userId]
        if tag not in user_tags:
            return []
        tag_list = user_tags[tag]
        return [self.all_tasks[idx - 1][1] for _, idx in tag_list]

    def completeTask(self, userId, taskId):
        if not (1 <= taskId <= len(self.all_tasks) and userId in self.by_user):
            return
        due_date, _, tag_set = self.all_tasks[taskId - 1]
        entry = (due_date, taskId)
        ulist = self.by_user[userId]
        pos = bisect.bisect_left(ulist, entry)
        if pos < len(ulist) and ulist[pos] == entry:
            del ulist[pos]
        for tag in tag_set:
            tlist = self.by_user_tag[userId][tag]
            pos = bisect.bisect_left(tlist, entry)
            if pos < len(tlist) and tlist[pos] == entry:
                del tlist[pos]
