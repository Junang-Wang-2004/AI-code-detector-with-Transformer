class Node:
    def __init__(self):
        self.children = {}
        self.is_file = False
        self.content = ""

class FileSystem:
    def __init__(self):
        self.root = Node()

    def _split_path(self, path):
        if path == "/":
            return []
        components = path.split("/")[1:]
        return [comp for comp in components if comp]

    def _navigate(self, path, create=False):
        segments = self._split_path(path)
        current = self.root
        for segment in segments:
            if create and segment not in current.children:
                current.children[segment] = Node()
            current = current.children[segment]
        return current

    def ls(self, path):
        segments = self._split_path(path)
        node = self._navigate(path, False)
        if node.is_file:
            return [segments[-1]]
        return sorted(node.children.keys())

    def mkdir(self, path):
        node = self._navigate(path, True)
        node.is_file = False

    def addContentToFile(self, file_path, content):
        node = self._navigate(file_path, True)
        node.is_file = True
        node.content += content

    def readContentFromFile(self, file_path):
        node = self._navigate(file_path, False)
        return node.content
