print("=====NOTAS ESCOLAR======")

nota1 = float(input("digite primeira nota: "))
nota2 = float(input("digite segunda nota: "))
nota3 = float(input("digite terceira nota: "))

media = (nota1 + nota2 + nota3) /3
print(f"MEDIA: {media:.2f}")

if media >= 7:
    print("aprovado!!")
elif media >= 5:
    print("recuperação")
else:
    print("reprovado")