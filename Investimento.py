entrada = input().split()
capital = float(entrada[0])
juros = float(entrada[1])
anos = int(entrada[2])
montante = capital
contador = 0
trimestre = int((12*anos)/3)

for anos in range(1,trimestre+1): 
    contador = montante 
    montante = capital*(1+juros)**anos
    rendimento = (montante - contador) 
    print("Rendimento: %.2f Montante: %.2f"%(rendimento,montante))