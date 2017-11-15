#ClassOverloadFunctions.py

class ClassWithOverloadFunctions:

    def methodWithOneIntParam(self, pI11) :
        print('called method with one arg:', pI11)

    def methodWithOneStringParam(self, pS11) :
        print('called method with one arg:', pS11)

    def methodWith3Params(self, p31, p32, p33) :
        print('called method with one arg:', p31, p32, p33)
    
    def defaultFunction(self):
        print('no method found to hadle ')

    def __repr__(self):
        return "<ClassWithOverloadFunctions: name=%s>" % (__name__)

    def genericFunction(self, *args):
        """ Depending on parameters received, it calls appropriate function """
        
        print('\n----------\nEntered genericFunction with', len(args), 'param(s) ...')
        # Note: calling genericFunction(101, 201) will return <<=>>    (<__main__.ClassWithOverloadFunctions object at 0x0030B430>, 101, 201)
        # 1st (implicit ) parameter is always self

        #print('Input parameters :', args)
        #print(type(args)) # <class 'tuple'> 
        
        # convert tuple to List
        inputValuesList = list(args) # note: using  '[args]' instead of 'list(args)' will create a list containing a tuple
        #print(type(inputValuesList)) # <class 'list'>
        #print('inputValues List : ', inputValuesList)


        # OK
        #[ print(x) for x in inputValuesList ]

        if len(args) == 1 and type(args[0]) == int : # Branch on number arguments
            print('calling methodWithOneIntParam')
            # You need to pass self as the first argument to all instance methods.
            self.methodWithOneIntParam(args[0])
        elif len(args) == 1 and type(args[0]) == str : # Branch on argument types (or isinstance())
            print('calling methodWithOneStringParam')
            self.methodWithOneStringParam(args[0])
        elif len(args) == 3 : # Branch on argument types (or isinstance())
            print('calling methodWith3Params')
            self.methodWith3Params(args[0], args[1], args[2])            
        else :
            print('no method found to hadle ', len(args), ' input parameters')

if __name__ == '__main__':

    instance1 = ClassWithOverloadFunctions()
    
    #ok
    # print(instance1.genericFunction.__doc__)

    instance1.genericFunction(101)
    instance1.genericFunction('string1')
    instance1.genericFunction(101, 102)
    instance1.genericFunction(101, 102, 103)
    print(instance1.__repr__)