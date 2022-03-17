linhas = int(input()) 
if(1 <= linhas <= 1000):
    
    for i in range(1,linhas+1): 
        numero = i 
        quadrado = i**2 
        cubo = i**3 
        print("%d %d %d"%(numero,quadrado,cubo))