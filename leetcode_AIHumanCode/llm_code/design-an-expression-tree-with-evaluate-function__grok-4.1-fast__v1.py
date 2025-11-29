from abc import ABC, abstractmethod

class Node(ABC):
    @abstractmethod
    def evaluate(self) -> int:
        pass

class ExprNode(Node):
    def __init__(self, token):
        self.token = token
        self.left = None
        self.right = None

    def evaluate(self) -> int:
        if self.token.isdigit():
            return int(self.token)
        left_result = self.left.evaluate()
        right_result = self.right.evaluate()
        if self.token == '+':
            return left_result + right_result
        elif self.token == '-':
            return left_result - right_result
        elif self.token == '*':
            return left_result * right_result
        elif self.token == '/':
            return left_result // right_result

class TreeBuilder:
    def buildTree(self, postfix):
        operand_stack = []
        for char in postfix:
            if char.isdigit():
                leaf = ExprNode(char)
                operand_stack.append(leaf)
            else:
                operator_node = ExprNode(char)
                operator_node.right = operand_stack.pop()
                operator_node.left = operand_stack.pop()
                operand_stack.append(operator_node)
        return operand_stack.pop()
