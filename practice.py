def addTwoNumbers(self, l1, l2):
    result = curr = list()
    len1 = len(l1)
    len2 = len(l2)
    temp_L1 = []
    temp_L2 = []
    result = []
    for i in range(len1):
        data1 = 10 ** (len1 - i - 1) * l1[len1 - i - 1]
        temp_L1.append(data1)
        print(data1)
    for j in range(len2):
        data2 = 10 ** (len2 - j - 1) * l2[len2 - j - 1]
        temp_L2.append(data2)
        print(data2)
    total = sum(temp_L2) + sum(temp_L1)
    total_str = str(total)
    len_total = len(str(total))
    for k in range(len_total):
        result.append(total_str[len_total - k - 1])
    return result
