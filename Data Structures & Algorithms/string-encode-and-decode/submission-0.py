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
            delim_pos = s.find('#', i)
            length = int(s[i:delim_pos])
            word = s[delim_pos + 1 : delim_pos + 1 + length]
            decoded_list.append(word)
            i = delim_pos + 1 + length
        return decoded_list