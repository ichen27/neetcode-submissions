class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # array of nums
        # Find subarray that has the largest product within the array
        # Sequence of numbers of largest product
        # Moving window

        # Avoids Negative and zero values
        negLeft = 0
        negRight = 0
        negCount = 0
        negProduct = nums[0]

        # Only avoids 0 values
        # Keeps track of if negative values can increase product
        zeroLeft = 0
        zeroRight = 0
        zeroProduct = nums[0]

        largestProduct = nums[0]

        for i in nums:
            if i < 0:
                negCount += 1

        while True:
            # Keep multiplying
            # Until the currProdct <= 0 
            # Then move the entire window past that value

            # If the pointer that avoids negs and zeros is within the array
            if negRight < len(nums):
                # Keep multiplying and comparing with largest
                # Check if its the first product in the subarray if negRight = negLeft
                if negRight != negLeft:
                    negProduct *= nums[negRight]
                else: 
                    # If first integer in subarray, negProduct is the first element
                    negProduct = nums[negRight]

                largestProduct = max(largestProduct, negProduct)
                # Resets product whenever product <= 0
                # Sets right pointer to element after 0
                # Sets left pointer to the same index as the right pointer
                if negProduct <= 0:
                    negRight += 1
                    negleft = negRight
                else:
                    negRight += 1

            # If pointer that takes negatives into account is within the array
            if zeroRight < len(nums):
                # Keep multiplying
                if zeroRight != zeroLeft:
                    zeroProduct *= nums[zeroRight]
                else:
                    zeroProduct = nums[zeroRight]

                # checks if the value at the current pointer is negative
                # And checks how many neg numbers are left
                # If none, then reset

                # Compare with largest
                largestProduct = max(largestProduct, zeroProduct)

                # Zero then reset
                # After multiplying, if the val is negative and there is an even number of negs left, iterate until drop first negative
                if nums[zeroRight] < 0:
                    negCount -= 1
                    if negCount == 0 and zeroProduct < 0:
                        zeroRight += 1
                        index = 0
                        while index < negRight:
                            zeroProduct //= nums[index]
                            if nums[index] < 0:
                                break
                            index += 1
                        negLeft = index + 1
                        if index != negRight - 1:
                            largestProduct = max(largestProduct, zeroProduct)
                    else:
                        zeroRight += 1
                elif zeroProduct == 0:
                    zeroRight += 1
                    zeroLeft = zeroRight
                else:
                    zeroRight += 1
    
            print(f"Largest Product: {largestProduct}")
            print(f"Avoid all: Left: {negLeft}, Right: {negRight}, product: {negProduct}")
            print(f"Avoid zeros: Left: {zeroLeft}, Right: {zeroRight}, product: {zeroProduct}")

        
            if negRight >= len(nums) and zeroRight >= len(nums):
                break

        return largestProduct
            
        