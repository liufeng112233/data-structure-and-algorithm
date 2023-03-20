class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        res = []
        nums.sort()
        nums_new = list(set(nums))
        # 需要判断数据是否重复，重复数据的量
        if nums[0] != 1 and nums_new[0] - 0 != 1:  # 左边界不是1
            for k in range(nums_new[0] - 1, 0, -1):
                res.append(k)
        if n - nums_new[-1] != 0:  # 右边界不是n,切实重复出现
            for k in range(n - nums_new[-1]):
                res.append(n - k)
        for i in range(1, len(nums_new)):  # 中间情况
            if nums_new[i] - nums_new[i - 1] != 1:
                for j in range((nums_new[i] - nums_new[i - 1]) - 1, 0, -1):
                    res.append(nums_new[i] - j)
        res1 = list(set(res))
        res1.sort()
        return res1


# 采用嘻哈表
class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # nums = [4, 3, 2, 7, 8, 2, 3, 1]
        # nums = [1,1]
        # nums = [1,1,2,2]
        # nums = [1,1,1,1,1,2,4]
        dic = {}
        res = []
        n = len(nums)
        for i, num in enumerate(nums):  # 这里主要是记录出现的元组和次数
            if num in dic:
                dic[num] += 1
            else:
                dic[num] = 1
        for i in range(1,n+1):   # 判断字典内部元素，不在的补齐，由于【1，n】，所以循环是1——n+1
            if i not in dic:
                res.append(i)
