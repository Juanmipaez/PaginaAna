Numero_de_casos = int(input())
Coordenada_X = []
Coordenada_Y = []

for numeros in range(Numero_de_casos):
    numero_x = float(input())
    numero_y = float(input())
    Coordenada_X.append(numero_x)
    Coordenada_Y.append(numero_y)

def cuadrantes(x,y):
    if x== 0 and y == 0:
        return 0
    elif x==0 and y!=0:
        return "Y"
    elif y==0 and x!=0:
        return "X"
    elif x>0 and y>0:
        return 1
    elif x<0 and y>0:
        return 2
    elif x<0 and y<0:
        return 3
    elif x>0 and y<0:
        return 4

for index in range(Numero_de_casos):
    print(cuadrantes(Coordenada_X[index],Coordenada_Y[index]))
