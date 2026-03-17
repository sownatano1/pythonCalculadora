import time
import os
import platform
import math

def clear_console():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")

clear_console()
print("Bem-vindo a Calculadora Pro Max 3000")
time.sleep(2)
clear_console()
print(".")
time.sleep(1)
clear_console()
print("..")
time.sleep(1)
clear_console()
print("...")
time.sleep(1)
clear_console()

print("Escreva o primeiro numero: ")
numero1 = int(input())
clear_console()

print("Escreva o segundo numero: ")
numero2 = int(input())
clear_console()

def Escolha():
    clear_console()
    print("Escolha o tipo de calculo:")
    print("Multiplicação = m")
    print("Divisão = d")
    print("Adição = a")
    print("Subtração = s")
#AAAAAAAAAAAAAAAAAAAAAAAAA LUANA :)






#Ouviram do Ipiranga, as margens plácidas
#De um povo heroico, o brado retumbante
#E o Sol da liberdade, em raios fúlgidos
#Brilhou no céu da pátria nesse instante









#hehe sou brasileiro com muito orgulho e muito amor <3
Escolha()

def Calculate():
    simbolo = str(input())
    clear_console()

    
    if (simbolo == "m"):
        resultado = numero1 * numero2
        print(resultado)

    elif (simbolo == "d"):
        resultado = numero1 / numero2
        print(resultado)

    elif (simbolo == "a"):
        resultado = numero1 + numero2
        print(resultado)

    elif (simbolo == "s"):
        resultado = numero1 - numero2
        print(resultado)

    else:
        print("Não existe essa opção")
        print("Escolha denovo")
        Escolha()
        Calculate()
        

Calculate()