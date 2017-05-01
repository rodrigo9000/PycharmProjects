# Description: For this challenge you will be comparing two numbers and determining which one is greater.
# Challenge
# Using the Python language, have the function CheckNums(num1,num2) take both parameters being passed and return the string
# true if num2 is greater than num1, otherwise return the string false. If the parameter values are equal to each other then
# return the string -1.
# Sample Test Cases
# Input:3 & num2 = 122
# Output:"true"
#
# Input:67 & num2 = 67
# Output:"-1"
def main():
    def CheckNums(num1, num2):
        if ( num2 > num1):
            return "true"
        elif (num1 == num2):
            return "-1"
        else:
            return "false"
    print CheckNums(67, num2=67)
if __name__== "__main__": main()