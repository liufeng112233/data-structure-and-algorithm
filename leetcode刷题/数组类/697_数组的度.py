class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = {}  # 存储数字、次数、第一次位置、最后一次位置
        # 重点注意嘻哈表的
        for i, num in enumerate(nums):   #
            if num in dic:
                dic[num][0] += 1
                dic[num][2] = i
            else:
                dic[num] = [1, i, i]  # 运行这一句话就是表示该数出现了一次
        maxnum = minlen = 0
        for count, left, right in dic.values():
            if maxnum < count:
                maxnum = count
                minlen = right - left+1
            elif maxnum == count:
                if minlen > (right - left + 1):
                    minlen = right - left + 1
        return minlen
