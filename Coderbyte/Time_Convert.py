# Description: For this challenge you will be determining the difference in hours and minutes between two given times.
# Challenge
# Using the Python language, have the function TimeConvert(num) take the num parameter being passed and return the number
# of hours and minutes the parameter converts to (ie. if num = 63 then the output should be 1:3). Separate the number of
# hours and minutes with a colon.
# Sample Test Cases
# Input:126
# Output:"2:6"
#
# Input:45
# Output:"0:45"
def main():
    def TimeConvert(num):
        # get the hour
        hour = (num / 60)
        # get the minutes
        min = (num % 60)

        return (str(hour) + ':' + str(min))

    print TimeConvert(10)
if __name__== "__main__": main()