# Given an array of integers, return indices of the two numbers such that they add up to a specific target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# Example:
#
# Given nums = [2, 7, 11, 15], target = 9,
#
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].
from typing import List

class Solution:
    @staticmethod
    def two_sum(nums: List[int], target: int) -> List[List]:
        number_map = {number: number for number in nums}
        results = []
        for number in nums:
            if (target - number) in number_map:
                results.append([number, (target - number)])
                del(number_map[number])

        return results


result = Solution.two_sum([11, 7, 15, 2], 9)
print(result)

result = Solution.two_sum([11, 7, 15, 2], 19)
print(result)
