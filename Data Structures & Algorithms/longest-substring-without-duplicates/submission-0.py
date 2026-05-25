class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Sliding window
        # Right pointer keep going as long as it doesn't hit a duplicate
        ## If hits a duplicate, left pointer keeps going as long as there is no duplicate
        ## Or until left pointer == right pointer
        ## Variable to store length of longest string

        # Use hash map
        # stores the count of every character
        # If any value in the hash map > 1
        # While loop
        # keep moving left pointer and subtracting from hash map
        # Exit while and keep moving right pointer and adding to hash map

        l = 0
        longest = 0
        charsUsed = {}

        for r in range(len(s)):

            if s[r] in charsUsed:
                charsUsed[s[r]] += 1
            else:
                charsUsed[s[r]] = 1
            while 2 in charsUsed.values():

                charsUsed[s[l]] -= 1
                l += 1
            curr_len = (r+1) - l
            if curr_len > longest:
                longest = curr_len

        return longest




        