class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        output = []
        containsZero = False
        for num in nums:
            if num == 0:
                if containsZero == True:
                    product = 0
                else:
                    containsZero = True
            else:
                
                product *= num


        for num in nums:
            if containsZero == True and num == 0:
                output.append(int(product))
            elif containsZero == True and num != 0:
                output.append(0)
            else:

                output.append(int(product/num))

        return output

        

        