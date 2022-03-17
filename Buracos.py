t = int(input())
i = 0
while(i < t and t <= 40):
    
    try: 
        buracos = 0 
        palavra = input() 
        for letra in palavra: 
        
            if(letra == "B"): 
                buracos += 2
            elif(letra == "A" or letra == "O" or letra == "P" or letra == "R" or letra == "D" or letra == "Q"): 
                buracos += 1
        print(buracos)
        i += 1 
        buracos = 0 
    except EOFError: 
        break