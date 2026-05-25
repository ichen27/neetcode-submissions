class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Variables: current count, pointer, max count
        # Palindrome, string that reads the same forwards and backward
        # Iterate through every value in string
        # Set of pointers entending from one value and extending from middle 2
        ## Satisifies odd and even length palindrome

        max_even = ""
        max_odd = ""
        odd_left = 0
        odd_right = 0
        stillOdd = True
        stillEven = True
        even_left = 0
        even_right = 0

        if len(s) == 1:
            return s[0]
        elif len(s) == 0:
            return ""

        for center in range(0, len(s)):
            if center - 1 >= 0 and center + 1 <= len(s) - 1:
                odd_left = center - 1
                odd_right = center + 1
            else:
                stillOdd = False
            if center + 1 <= len(s) - 1:
                even_left = center
                even_right = center + 1
            else:
                stillEven = False
            print(f"Center: {center}")
            stillOdd = True
            stillEven = True
            while stillOdd or stillEven:
                if s[odd_left] == s[odd_right] and stillOdd:
                    if len(s[odd_left:odd_right+1]) >= len(max_odd):
                        max_odd = s[odd_left:odd_right+1]
                    if odd_left - 1 >= 0 and odd_right + 1 <= len(s) - 1:
                        odd_left -= 1
                        odd_right += 1
                    else:
                        stillOdd = False
                else:
                    stillOdd = False
                
                if s[even_left] == s[even_right] and stillEven:
                    print(f"Current Even: {s[even_left:even_right+1]}")
                    if len(s[even_left:even_right+1]) >= len(max_even):
                        max_even = s[even_left:even_right+1]
                    if even_left - 1 >= 0 and even_right + 1 <= len(s) - 1:
                        even_left -= 1
                        even_right += 1
                    else:
                        stillEven = False
                else:
                    stillEven = False
            
            print(f"Max Even: {max_even}, Max Odd: {max_odd}")

        if len(max_even) >= len(max_odd):
            return max_even
        else:
            return max_odd



                










        