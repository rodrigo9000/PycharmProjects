# Challenge
# Using the Python language, have the function SimpleSymbols(str) take the str parameter being passed and determine if it
# is an acceptable sequence by either returning the string true or false. The str parameter will be composed of + and = symbols
# with several letters between them (ie. ++d+===+c++==a) and for the string to be true each letter must be surrounded by a + symbol.
# So the string to the left would be false. The string will not be empty and will have at least one letter.
# Sample Test Cases
# Input:"+d+=3=+s+"
# Output:"true"
#
# Input:"f++d+"
# Output:"false"
def main():
    def SimpleSymbols(str):
        result = ''
        # test if the first character or last are alphabetic. If true, return string 'false'
        if (str[0].isalpha() | str[-1].isalpha()):
            result = "false"
            return result
        # Lopp through string characters
        for i, v in enumerate(str):
            # Test if it's an alphabetic character and the previous char and the later char are '+' symbols
            if (str[i].isalpha() and str[(i - 1)] == '+' and str[(i + 1)] == '+'):
                result = "true"
            # Test if it's an alphabetic character and the previous char OR later char are NOT '+' symbols
            elif (str[i].isalpha() and (str[(i - 1)] != '+' or str[(i + 1) != '+'])):
                result = "false"
                break
        return result
    print SimpleSymbols('f++d+')


if __name__== "__main__": main()