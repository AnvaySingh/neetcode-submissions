class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for word in strs:
            encoded_string += f"{len(word)}#{word}"
        return encoded_string

    def decode(self, s: str) -> List[str]:
        decoded_list = []
        i = 0
        while i < len(s):
            
            delim_pos = s.find('#', i) #looks for character # starting from index i, it returns the int index pos of character #
            length = int(s[i:delim_pos]) #slice the string from index i to int delim_post(but not including delim_post index)
            word = s[delim_pos + 1 : delim_pos + 1 + length]
            decoded_list.append(word)
            i = delim_pos + 1 + length
        return decoded_list