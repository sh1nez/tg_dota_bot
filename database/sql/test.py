def asd():
    print(123)

def dsa():
    print(312)

def new_func():
    print('ERROR')

a = asd
b = dsa
c = a
c = new_func
tup = (a, b, c)

for i in tup:
    i()