class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i_index, i in enumerate(nums):
            for j_index, j in enumerate(nums):
                if i + j == target and i_index != j_index:
                    return [i_index, j_index]


        