def paresDivisibles(k, a):
    count = 0  # Inicializamos un contador en 0
    
    # Iteramos sobre todos los pares de elementos en la lista a
    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            if (a[i] + a[j]) % k == 0:
                count += 1  # Si la suma es divisible por k, incrementamos el contador
    
    return count  # Retornamos el contador como resultado

# Ejemplo de uso
k = 25
a = [2,10,45,67,110,200,5,24,8,4,3,10,100,89,59,100,234,56,78,90,67,23,32,45,89,90,100,101]
resultado = paresDivisibles(k, a)
print(f"El número de pares (i, j) donde i < j y (i + j) es divisible por {k} es: {resultado}")
