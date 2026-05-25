class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Length of longest consectutive sequence of elements that can be formed
        # each element needs to be exactly 1 greater than the previous element
        # Dont need to be consectutive in original array

        # 1: Sort and iterate through
        # O(nlogn) worst case

        # 2: Convert to set
        # O(n)
        # Only check the start of 

        longest = 0
        curr = 0
        numSet = set(nums)

        for i in nums:
            
            # Start of sequence
            if i - 1 not in numSet:
                curr = 1
                j = 1

                while i + j in numSet:
                    curr += 1
                    j += 1

                longest = max(longest, curr)

            
        return longest








        