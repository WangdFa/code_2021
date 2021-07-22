"""
求最大水容器，给定一个包含正整数的数组，a1，a2，...，an。每个元素都可以呈现成一个点(i，ai)。过每个点，做垂直于x轴的垂线，
得到对应交点(0，ai)。(0，ai)和(i，ai)构成一条直线。每条直线两两组合，构成一个储水容器，找到存储量最大的那个容器。
exmple:
输入是[1,3,5]，那么一共有三条垂直与x轴的直线，直线两两组合，面积最大为3。
"""
def long_word(example):
    left = 0
    right = len(example)-1
    max_area = 0
    while(left < right):
        tem_area = abs(left-right)*min([example[left],example[right]])
        if tem_area > max_area:
            max_area = tem_area
        if example[left] >= example[right]:
            right -= 1
        else:
            left += 1
    return max_area

def maxArea(height):
    """
    :type height: List[int]
    :rtype: int
    """
    area_tmp = 0
    area_max = 0
    left = 0
    right = len(height) - 1
    while (left < right):
        min_height = min(height[left], height[right])
        area_tmp = (right - left) * min_height
        if area_tmp > area_max:
            area_max = area_tmp
        if height[left] < height[right]:    #判断长短，省去了无谓计算
            left += 1
        else:
            right -= 1
    return area_max
a = maxArea([1,3,5])
b = long_word([1,3,5])
print(a)
print(b)