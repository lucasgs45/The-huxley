quantidade = int(input()) 
resultado = 0
if(0 <= quantidade <= 10000): 
    
    for i in range(0,quantidade): 
        numero = int(input()) 
        resultado += numero 
print("%d\n"%resultado)