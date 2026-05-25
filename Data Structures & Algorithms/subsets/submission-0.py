class Solution:
    
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # Backtracking 
        # Recursion

        return self.recursion_helper(nums, [], [], -1)



    def recursion_helper(self, nums: List[int], total: List[List[int]], subset: List[int], index):
        index += 1
        if index >= len(nums):
            return total.append(subset)

        self.recursion_helper(nums, total, subset, index)
        subset = subset + [nums[index]]
        self.recursion_helper(nums, total, subset, index)


        
        return total



        