class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack=[]  # 栈元素
        self.minstack =[]  # 栈最小元素
    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack.append(x)   # 入栈
        if not self.minstack or x<=self.minstack[-1]:   # 判断minstack是否空，或者栈顶是否为最小值
            self.minstack.append(x)

    def pop(self):
        """
        :rtype: None
        """
        if self.stack.pop()==self.minstack[-1]:
            self.minstack.pop() 


    def top(self):
        """
        :rtype: int
        """ 
        return self.stack[-1]

    def min(self):
        """
        :rtype: int
        """
        return self.minstack[-1]
