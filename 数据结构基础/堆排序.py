"""
    树顺序存储，采用列表存储
"""


def sift(li, low, high):
    """
    :param li: 列表
    :param low:  堆的根节点位置
    :param high:  堆的最后一个元素的位置
    :return:
    """
    i = low
    j = 2 * i + 1  # 右孩子
    tmp = li[low]  # 将堆顶保存
    while j <= high:  # 只要j位置有界
        if j + 1 < +high and li[j] < li[j + 1]:  # 右孩子较大且有界
            j = j + 1  # j指向右孩子
        if li[j] > tmp:
            li[i] = li[j]
            i = j  # 进入下一层
            j = 2 * i + 1
        else:  # tmp更大，将tmp放到i的位置上
            li[i] = tmp  # 将tmp放到某一级的领导位置上。可删除
            break
    else:
        li[i] = tmp  # 把tmp放到叶子节点上


def heap_sort(li):
    n = len(li)
    for i in range((n - 2) // 2, -1, -1):
        # 表示建堆的时候调整的部分的下标
        sift(li, i, n - 1)
        # 建堆完成
        for i in range(n - 1, -1, -1):
            li[0], li[i] = li[i], li[0]
            sift(li, 0, i - 1)  # i-1是新的high
