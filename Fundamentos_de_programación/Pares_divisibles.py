def paresDivisibles(k,a):
    contador = 0
    for num_1 in range(len(a)):
        for num_2 in range(num_1+1,len(a)):
            if (a[num_1] + a[num_2]) % k == 0:
                contador+=1
    return contador