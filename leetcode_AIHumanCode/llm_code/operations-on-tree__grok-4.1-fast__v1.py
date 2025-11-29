class LockingTree(object):

    def __init__(self, parent):
        self.parent_arr = parent
        self.children_arr = [[] for _ in range(len(parent))]
        self.owner = {}
        for node_idx, par_idx in enumerate(parent):
            if par_idx != -1:
                self.children_arr[par_idx].append(node_idx)

    def lock(self, num, user):
        if num in self.owner:
            return False
        self.owner[num] = user
        return True

    def unlock(self, num, user):
        if num not in self.owner or self.owner[num] != user:
            return False
        del self.owner[num]
        return True

    def upgrade(self, num, user):
        cur = num
        while cur != -1:
            if cur in self.owner:
                return False
            cur = self.parent_arr[cur]
        to_unlock = []
        stk = [num]
        while stk:
            nd = stk.pop()
            if nd in self.owner:
                to_unlock.append(nd)
            for cld in self.children_arr[nd]:
                stk.append(cld)
        if to_unlock:
            for u in to_unlock:
                del self.owner[u]
            self.owner[num] = user
            return True
        return False
