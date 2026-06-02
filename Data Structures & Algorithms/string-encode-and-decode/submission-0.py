class Solution:

    def encode(self, strs: List[str]) -> str:
        
        endodedString = ""

        for strr in strs:

            for char in strr:
                if endodedString == "":
                    endodedString += str(ord(char))
                else:
                    endodedString += "="+str(ord(char))
                
            endodedString+="-"

        return endodedString

    def decode(self, s: str) -> List[str]:
        out = []
        stringg  = ""
        asc_value = ""
        for char in s:
            if char == "-":
                if asc_value != "":
                    stringg += chr(int(asc_value))
                out.append(stringg)
                stringg = ""
                asc_value = ""
            elif char == "=":
                if asc_value != "":
                    stringg += chr(int(asc_value))
                asc_value = ""
            
            else:
                asc_value += char
        
        return out



