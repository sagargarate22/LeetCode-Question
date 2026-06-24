class Solution:
    def decodeString(self, s: str) -> str:
        i = 0 

        def decode() -> str:
            nonlocal i
            res = ""
            num = ""

            while i < len(s):
                if s[i].isdigit():
                    num += s[i]
                    i+=1
                elif s[i] == '[':
                    i+=1
                    res += decode() * int(num)
                    num = ""
                elif s[i] == ']':
                    i += 1
                    return res
                else:
                    res += s[i]
                    i += 1
            
            return res
        
        return decode()

