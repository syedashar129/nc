class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for item in s:
            if item != ']':
                stack.append(item)
            else:
                substr = ''
                while stack and stack[-1] != '[':
                    substr = stack.pop() + substr
                stack.pop()

                # grab the digit
                k = ''
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                
                multiplied_substr = int(k) * substr
                stack.append(multiplied_substr)
        
        return "".join(stack)

# no white spaces and clean 
# k[x] --> k * x 
# stack question


# stack = []
# final_str = ''

# loop s
#   if not ] --. append 
#   else -> pop until the [
#   pop the [

#   grab the digits before it --> while digit
#   multiply the digit by the substr
#   add to end of stack

# return joined stack 

# time --> O(n) --> looping all of input
# space --> O(n) --> stack 