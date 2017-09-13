#CollectionsMisc.py
L = [1,2,3]
D = {'a':1, 'b':2}

# L3=L[:],  D3 = D.copy()
# This way changes made from the other variables will change the copies, not the originals
L2, L3 = L, L[:]
D2, D3 = D, D.copy()

print('Before : L=', L, ', L2=', L2, ', L3=', L3) # L= [1, 2, 3] , L2= [1, 2, 3] , L3= [1, 2, 3]
L[1]=222
print('After : L=', L, ', L2=', L2, ', L3=', L3) # L= [1, 222, 3] , L2= [1, 222, 3] , L3= [1, 2, 3]

print('Before : D=', D, ', D2=', D2,  ', D3=', D3) #D= {'a': 1, 'b': 2} , D2= {'a': 1, 'b': 2} , D3= {'a': 1, 'b': 2}
D['b']='changed'
print('After : D=', D, ', D2=', D2,  ', D3=', D3) #D= {'a': 1, 'b': 'changed'} , D2= {'a': 1, 'b': 'changed'} , D3= {'a': 1, 'b': 2}

#The == operator tests 'value equivalence' : comparing all nested objects recursively
#The is operator tests 'object identity' :
#           whether the two are really the same object (i.e., live at the same address in memory).
print('L == L2, L is L2 :', L == L2, L is L2) # True True
print('L == L3, L is L3 :', L == L3, L is L3) # False False
print('D == D2, D is D2 :', D == D2, D is D2) # True True
print('D == D3, D is D3 :', D == D3, D is D3) #  False False
