# Using the Python language, have the function LetterCapitalize(str) take the str parameter being passed and capitalize
# the first letter of each word. Words will be separated by only one space
def main():
    def LetterCapitalize(str):
        print str.title()

    LetterCapitalize('i ran there')

if __name__== "__main__": main()