# have the function FirstReverse(str) take the str parameter being passed and return the string in reversed order.
# For example: if the input is "Hello World and Coders" then your program should return the string 'sredoC dna dlroW olleH'
def main():
    def FirstReverse(str):
        # code goes here
        str = ''.join(reversed(str))
        return str
    print FirstReverse("Hello World and Coders")
if __name__== "__main__": main()