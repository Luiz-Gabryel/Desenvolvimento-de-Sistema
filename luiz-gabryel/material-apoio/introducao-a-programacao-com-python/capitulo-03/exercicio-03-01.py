# progrma que fala se o numero e int ou Float.

n1 = 5
n2 = 5.0
n3 = 4.3
n4 = -2
n5 = 100
n6 = 1.333

for numero in (n1, n2, n3, n4, n5, n6):
    if '.' in str (numero):
        print("Esse e float")
    else:
        print("Esse e int")