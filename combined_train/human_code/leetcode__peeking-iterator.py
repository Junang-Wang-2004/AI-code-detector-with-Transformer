class C1(object):

    def __init__(self, a1):
        """
        Initialize your data structure here.
        """
        self.iterator = a1
        self.val_ = None
        self.has_next_ = a1.hasNext()
        self.has_peeked_ = False

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        """
        if not self.has_peeked_:
            self.has_peeked_ = True
            self.val_ = next(self.iterator)
        return self.val_

    def __next__(self):
        """
        """
        self.val_ = self.peek()
        self.has_peeked_ = False
        self.has_next_ = self.iterator.hasNext()
        return self.val_

    def hasNext(self):
        """
        """
        return self.has_next_
