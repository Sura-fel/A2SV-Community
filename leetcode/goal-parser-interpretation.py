class Solution:
    def interpret(self, command: str) -> str:
        i = 0
        st = ""
        while i < len(command):
            if command[i] == "G":
                st += "G"
                i += 1
            elif command[i+1] == ")":
                st += "o"
                i += 2
            else:
                st += "al"
                i += 4
        return st
