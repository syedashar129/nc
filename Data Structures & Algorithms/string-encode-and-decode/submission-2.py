class Solution:

    def encode(self, strs: List[str]) -> str:
        # list of strings --> str
        final_str = ""
        for word in strs:
            final_str += f'{len(word)}#{word}' 
        return final_str #  5#Hello5#World

    def decode(self, s: str) -> List[str]:
        # str --> list of str
        # 5#Hello5#World --> ['Hello', 'World']
        i = 0
        res = []
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            
            length_word = int(s[i : j])
            word = s[j + 1 : j + 1 + length_word]
            res.append(word)
            i = j + 1 + length_word
        
        return res





        


# brute: 
# optimal: 

# encode: 
    # loop strs
        # append each one to a single str w /delimiter
    # n / m (input + delimiter)

# decode
    # loop str
        # 

