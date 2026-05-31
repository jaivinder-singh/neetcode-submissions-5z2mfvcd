class NumArray:

    def __init__(self, nums: List[int]):

        self.preFixSum = []
        self.totalSum = 0
        for num in nums:
            self.totalSum += num
            self.preFixSum.append(self.totalSum)

        print(f'self.preFixSum{self.preFixSum}')
        

    def sumRange(self, left: int, right: int) -> int:

        preRight = self.preFixSum[right]
        preLeft = self.preFixSum[left - 1] if left > 0 else 0

        return preRight - preLeft
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)