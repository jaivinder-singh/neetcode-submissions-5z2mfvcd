class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            compli = target - num

            if compli in seen:
                return [seen[compli], i]
                

            seen[num] = i