class Solution:
    def isValid(self, s: str) -> bool:
        parenthesis_map = {
            '(' : ')', 
            '{' : '}',
            '[':  ']'
        }

        stack = []

        for char in s:
            if char in parenthesis_map: # open 
                stack.append(char)
            elif stack and parenthesis_map[stack[-1]] == char : # closed
                stack.pop()
            else:
                return False
            
        return not stack 

    
# open bracket closed by closed bracket
# open brackets closed in correct order
# close has open brakccket 
# return true or false

# brute: 
# optimal: stack + map (n (iterate s) / n (stack))

# define the needed open closed pairs using map --> set amount O(1)
# stack
# loop s
    # if opening --> add to stack 
    # if closing --> look at top of stack and pop from stakc if correct 

# return not stack

