class Solution:
    def isValid(self, s):
        stack = ["?"]
        dic = {'{': '}', '[': ']', '(': ')', '?': '?'}
        for c in s:
            if c in dic:
                stack.append(c)
            elif dic[stack.pop()] != c:
                return False
        if len(stack) == 1:
            return True
        elif len(stack) > 1:
            return False


s = "()[]{}"
y = Solution()
res=y.isValid(s)
