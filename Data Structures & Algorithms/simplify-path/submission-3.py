class Solution:
    def simplifyPath(self, path: str) -> str:
        paths = path.split('/')
        stack = []

        for char in paths:
            if char == '..':
                if stack: 
                    stack.pop()
            elif char != '' and char != '.':
                stack.append(char)

        return '/' + '/'.join(stack)
    
# split path
# stack 

# loop path 
#   if .. --> pop
#   elif not empty ornot . --> add

# join stac with '/'

# time: O(n)
# space: O(n)