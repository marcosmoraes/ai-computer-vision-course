#estrutura de repetição
#Exemplo de estrutura de repetição for:
for i in range(5):
    print(i*2)

#faça outro exemplo de estrutura de repetição for imprimindo uma lista de nomes
nomes = ["João", "Maria", "Pedro", "Ana"]
for nome in nomes:
    print(nome)

#faça um exemplo de for usando uma lista misturada de números e strings
lista_misturada = [1, "dois", 3, "quatro", 5]
for item in lista_misturada:
    print(item)

#faça um for de exemplo de uma matriz multidimensional (lista de listas) usando (cód, nome, nota1, nota2, nota3, nota4, media)
matriz = [
    ["João", 8.5, 7.0, 9.0, 6.5, 7.5],
    ["Maria", 7.0, 8.0, 6.5, 7.5, 7.0],
    ["Pedro", 4.0, 8.5, 7.0, 8.0, 5.5],
    ["Ana", 6.5, 7.0, 8.5, 7.5, 7.0]
]
for aluno in matriz:
    if aluno[5] >= 7.0:
        print(f"Aluno: {aluno[0]}, Média: {aluno[5]:.2f}, Aprovado")
    else:
        print(f"Aluno: {aluno[0]}, Média: {aluno[5]:.2f}, Reprovado")

#faça um exemplo de estrutura de repetição while (enquanto). Enquanto a condição for verdadeira, o bloco de código será executado.
contador = 0
while contador < 5:
    print(contador)
    contador += 1 # contador = contador + 1

#faça um teste de mesa do código acima.
#contador = 0
#0 < 5 (True)
#print(0)
#contador = 1
#1 < 5 (True)
#print(1)
#contador = 2
#2 < 5 (True)
#print(2)
#contador = 3
#3 < 5 (True)
#print(3)
#contador = 4
#4 < 5 (True)
#print(4)
#contador = 5
#5 < 5 (False)

lista = []
contador = 0
while len(lista) < 5: # lenght comprimento da lista
    contador += 1
    lista.append(contador)
    print(contador)
print(lista)

lista_de_nomes = ["João", "Maria", "Pedro", "Ana", "José","Paulo"]
print(lista_de_nomes)
while lista_de_nomes: #outra alternativa de fazer o while len(lista_de_nomes) > 0:
    lista_de_nomes.pop()
    print(lista_de_nomes)

print(lista_de_nomes)