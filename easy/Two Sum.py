import time
from typing import List

start = time.time()


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

# 测试
s = Solution()
result = s.twoSum([3,2,4], 6)
print(result)
end = time.time()
print(end - start)

# 大佬鼠
def twoSum(nums, target):
    """
    :param nums: List[int]
    :param target: int
    :return: list[int]
    """
    d = {}
    for index, num in enumerate(nums):
        if target - num in d:
            return [d[target - num], index]
        d[num] = index