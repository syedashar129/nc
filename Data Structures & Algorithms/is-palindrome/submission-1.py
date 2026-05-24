class Solution:
    def isPalindrome(self, s: str) -> bool:
        start_pointer = 0
        end_pointer = len(s) - 1

        while start_pointer < end_pointer:
            while not s[end_pointer].isalnum() and start_pointer < end_pointer:
                end_pointer -=1
            while not s[start_pointer].isalnum() and start_pointer < end_pointer :
                start_pointer +=1
            if s[start_pointer].lower() == s[end_pointer].lower():
                start_pointer +=1
                end_pointer -=1
            else:
                return False
        return True

# 2 pointer
# converging pointers

# time: O(n)
# space: O(1)

# ignore non alpha spaces
# make sure that we lower when comparing 


# 2 pointers
# whie start pointer < end pointer:
#   if end pointer is not alpha --> decrease 
#   if start pointer is not alph a--> increase
#   if lower(start) == lower(end)
#       keep going
#   else:
#       return False
# return true 