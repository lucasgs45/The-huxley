n = int(input())
m = int(input())
while m >= n:
    if(n % 2 == 0): 
        n += 1
        continue
    else:
        print(n)
        n += 1