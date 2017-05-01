class Duck:
    def __init__(self, **kwargs):
        print ('Constructor!')
        self.variables = kwargs

    def quack(self):
        print ("quaaaaack", self._v)

    def walk(self):
        print ("Walk like a duck!", self._v)

    def set_variable(self, k, v):
        self.variables[k] = v

    def get_variable(self, k):
        return self.variables.get(k, None)
def main():
    donald = Duck(feet = 2)
    donald.set_variable('color', 'Blue')
    donald.set_variable('size', 'medium')
    print (donald.get_variable('color'))
    print (donald.get_variable('feet'))
    print (donald.get_variable('size'))



if __name__== "__main__": main()

