
def main():
    # Lambda Function
    var = lambda x, y: x if x > y else y
    print "The greater is: ", var(3, 5)

    # Map function
    n = [4, 3, 2, 1]
    result = map(lambda x: x ** 2, n)
    print result

    # Filter Function
    print "Filtering elements less than 10: ", filter(lambda x: x < 10, result)

    # Reduce function - For example, reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) calculates ((((1+2)+3)+4)+5)
    print "Operation using Reduce function: ", reduce(lambda x, y: x + y, result)




if __name__== "__main__": main()