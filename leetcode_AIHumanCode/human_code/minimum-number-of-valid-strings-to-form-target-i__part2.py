# Time:  O(n + w * l)
# Space: O(n + t), t is the total size of ac automata trie
import collections


class AhoNode(object):
    def __init__(self):
        self.children = collections.defaultdict(AhoNode)
        # self.indices = []
        self.suffix = None
        # self.output = None
        self.length = 0  # added


class AhoTrie(object):

    def step(self, letter):
        while self.__node and letter not in self.__node.children:
            self.__node = self.__node.suffix
        self.__node = self.__node.children[letter] if self.__node else self.__root
        return self.__get_ac_node_outputs(self.__node)
    
    def __init__(self, patterns):
        self.__root = self.__create_ac_trie(patterns)
        self.__node = self.__create_ac_suffix_and_output_links(self.__root)
    
    def __create_ac_trie(self, patterns):  # Time:  O(n), Space: O(t)
        root = AhoNode()
        for i, pattern in enumerate(patterns):
            node = root
            for l, c in enumerate(pattern, 1):  # modified
                node = node.children[c]
                node.length = l  # added
            # node.indices.append(i)
        return root

    def __create_ac_suffix_and_output_links(self, root):  # Time:  O(n), Space: O(t)
        queue = collections.deque()
        for node in root.children.values():
            queue.append(node)
            node.suffix = root

        while queue:
            node = queue.popleft()
            for c, child in node.children.items():
                queue.append(child)
                suffix = node.suffix
                while suffix and c not in suffix.children:
                    suffix = suffix.suffix
                child.suffix = suffix.children[c] if suffix else root
                # child.output = child.suffix if child.suffix.indices else child.suffix.output
                
        return root

    def __get_ac_node_outputs(self, node):  # Time:  O(z)
        return node.length  # modified
        # result = []
        # for i in node.indices:
        #     result.append(i)
        # output = node.output
        # while output:
        #     for i in output.indices:
        #         result.append(i)
        #     output = output.output
        # return result


# ac automata trie
class Solution2(object):
    def minValidStrings(self, words, target):
        """
        """
        trie = AhoTrie(words)
        dp = [0]*(len(target)+1)
        for i in range(len(target)):
            l = trie.step(target[i])
            if not l:
                return -1
            dp[i+1] = dp[(i-l)+1]+1
        return dp[-1]


