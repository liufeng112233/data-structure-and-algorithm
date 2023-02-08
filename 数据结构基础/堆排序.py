"""
    树顺序存储，采用列表存储
"""


def sift(li, low, high):
    """
    :param li: 列表
    :param low:  堆的根节点位置（堆顶）
    :param high:  堆的最后一个元素的位置
    :return:
    """
    i = low   # 保存根结点父节点
    j = 2 * i + 1  # 左孩子
    tmp = li[low]  # 将堆顶保存
    while j <= high:  # 只要j位置有界
        if j + 1 < high and li[j] < li[j + 1]:  # 右孩子较大且有界
            j = j + 1  # j指向右孩子
        if li[j] > tmp:
            li[i] = li[j]
            i = j  # 进入下一层
            j = 2 * i + 1
        else:  # tmp更大，将tmp放到i的位置上
            li[i] = tmp  # 将tmp放到某一级的领导位置上。可删除，小值向下调整
            break
    else:
        li[i] = tmp  # 把tmp放到叶子节点上


def heap_sort(li):
    n = len(li)
    for i in range((n - 2) // 2, -1, -1):
        # 表示建堆的时候调整的部分的根的下标
        sift(li, i, n - 1)
        # 建堆完成
    for i in range(n - 1, -1, -1):
        li[0], li[i] = li[i], li[0]
        sift(li, 0, i - 1)  # i-1是新的high


# 堆排序——topk问题，复杂度mlogn
# 现有N个数，设计算法得到前K大的数
# 小根堆处理Topk
def sift_min(li, low, high):
    """ 小根堆
    :param li: 列表
    :param low:  堆的根节点位置（堆顶）
    :param high:  堆的最后一个元素的位置
    :return:
    """
    i = low
    j = 2 * i + 1  # 左孩子
    tmp = li[low]  # 将堆顶保存
    while j <= high:  # 只要j位置有界
        if j + 1 <= high and li[j] > li[j + 1]:  # 右孩子较大且有界
            j = j + 1  # j指向右孩子
        if li[j] < tmp:
            li[i] = li[j]
            i = j  # 进入下一层
            j = 2 * i + 1
        else:  # tmp更大，将tmp放到i的位置上
            li[i] = tmp  # 将tmp放到某一级的领导位置上。可删除，小值向下调整
            break
    else:
        li[i] = tmp  # 把tmp放到叶子节点上


def topk(li, k):
    heap = li[0:k]
    for i in range((k - 2) // 2, -1, -1):
        sift(heap, i, k - 1)
        # 建堆
    for i in range(k, len(li) - 1):
        if li[i] > heap[0]:  # 堆顶元素比较
            heap[0] = li[i]
            sift(heap, 0, k - 1)
    # 遍历
    for i in range(k - 1, -1, -1):
        heap[0], heap[i] = heap[i], heap[0]
        sift(li, 0, i - 1)  # i-1是新的high
        # 出数
    return heap

