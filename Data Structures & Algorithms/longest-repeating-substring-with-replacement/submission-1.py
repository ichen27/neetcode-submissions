class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Given string s, contains uppercase letters
        # integer k, how many letters you can replace
        # perform k replacements and return length of longest substring of one letter

        # 1. 
        # Count occurances of each letter
        # Take highest count
        # Issue might be if they are spread apart
        # ABBCDEFAWYZJA k = 2

        # 2.
        # Iterate through and for each iteration try replacing for as far as it can go
        # Maybe nested loop
        # Replace if not the same as first, don't if is
        # Break once can no longer replace and not the same character
        # Starting point:
        ## Don't start from a point if it was already used in a longer substring and it wasn't changed
        longest = 0

        for i in range(len(s)):
            currLength = 0
            replacements = 0
            #currStr = ""
            for j in range(i, len(s)):
                if replacements == k and s[j] != s[i]:
                    break
                if s[j] == s[i]:
                    currLength += 1
                    #currStr = currStr + s[i]
                else:
                    replacements += 1
                    currLength += 1
                    #currStr  = currStr + s[i]

            left = i - 1
            while replacements < k:
                if left < 0:
                    break
                if s[left] == s[i]:
                    currLength += 1
                else:
                    replacements += 1
                    currLength += 1

                left -= 1



            longest = max(longest, currLength)
                #print(currStr)





        return longest


