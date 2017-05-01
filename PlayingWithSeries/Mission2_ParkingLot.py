class Car:
    # class variable
    hst_tax = .13
    # use dictionary to get parameters
    def __init__(self, make, model, color = None, year = None, price = None):
        self.make = make
        self.model = model
        self.color = color
        self.year = year
        self.price = price
        self.tax = price * Car.hst_tax

def main():
    myCar1 = Car(make = 'KIA', model = 'Rio5', color = 'Black', year = 2011, price = 9000)
    print myCar1.model
    print myCar1.price
    print myCar1.tax
    print ""
    myCar2 = Car(make = 'Honda', model = 'Civic', color = 'Silver', year = 2013, price = 11000)
    print myCar2.model
    print myCar2.price
    print myCar2.tax
    print ""

    print hasattr(myCar2, 'price')
if __name__== "__main__": main()