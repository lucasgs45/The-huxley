#Inicializa
n = int(input())
m = int(input())
i = n 
aux = 0
if(m > n): #Verifica se m > n
    while i <= m: #Itera de n ate m
        if(i % n == 0 and i > aux): #Se i for maior que aux, troca de valor. Assim, obtemos o valor maximo
            aux = i
        i += 1
    print(aux)
else: #O caso contrario nunca ira ter multiplos menores que m
    print("sem multiplos menores que %d" %m)
