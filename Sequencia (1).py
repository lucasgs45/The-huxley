x,y = input().split()
x = int(x)
y = int(y)
if((1 <= x <= 20) and (x <= y <= 100000 )):
    
    for i in range(1,x+1):
        if(i % x != 0):  
           print("%d"%i,end = " ") 
        else: 
            print("%d"%i)
           
            for j in range(x+1,y+1): 
                if(j % x != 0): 
                    print("%d"%j, end = " ")
                else:
                    print("%d"%j)