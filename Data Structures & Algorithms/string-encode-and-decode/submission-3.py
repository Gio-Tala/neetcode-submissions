class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for word in strs:
            encoded_word = "-".join(str(ord(letter)) for letter in word)
            encoded_str += encoded_word + ","

        return encoded_str

    def decode(self, s: str) -> List[str]:
        if s == "":
            return []
        decoded_list = []
        for word in s[:-1].split(","):
            curr_word = ""
            if word == "":
                decoded_list.append("")
                continue
            for asc in word.split("-"):
                curr_word += chr(int(asc))
            decoded_list.append(curr_word)
        return decoded_list
