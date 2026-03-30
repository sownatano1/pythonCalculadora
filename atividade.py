from datetime import date

nome = input("Qual é o seu nome? : ")
print(f"Olá {nome}")

numero = int(input("Escreva um número inteiro aleatório : "))
print(f"O dobro de {numero} é {numero*2}")

num1 = int(input("Escreva o primeiro número inteiro : "))
num2 = int(input("Escreva o segundo número inteiro : "))
print(f"A soma dos dois numeros é {num1 + num2}")

ano = int(input("Em qual ano você nasceu? : "))
ano_atual = date.today().year
idade = ano_atual - ano
print(f"Então você tem {idade} anos")

salario = float(input("Quanto é o seu salário? : "))
aumento = (salario * 0.1) + salario
print(f"Você recebe R$ {salario:.2f} mas com 10% de aumento receberia R$ {aumento:.2f}")

c = float(input("Escreva a temperatura em Celsius: "))
f = (c * 9/5) + 32
print(f"{c} °C convertendo para Fahrenheit, ficaria {f} °F")

#Cadastro
n = input("Digite o seu nome: ")
i = int(input("Digite a sua idade: "))
c = input("Digite a sua cidade: ")
print(f"Nome = {n} | Idade = {i} | Cidade = {c}")

#Calculadora esta em outro codigo

hora = int(input("Digite a quantidade que ganha por hora: "))
hora_t = int(input("Digite a quantidade de horas trabalhadas por mês: "))
valor = hora * hora_t
print(f"Você recebe R$ {valor} por mês")

#Reais para dolares
reais = float(input("Digite o valor em reais: "))
cotacao = 5.10
dolar = reais / cotacao
print(f"R$ {reais} equivale a $ {dolar:.2f} dólares")