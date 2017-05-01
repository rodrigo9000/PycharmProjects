class Car:
    # use dictionary to get parameters
    def __init__(self, **kwargs):
        self.variables = kwargs  # i can set default values with ()

    def set_car(self, k, v):
        self.variables[k] = v

    def get_car(self, k):
        return self.variables.get(k, None)
def main():


        myCar1 = Car(make='KIA', model='Rio5', color='Black', year=2011, price=9000)
        print (myCar1.get_car('model'))
        print (myCar1.get_car('price'))
        print ""
        myCar2 = Car()
        myCar2.set_car('make', 'Honda')


if __name__== "__main__": main()