import math
N  = int(input())
x = float(input())
cosx = 1
i=2
j = True
l = [1]
for _ in range(1,N):
    if j==True:
        elemento = (x**i)/math.factorial(i)
        elementor = round(elemento,2)
        elementor = -1*elementor
        l.append(elementor)
        cosx-=elemento
        j = False
        i+=2
    elif j==False:
        elemento=(x**i)/math.factorial(i)
        elementor=round(elemento,2)
        l.append(elementor)
        cosx+=elemento
        j=True
        i+=2
print(*l,sep=", ")
cosxr = round(cosx,2)
print(cosxr)