# Como tratar exceções em Python 
# try:
# try:
#     numero = int(input('Digite um número: '))
# except:
#     print('Você não digitou um número')


def dividir():
    try:
        numero1 = int(input('Digite o primeiro número: '))
        numero2 = int(input('Digite o segundo número: '))
        resultado = numero1 / numero2
        print(f'O resultado da divisão é: {resultado}')
    except ValueError as e:
        print('Por favor, digite um número válido. Erro: {e}')
    except ZeroDivisionError as e:
        print(f'Erro: {e}')
    except Exception as e:
        print('Ocorreu um erro desconhecido. . Erro: {e}')

#chamar a função dividir
dividir()

#Lendo um arquivo com segurança
try:
    with open("arquivo.txt", "r") as arquivo:
        conteudo = arquivo.read()
        print(conteudo)
except FileNotFoundError:
    print("O arquivo não foi encontrado!")
except PermissionError:
    print("Você não tem permissão para ler este arquivo!")
