"""
Copyright MIT BWSI Autonomous RACECAR Course
MIT License
Summer 2023

Code Clash #12 - Braces Brackets & Bows Balance (balancechecking.py)


Author: Ali Qattan

Difficulty Level: 6/10

Prompt: In your IDEs, your code editors and sometimes Vim (for those 
unfortunate ones who use vim) your application will yell at you when you don’t
have matching closing brackets. Python does not have that problem as much as
other languages like Java and C which rely heavily on curly braces.  You need 
to write a program that allows for that functionality so that every ‘[‘ and ‘{‘ 
and ‘(‘ has a matching ‘]’  ‘}’  ‘)’. 
This problem can be solved quickly using the right data structure.

Test Cases:
Input: {[()]}  Output: True

Input: [()]  Output: True

Input:{[{}]  Output: False

"""
class Solution:
    def isBalanced(self, parenthesis): 
            #type parenthesis: string
            #return type: boolean
            curly_counter = 0
            bracket_counter = 0
            Parenth_counter = 0
            #TODO: Write code below to returnn a boolean value with the solution to the prompt.
            for i in parenthesis:
                if i == "[":
                    bracket_counter +=1
                if i == "]":
                    bracket_counter -=1
 
                if i == "(":
                    Parenth_counter +=1
                if i == ")":
                    Parenth_counter -=1

                if i == "{":
                    curly_counter +=1
                if i == "}":
                    curly_counter -=1

            if curly_counter ==0 and bracket_counter ==0 and curly_counter == 0:
                return True
            else:
                return False

            pass

def main():
    str1=input()
    tc1= Solution()
    ans=tc1.isBalanced(str1)
    print(ans)

if __name__ == "__main__":
    main()
