class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        start_pointer = 0
        end_pointer = len(s) - 1

        while start_pointer < end_pointer:
            s[start_pointer], s[end_pointer] = s[end_pointer], s[start_pointer] 
            start_pointer += 1
            end_pointer -= 1

# 2 pointer: Converging pointers
# time: O(n)
# space: O(1)