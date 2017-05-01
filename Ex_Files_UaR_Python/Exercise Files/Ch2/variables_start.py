# 
# Example file for variables
# (For Python 3.x, be sure to use the ExampleSnippets3.txt file)

# Comment
f = 0;
print f

# re-declaring the variable works
f = "abc"
print f

# Global vs. local variables in functions
def someFunction():
  global f
  f = "def"
  print f
  
someFunction()