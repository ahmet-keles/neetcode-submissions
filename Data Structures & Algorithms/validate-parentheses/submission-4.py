class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        if len(s) < 2:
            return False

        for i in range(len(s)):

            if s[i] == '(' or s[i] == '[' or s[i] == '{':
                stack.append(s[i])
                continue

            if not stack:
                return False

            c = stack.pop()
            if s[i] != ')' and c == '(' or s[i] != ']' and c == '[' or s[i] != '}' and c == '{':
                return False

        if not stack:
            return True

        return False