#-----------------------------------------------------------------------------------
#Projeto CTC34 - Parser de expressoes matematica em C                              |
#Arquivo: Reconhecedor de expressoes matematicas validas com numeros inteiros em C |
#Aceitação da Cadeia
#COMP-19                                                                           |
#2o Semestre                                                                       |
#                                                                                  |
#Grupo:                                                                            |
#Gabriela Lima                                                                     |
#Lindemberg Teixeira                                                               |
#Talize Facó                                                                       |
#                                                                                  |
#Professor: Forster S2                                                             |
#----------------------------------------------------------------------------------|
exp = input("Cadeia a ser avaliada:")
exp = exp.replace(" ", "")
list = []
for ch in exp:
    list.append(ch)
list.append("$")
print("\n")
print("Sequencia de simbolos:")
print(list)
print("\n")
i = 0
contpar= 0
est = "inicio"
print("Caminho de estados percorrido:")
for i in range(len(list)):
    if est == "inicio":
        if list[i].isnumeric():
            est = "num"
        elif list[i]=="(":
            est = "inicio"
            contpar = contpar+1
        elif list[i]=="+":
            est = "sinal_p"
        elif list[i]=="-":
            est = "sinal_n"
        else:
            est="rejeita"
            break
    elif est == "sinal_p":
        if list[i].isnumeric():
            est = "num"
        elif list[i]=="(":
            est = "inicio"
            contpar = contpar + 1
        else:
            est= "rejeita"
            break
    elif est == "sinal_n":
        if list[i].isnumeric():
            est = "num"
        elif list[i]=="(":
            est = "inicio"
            contpar = contpar + 1
        else:
            est= "rejeita"
            break
    elif est == "num":
        if list[i].isnumeric():
            est = "num"
        elif list[i]=="+" or list[i]=="-" or list[i]=="*" or list[i]=="/" or list[i]=="%":
            est = "operador"
        elif list[i] == "$" and contpar==0:
            est="aceita"
            break
        elif list[i] == "$" and contpar != 0:
            est="rejeita"
            break
        elif list[i]==")" and contpar != 0:
            est = "fpar"
            contpar = contpar -1
        else:
            est="rejeita"

    elif est == "operador":
        if list[i].isnumeric():
            est = "num"
        elif list[i]=="(":
            est = "inicio"
            contpar = contpar + 1
        elif list[i-1]=="+" and list[i]=="-":
            est = "operador"
        elif list[i-1]=="-" and list[i]=="+":
            est = "operador"
        elif (list[i-1]=="*" or list[i-1]=="%" or list[i-1]=="/") and (list[i]=="+" or list[i]=="-"):
            est = "operador"
        else:
            est = "rejeita"
            break
    elif est == "fpar":
        if list[i] == "$" and contpar==0:
            est="aceita"
            break
        elif list[i] == "$" and contpar != 0:
            est="rejeita"
            break
        elif list[i] == ")" and contpar == 0:
            est="rejeita"
            break
        elif list[i]==")" and contpar != 0:
            est = "fpar"
            contpar = contpar - 1
        elif list[i]=="+" or list[i]=="-" or list[i]=="*" or list[i]=="/" or list[i]=="%":
            est = "operador"
        else:
            est = "rejeita"
            break
    print(est)
print("\n")
if est == "rejeita":
    print("A cadeia " + str(exp) + " constitui uma expressao matematica INVALIDA")
if est == "aceita":
    print("A cadeia " + str(exp) + " constitui uma expressao matematica VALIDA")