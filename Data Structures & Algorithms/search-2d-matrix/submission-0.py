class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        one_d_list = []
        for lis in matrix:
            one_d_list.extend(lis)


        left = 0
        right = len(one_d_list) - 1

        while left <= right:

            mid = (left + right)//2

            if target > one_d_list[mid]:
                left = mid + 1
            
            elif target < one_d_list[mid]:
                right = mid - 1

            else:
                return True
        
        return False
        