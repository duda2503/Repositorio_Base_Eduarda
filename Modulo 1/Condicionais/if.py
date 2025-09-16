while True:
    numero = int(input("Digite um numero inteiro: "))   
    if numero % 2 == 0:
       print("O numero é PAR. ")
    else:
        print("o numero é IMPAR. ")
repetir = input("Deseja verificar outro numero?(s para sim): ")
if repetir.lover() != "S":
    print("progresso encerrado")
