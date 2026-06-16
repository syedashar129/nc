class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = '+-/*'
        for token in tokens:
            if token not in operators:
                # number
                stack.append(int(token))
            else:
                # operator
                right = stack.pop()
                left = stack.pop()

                output = self.do_operation(token, left, right)
                stack.append(output)
        return stack[-1]

    def do_operation(self, operator, left, right):
        output = 0
        if operator == '+':
            output = left + right
        elif operator == '-':
            output = left - right
        elif operator == '/':
            output = left // right
        else:
            output = left * right
        return output
        




# init stack
# loop thorugh tokens
#   if num --> add to stack as int
#   else --> pop left and right + do operation + add to stack
#  return stack[-1]

# time - O(n)
# space - O(n)