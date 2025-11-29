class C1:

    def __init__(self):
        self.children = {}
        self.pass_count = 0
        self.word_count = 0

class C2:

    def __init__(self):
        self.root = C1()

    def insert(self, a1):
        v1 = self.root
        v1.pass_count += 1
        for v2 in a1:
            if v2 not in v1.children:
                v1.children[v2] = C1()
            v1 = v1.children[v2]
            v1.pass_count += 1
        v1.word_count += 1

    def countWordsEqualTo(self, a1):
        v1 = self.root
        for v2 in a1:
            if v2 not in v1.children:
                return 0
            v1 = v1.children[v2]
        return v1.word_count

    def countWordsStartingWith(self, a1):
        v1 = self.root
        for v2 in a1:
            if v2 not in v1.children:
                return 0
            v1 = v1.children[v2]
        return v1.pass_count

    def erase(self, a1):
        if self.countWordsEqualTo(a1) == 0:
            return
        v1 = self.root
        v1.pass_count -= 1
        for v2 in a1:
            v3 = v1.children[v2]
            if v3.pass_count == 1:
                del v1.children[v2]
                return
            v1 = v3
            v1.pass_count -= 1
        v1.word_count -= 1
