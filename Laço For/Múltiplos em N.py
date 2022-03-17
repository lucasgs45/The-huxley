multiplo = int(input()) 
x = int(input()) 
y = int(input())
quantidade = 0 

for i in range(x,y+1): 
    if(i % multiplo == 0):
        print(i)
        quantidade += 2
        
if(quantidade == 0): 
    print("INEXISTENTE")
