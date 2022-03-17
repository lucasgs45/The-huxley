n = int(input())
if(0 < n < 1000): 
     
    for i in range(1,n+1): 
        numero = i
        quadrado = i ** 2 
        cubo = i ** 3 
        print("%d %d %d"%(numero,quadrado,cubo))
       
        quadrado += 1 
        cubo += 1 
        print("%d %d %d"%(numero,quadrado,cubo))