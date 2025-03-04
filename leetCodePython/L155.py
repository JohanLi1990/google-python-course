from collections import deque
class MinStack(object):
    '''
    one normal stack
    one min stack
    '''
    def __init__(self):
        self.normal = deque()
        self.minStack = deque()
        
    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.normal.appendleft(val)
        if (len(self.minStack) > 0):
            self.minStack.appendleft(min(val, self.minStack[0]))
        else:
            self.minStack.appendleft(val)
        

    def pop(self):
        """
        :rtype: None
        """
        ret = self.normal.popleft()
        self.minStack.popleft()
    
    def top(self):
        """
        :rtype: int
        """
        return self.normal[0]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.minStack[0]
        