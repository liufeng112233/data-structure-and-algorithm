nums = [-2, 1, -3, 4, 2, -2, 3, -5, 4]
result = -float('inf')
count = 0
for i in range(len(nums)):
    count += nums[i]
    if count > result:
        result = count
    if count <= 0:
        count = 0
