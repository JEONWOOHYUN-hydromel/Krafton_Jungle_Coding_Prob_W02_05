# 스택 - Basic Calculator
# 문제 링크: https://leetcode.com/problems/basic-calculator/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        m = ""
        result = 0
        i = 0
        while i < len(s):
            cmd = s[i]
            if cmd == "(":
                par = 1
                i += 1
                while par != 0:
                    if s[i] == "(":
                        par+=1
                    elif s[i] == ")":
                        par-=1
                    
                    stack.append(s[i])
                    i+=1
                stack.pop()
                num = self.calculate("".join(stack))
                i-=1

            elif cmd == " ":
                i+=1
                continue
            elif cmd == "+":
                i+=1
                m = "+"
                continue
            elif cmd == "-":
                i+=1
                m = "-"
                continue
            else:
                num_stack = []
                while i < len(s) and s[i].isdigit():
                    num_stack.append(s[i])
                    i+=1
                i-=1
                num = int("".join(num_stack))
            
            if m == "" or m == "+":
                result += num
            elif m == "-":
                result =  result - num
            
            i+=1
            stack = []
        return result
            
