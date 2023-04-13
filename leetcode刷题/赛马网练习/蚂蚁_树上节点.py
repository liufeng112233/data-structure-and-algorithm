n = int(input())
res = 0
for _ in range(n-1):
    a, b = list(map(int, input().split()))   # 表示两个节点之间的连接数值
    res += abs(b-a)
print(res)