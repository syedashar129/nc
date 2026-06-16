class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # similar to brackets question
        # look at the end and then pop until the end 
        # keep a stack to maintain
        stack = []
        operators = '+-*/'
        for char in tokens:
            if char not in operators:
                stack.append(int(char))
            else: 
                operator = char
                right = stack.pop()
                left = stack.pop()
                evaluated_val = self.do_operation(left, right, operator)
                stack.append(evaluated_val)
        return stack.pop()


    
    def do_operation(self, left, right, operator):
        if operator == '+':
            return left + right
        
        elif operator == '-':
            return left - right
        
        elif operator == '*':
            return left * right
        
        elif operator == '/':
            return left//right


                



# tokens
# [1 , 2, +] --> [3]
# [3, 3, *] --> [9]
# [9, 4,  -] --> [5]
# return top of stack

# need to make sure that we do (second popped element - first popped element) -- each popped PRE PENDS
#
