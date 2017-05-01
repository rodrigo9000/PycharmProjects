# Have the function FirstFactorial(num) take the num parameter being passed and return the factorial
# of it. (eg. if num = 4, return (4*3*2*1).
def main():
    def FirstFactorial(num):
        # code goes here
        import math
        num = math.factorial(num)
        return num

    print FirstFactorial(8)
if __name__== "__main__": main()