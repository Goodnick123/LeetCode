# -*- coding: utf-8 -*-
# @Time    : 2018/2/25 23:50
# @Author  : Yeh

class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack=[]
        self.minStack=[]

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)
        if self.minStack==[]:
            self.minStack.append(x)
        else:
            if self.minStack[-1]>x:
                self.minStack.append(x)
            else:
                self.minStack.append(self.minStack[-1])



    def pop(self):
        """
        :rtype: void
        """
        if self.stack:
            tmp = self.stack[-1]
            del self.minStack[-1]
            del self.stack[-1]
            return tmp
        else:
            return None

    def top(self):
        """
        :rtype: int
        """
        if self.stack:
            return self.stack[-1]
        else:
            return None

    def getMin(self):
        """
        :rtype: int
        """
        return self.minStack[-1]



# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(2)
print(obj.getMin())
obj.push(1)
print(obj.getMin())
obj.push(3)
print(obj.getMin())
obj.push(4)
print(obj.getMin())
obj.push(0)
print(obj.getMin())

print(obj.pop())
print(obj.pop())

