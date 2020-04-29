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
    def two_sum(nums: List[int], target: int) -> List[List[int]]:
        number_map = {number: number for number in nums}
        results = []
        for number in nums:
            if (target - number) in number_map:
                results.append([number, (target - number)])
                del (number_map[number])

        return results

class SolutionX:
    @staticmethod
    def two_sum(nums: List[int], target: int) -> List[int]:
        values = {}
        counter = 0
        for number in nums:
            if target - number in values.keys():
                return [values.get(target - number), counter]
            values[number] = counter
            counter += 1


result = Solution.two_sum([11, 7, 15, 2], 9)
print(result)

result = Solution.two_sum([11, 7, 15, 2], 19)
print(result)

result = Solution.two_sum([3, 2, 1], 6)
print(result)

result = SolutionX.two_sum([3, 2, 4], 6)
print("found: ", result)

result = SolutionX.two_sum([3, 3], 6)
print("found: ", result)
