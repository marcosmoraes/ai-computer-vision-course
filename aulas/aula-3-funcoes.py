#estrutura de uma função
#def nome_da_funcao(parametro1, parametro2):
    #código da função
    #return resultado

#faça um cálculo de média de notas de uma lista de alunos.
notas = [8, 7, 9, 6]

#crie uma função que calcule a média de uma lista de notas.
def calcular_media(notas):
    return sum(notas) / len(notas)

#chamando uma função
print(calcular_media(notas))

## Exercício 9: Calculadora de Gorjeta

#Crie uma função que:
#- Peça o **valor total da conta**
#- Calcule **10% de gorjeta**
#- Mostre o **valor total com gorjeta**

def calcular_gorjeta(valor_total): 
    return valor_total * 0.2

#valor_total_conta = float(input("Digite o valor total da conta: R$ "))
#print(f"Valor da gorjeta: R$ {calcular_gorjeta(valor_total_conta):.2f}")

#crie uma função que faça o login de um usuário.
def login(usuario, senha):
    if usuario == "admin" and senha == "123":
        sucesso = "Login realizado com sucesso!"
        return sucesso
    else:
        fracasso = "Usuário ou senha incorretos."
        return fracasso

user = input("Digite o usuário: ")
senha = input("Digite a senha: ")
print(login(user, senha))

#refatorando o código acima, coloque tipagem nos parâmetros e no retorno da função
def login(usuario: str, senha: str) -> bool:
    if usuario == "admin" and senha == "123":
        return True
    else:
        return False
    