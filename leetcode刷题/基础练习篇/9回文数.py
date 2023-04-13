class Solution(object):

    def romanToInt(self,s):
        """
        :type s: str
        :rtype: int
        """
        self.base_dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        self.data = 0
        i = 0
        while i + 1 < len(s):  # 判断i+1和字符串长度的关系，
            if self.base_dic[s[i]] >= self.base_dic[s[i + 1]]:  # 这里是边界问题，i+1不能超过边界
                self.data = self.data + self.base_dic[s[i]]
                i += 1
            elif self.base_dic[s[i]] < self.base_dic[s[i + 1]]:  # 当前一个值小于后面一个值，该值设定为负数
                self.data = self.data - self.base_dic[s[i]]
                i += 1
        if i + 1 == len(s):  # 处理边界问题
            self.data = self.data + self.base_dic[s[i]]
            # print('运行')
        return self.data
