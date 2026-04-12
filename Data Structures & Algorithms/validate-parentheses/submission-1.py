class Solution:
    def isValid(self, s: str) -> bool:

        bracket_map = {"{":"}","(":")","[":"]"}
        stack = []

        for i in range(len(s)):
            if s[i] in bracket_map.keys():
                stack.append(s[i])
            else:
                if len(stack) > 0:
                    if bracket_map[stack[-1]] == s[i]:
                        stack.pop()
                    else:
                        return False
                else:
                    return False


        
        if len(stack) == 0:
            return True
        return False