class Solution:
    def __init__(self):
        self.mem = {}

    def lengthOfLIS(self, nums: List[int]) -> int:
        
        def dpHelper(index, last):
            if index >= len(nums):
                return 0
            


            if nums[last] < nums[index] or last == -1:
                if (index, last) in self.mem:
                    return self.mem[(index, last)]

                
                take = 1 + dpHelper(index + 1, index)
                skip = 0 + dpHelper(index + 1, last)

                self.mem[(index, last)] = max(take, skip)

                return self.mem[(index, last)]


            elif nums[last] >= nums[index]:
                if (index, last) in self.mem:
                    return self.mem[(index, last)]

                self.mem[(index, last)] = 0 + dpHelper(index + 1, last)

                return self.mem[(index, last)]





        
        return dpHelper(0, -1)



        