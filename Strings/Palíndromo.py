n = int(input())
for i in range(0,n): 
    string = input()
    if(len(string) <= 255):
        string = string.replace(" ","") 
        string = string.lower() 
        if(string == string[::-1]): 
            print("SIM")
        else:
            print("NAO")
