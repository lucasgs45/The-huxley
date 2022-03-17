n = int(input())
contador = 0
soma = 0.00
a = 1
b = 3
while contador < n:
    if n == 0:
        print('%.2f'%contador)
    elif contador == (n-1):
        print("{}/{}".format(a,b))
        soma = soma + (a/b)
    else:
        print("{}/{}".format(a,b), end="")
        soma = soma + (a/b)
        a += 1 
        b += 3
        if contador < (n - 1):
            print(" +", end=" ")
    contador += 1

print('%.2f'%soma)
