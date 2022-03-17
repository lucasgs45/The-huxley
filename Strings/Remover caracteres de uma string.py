linha1 = input() 
linha2 = input() 

if(len(linha1) <= 80 and len(linha2) <= 80): 
    for letters in linha1: 
        if(not(letters in linha2)): 
            print(letters,end="")
