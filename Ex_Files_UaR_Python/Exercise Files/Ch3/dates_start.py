#
# Example file for working with date information
# (For Python 3.x, be sure to use the ExampleSnippets3.txt file)
from datetime import date
from datetime import time
from datetime import datetime

## DATE OBJECTS
# Get today's date from the simple today() method from the date class
today = date.today()
print "Today's date is ", today
  
 # print out the date's individual components
print "Date Components: ", today.day, today.month, today.year

# retrieve today's weekday (0=Monday, 6=Sunday)
print "Today's Weekday #: ", today.weekday()  

# Get the current time
t = datetime.time(datetime.now())
print "The current time is ", t

# weekday returns 0 (monday) through 6 (sunday)
wd = date.weekday(today)  
# Days start at 0 for Monday 
days = ["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
print "Today is day number %d" % wd
print "Which is a " + days[wd]


# re-declaring the variable works
f = "abc"
print "whatever: " %f
  
def main():

 if __name__ == "__main__":
  main();
  