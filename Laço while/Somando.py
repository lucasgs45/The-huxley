num1 = int(input())
num2 = int(input())
sum_numbers = 0
if(num2 >= 0): 
    i = num1 
    while(i <= num2):  
        if(i >= 0):
            sum_numbers += i
            i += 1
            continue 
        i += 1
    print(sum_numbers)
else:

    i = num2
    while(i <= num1): 
        if(i >= 0):
            sum_numbers += i
            i += 1
            continue
        i += 1
    print(sum_numbers)
