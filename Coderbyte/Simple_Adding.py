# Description: For this challenge you will be adding up all the numbers from 1 to a certain argument.
# Using the Python language, have the function SimpleAdding(num) add up all the numbers from 1 to num.
# For example: if the input is 4 then your program should return 10 because 1 + 2 + 3 + 4 = 10. For the test
# cases, the parameter num will be any number from 1 to 1000.
def main():
    def SimpleAdding(num):
        sum = 0
        for n in range(1, num + 1):
            sum = sum + n
        num = sum
        return num

    print SimpleAdding(12)

if __name__== "__main__": main()