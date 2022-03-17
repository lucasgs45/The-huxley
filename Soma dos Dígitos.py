entrada = int(input())
tamanho = len(str(entrada)) 
saida = 0
for i in range(0,tamanho): 
    saida += (entrada // 10**i) % 10 
print(saida)
