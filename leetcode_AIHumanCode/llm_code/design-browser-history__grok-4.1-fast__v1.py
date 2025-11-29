class BrowserHistory:

    def __init__(self, homepage):
        self.backward = [homepage]
        self.forward = []

    def visit(self, url):
        self.backward.append(url)
        self.forward = []

    def back(self, steps):
        while steps > 0 and len(self.backward) > 1:
            self.forward.append(self.backward.pop())
            steps -= 1
        return self.backward[-1]

    def forward(self, steps):
        while steps > 0 and self.forward:
            self.backward.append(self.forward.pop())
            steps -= 1
        return self.backward[-1]
