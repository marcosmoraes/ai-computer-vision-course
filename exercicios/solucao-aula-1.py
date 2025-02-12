#Exercício 1: Conversor de Temperatura
celsius = float(input("Digite a temperatura em Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C é igual a {fahrenheit:.1f}°F")

#Exercício 2: Calculadora de Idade em Dias

idade = int(input("Digite sua idade em anos: "))
dias = idade * 365
print(f"Você já viveu aproximadamente {dias:,} dias!")

#Exercício 3: Verificador de Números
    
numero = int(input("Digite um número: "))
par_impar = "par" if numero % 2 == 0 else "ímpar"
pos_neg = "positivo" if numero > 0 else "negativo" if numero < 0 else "zero"
print(f"O número {numero} é {par_impar} e {pos_neg}")
    
#Exercício 4: Calculadora de Desconto
    
preco = float(input("Digite o preço original: R$ "))
desconto = float(input("Digite a porcentagem de desconto: "))
valor_final = preco * (1 - desconto/100)
print(f"Preço com {desconto}% de desconto: R$ {valor_final:.2f}")
    
#Exercício 5: Conversor de Moedas
    
reais = float(input("Digite o valor em reais: R$ "))
taxa = 5.00
dolares = reais / taxa
print(f"R$ {reais:.2f} = US$ {dolares:.2f}")

#Exercício 6: Calculadora de Média

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
media = (nota1 + nota2 + nota3) / 3
resultado = "aprovado" if media >= 7 else "reprovado"
print(f"Média: {media:.1f} - {resultado}")

#Exercício 7: Calculadora de Área

base = float(input("Digite a base do retângulo: "))
altura = float(input("Digite a altura do retângulo: "))
area = base * altura
perimetro = 2 * (base + altura)
print(f"Área: {area:.2f}")
print(f"Perímetro: {perimetro:.2f}")

#Exercício 8: Verificador de Vogais

letra = input("Digite uma letra: ").lower()
vogais = 'aeiou'
resultado = "vogal" if letra in vogais else "consoante"
print(f"A letra '{letra}' é uma {resultado}")

#Exercício 9: Calculadora de Gorjeta

conta = float(input("Digite o valor da conta: R$ "))
gorjeta = conta * 0.10
total = conta + gorjeta
print(f"Gorjeta: R$ {gorjeta:.2f}")
print(f"Total com gorjeta: R$ {total:.2f}")

#Exercício 10: Verificador de Ano Bissexto
ano = int(input("Digite um ano: "))
bissexto = (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)
print(f"O ano {ano} {'é' if bissexto else 'não é'} bissexto")