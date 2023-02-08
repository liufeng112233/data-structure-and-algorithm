class Solution(object):
    def sortPeople(self, names, heights):
        for i in range(len(heights) - 1):  # 定义趟数
            exchange = False  # 添加标志位，主要是解决无序区也自然有序的情况[9,8,7,1,2,4,5,6]
            for j in range(len(heights) - i - 1):
                if heights[j] < heights[j + 1]:  # 降序<，升序>
                    heights[j], heights[j + 1] = heights[j + 1], heights[j]  # 两个数交换位置
                    names[j], names[j + 1] = names[j + 1], names[j]  # 两个数交换位置
                    exchange = True
            if not exchange:
                break
        return names
