class Solution:
    def isPalindrome(self, s: str) -> bool:
        one = ""
        two = ""


        for i in s:
            if i.isalpha() == True or i.isdigit() == True:
                one = one + i
        
        for y in range(len(one) -1, -1, -1):
            two = two + one[y]


        if one.lower() == two.lower():
            return True
        else:
            return False