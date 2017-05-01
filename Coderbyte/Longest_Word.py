# Using the Python language, have the function LongestWord(sen) take the sen parameter being passed
# and return the largest word in the string. If there are two or more words that are the same length,
# return the first word from the string with that length. Ignore punctuation and assume sen will not be empty.
import re
def main():
    def LongestWord(sen):
        # Creates a list of individual words
        sen = sen.split()
        max = 0

        # Loop through the list of words
        for word in sen:
            # search for alphabetical letters ( 1 or multiple).
            word = (re.search(r'[\w]+', word)).group()
            # Check the real size of the string
            count = len(word)
            if (count > max):
                max = count
                sen = word
        return sen


    print LongestWord('my new string sprint!!!')

if __name__== "__main__": main()