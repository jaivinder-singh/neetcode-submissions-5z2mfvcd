class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mapped = []
        for i in range(0,len(nums)):
            if nums[i] not in mapped:
                mapped.append(nums[i])
            else:
                return True
        return False

        