class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        point = 1
        for i in range(1,len(nums)):
            if nums[i] != nums[i -1]:
                nums[point] = nums[i]
                point += 1

        return point

        