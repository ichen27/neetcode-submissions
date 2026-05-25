class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        if len(nums) == 0:
            return 0

        index = 0

        while index <= len(nums) - 1:

            if nums[index] == val:
                nums.pop(index)
                continue

            index += 1

        return len(nums)

