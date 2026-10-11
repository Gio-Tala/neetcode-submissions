class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str_list = []
        for word in strs:
            encoded_word = "-".join(str(ord(letter)) for letter in word)
            encoded_str_list.append(encoded_word + ",")
        

        return "".join(encoded_str_list)

    def decode(self, s: str) -> List[str]:
        if s == "":
            return []
        decoded_list = []
        for word in s[:-1].split(","):
            curr_word = []
            if word == "":
                decoded_list.append("")
                continue
            for asc in word.split("-"):
                curr_word.append(chr(int(asc)))
            decoded_list.append("".join(curr_word))
        return decoded_list
