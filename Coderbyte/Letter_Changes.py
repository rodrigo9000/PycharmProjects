# Using the Python language, have the function LetterChanges(str) take the str parameter being passed and modify it
# using the following algorithm. Replace every letter in the string with the letter following it in the
# alphabet (ie. c becomes d, z becomes a). Then capitalize every vowel in this new string (a, e, i, o, u)
# and finally return this modified string.
# Sample Test Cases
# Input:"hello*3"
# Output:"Ifmmp*3
#
# Input:"fun times!"
# Output:"gvO Ujnft!"
def main():
    def LetterChanges(str):
        # Creates a list with the string letter [eg. 'h', 'e', 'l', 'l', 'o'
        str = list(str)
        # Loop through the letters
        for i, item in enumerate(str):
            # Test if item carries alphanumeric value
            if (item.isalpha()):
                # return the ASCII order number and add 1 to it. visit theasciicode.com.ar/ for reference
                item = (ord(item)) + 1
                # Convert the number back to character
                item = chr(item)
                # Put the character back to the same spot in the list
                str[i] = item
        # Evaluate if it's a vowel. If true, capitalize it.
        for i, v in enumerate(str):
            if v in ('a', 'e', 'i', 'o', 'u'):
                str[i] = v.upper()
        # joint the list to a string and return it
        str = ''.join(str)
        return str

    print LetterChanges('fun times!')

if __name__== "__main__": main()