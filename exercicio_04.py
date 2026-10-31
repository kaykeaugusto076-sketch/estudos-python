num1 = float(input("PRIMEIRO NUMERO: "))
operacao = input("operação +-/*: ")
num2 = float(input("SEGUNDO NUMERO: "))

#operador de soma
if operacao == "+":
    print(f"RESULTADO: {num1 + num2}")

#operador de subtração
elif operacao == "-":
    print(f"RESULTADO: {num1 - num2}")

#operador de multiplicação 
elif operacao == "*":
    print(f"RESULTADO: {num1 * num2}")
elif operacao == "x":
    print("ERRO: operador invalido (x)")  
      

#operador de divisão
elif operacao == "/":
    if num2 == 0:
        print("Erro: nao é possível um numero ser dividido por zero.")
    else:
        print(f"RESULTADO: {num1 / num2}")

else:
    print(f"Erro: operador inválido ({operacao}). Use +, -, * ou /.")