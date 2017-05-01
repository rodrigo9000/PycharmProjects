#
# Example file for working with conditional statements
# (For Python 3.x, be sure to use the ExampleSnippets3.txt file)

def main():
  x, y = 100, 10
   # conditional flow uses if, elif, else  
  if(x < y):
    st= "x is less than y"
  elif (x == y):
    st= "x is same as y"
  else:
      st= "x is greater than y"
  print st
  
if __name__ == "__main__":
  main()
