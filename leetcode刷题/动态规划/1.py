n, m = map(int, input().split())
att = list(map(int, input().split()))
len = len(att)
count = [0 for _ in range(len)]
dic = {}  # 存在相对应的列大辐射边界值
for i in range(len):
    dic[i] = [i - att[i], i + att[i]]
for i in range(len):
    for c in dic:
        if dic[c][0] <= i <= dic[c][1]:
            count[i] += 1
num = 0
for i in count:
    if i >= m:
        num += 1
print(num)

n, k = (int(i) for i in input().split())
arr = [int(i) for i in input().split()]
b = [0] * n
for i in range(n):
    if i - arr[i] < 0:
        b[0] += 1
    else:
        b[i - arr[i]] += 1
    if i + arr[i] < n - 1:
        b[i + arr[i] + 1] -= 1
tmp = 0
num = 0
for i in b:
    tmp += i
    if tmp >= k:
        num += 1
print(num)
