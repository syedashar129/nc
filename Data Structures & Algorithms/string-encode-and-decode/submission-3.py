class Solution:

    def encode(self, strs: List[str]) -> str:
        final_str = ""

        for word in strs:
            word_length = len(word)
            word_to_append = str(word_length) + '#' + word
            final_str += word_to_append
        return final_str


    def decode(self, s: str) -> List[str]:
        i = 0
        final_arr = []

        while i < len(s):
            j = i

            while s[j] != '#':
                j+=1
            
            word_length = int(s[i:j])
            end = j + 1 + word_length
            word = s[j + 1 : end]
            final_arr.append(word)
            
            i = end
        
        return final_arr




# encode 
    # ["Hello","World"] --> "5#Hello5#World"
    
    # m + n / m + n

    # final_str 
    # loop strs
        # get length
        # add to final_str --> length + # + str
    # return final_str

# decode 
    # "5#Hello5#World" --> ["Hello","World"]

    # m + n / m + n

    # i = 0
    # arr 
    # while loop until S
        # get length 
        # *get word 
        # add word
        # update i 
    # return arr 

