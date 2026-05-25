class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        non_zero = 1
        output = []
        zeros = 0

        for i in nums:
            product *= i
            if i == 0:
                zeros += 1
            else:
                non_zero *= i
        for i in nums:
            if i == 0:
                if zeros > 1:
                    temp = 0
                else:
                    temp = non_zero
            else:
                temp = int(product / i)
            output.append(temp)
        
        return output
        