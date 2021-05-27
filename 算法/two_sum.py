"""
给定一个整数的数组nums，返回相加为target的两个数字的索引值。
假设每次输入都只有一个答案，并且不会使用同一个元素两次。
exmple:
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""

def twoSum_slow(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    result = []
    for i, each in enumerate(nums):
        if abs(target - each) >= 0 and i not in result: #我认为这个判断没有必要
            try:
                tmp = nums.index(target - each)
                if tmp != i:
                    result.append(i)
                    result.append(tmp)
            except:
                continue
    return result
print(twoSum_slow([2, 3 , 7 , 11, 15],9))
a = [2, 3 , 7 , 11, 15]


def twoSum_fast(num,target):
    result = {}
    for i in range(len(num)):
        if num[i] in result:
            return [result[num[i]],i]
        else:
            result[target-num[i]] = i
print(twoSum_fast(a,9))

