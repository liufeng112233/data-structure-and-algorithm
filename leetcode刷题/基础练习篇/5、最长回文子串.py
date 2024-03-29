# class Solution:
#     # 扩展左右序号
#     def expandAroundCenter(self, s, left, right):
#         while left >= 0 and right < len(s) and s[left] == s[right]:
#             left -= 1
#             right += 1
#         return left + 1, right - 1
#
#     def longestPalindrome(self, s):
#         self.start, self.end = 0, 0
#         for i in range(len(s)):
#             self.left1, self.right1 = self.expandAroundCenter(s, i, i)
#             self.left2, self.right2 = self.expandAroundCenter(s, i, i + 1)
#             if self.right1 - self.left1 > self.end - self.start:
#                 self.start, self.end = self.left1, self.right1
#             if self.right2 - self.left2 > self.end - self.start:
#                 self.start, self.end = self.left2, self.right2
#         return s[self.start: self.end + 1]

class Solution:
    def longestPalindrome(self, s):
        stack =[]
        res= 0
        for i in range(len(s)):
            if s[i] in stack:
                stack.append(s[i])
                list_temp = ''.join(stack)
                stack.reverse()
                list_temp1 = ''.join(stack)
                if list_temp1 == list_temp:
                    res = max(res, len(stack))
                else:
                    stack.reverse()
            else:
                stack.append(s[i])