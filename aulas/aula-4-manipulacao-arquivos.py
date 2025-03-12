# Conceitos básicos de manipulação de arquivos
# Modos de abrir um arquivos no python 
# r - abre o arquivo somente para leitura
# w - abre o arquivo somente para escrita
# a - abre o arquivo para escrita, adicionando o conteúdo ao final do arquivo
# r+ - abre o arquivo para leitura e escrita
# w+ - abre o arquivo para leitura e escrita
# a+ - abre o arquivo para leitura e escrita, adicionando o conteúdo ao final do arquivo

# para ler o conteúdo de um arquivo, usamos o método read()
with open('media-dos-alunos.txt', 'r') as arquivo:
    print(arquivo.read())

# #para escrever em um arquivo, usamos o método write()
with open('media-dos-alunos.txt', 'w') as arquivo:
    arquivo.write('Média dos alunos\n')
    arquivo.write('Aluno 1: 7.5\n')
    arquivo.write('Aluno 2: 8.0\n')
    arquivo.write('Aluno 3: 9.0\n')
    arquivo.write('Aluno 4: 6.5\n')
    arquivo.write('Aluno 5: 7.0\n')

# #adionar conteúdo ao final do arquivo
with open('media-dos-alunos.txt', 'a') as arquivo:
    arquivo.write('Aluno 6: 8.5\n')
    arquivo.write('Aluno 7: 9.5\n')
    arquivo.write('Aluno 8: 7.5\n')
    arquivo.write('Aluno 9: 8.0\n')

#ler linha por linha
with open('media-dos-alunos.txt', 'r') as arquivo:
    for linha in arquivo:
         if linha.startswith('Aluno'):
              print(linha)

#função strip() - remove espaços em branco no início e no final da string
texto = '   Olá, mundo!   '
print(texto.strip())

texto = 'Olá \n mundo!' # \n é um caractere de quebra de linha
print(texto.strip())

#função split() - divide a string em uma lista de substrings
texto = 'Cód Aluno 9: 7.5'
novo_texto = texto.split()
print(novo_texto[-1])


with open('media-dos-alunos.txt', 'r') as arquivo:
    for linha in arquivo:
        if linha.startswith('Aluno'):
            nota = float(linha.strip().split(':')[1])
            if nota >= 8:
                print(f'O aluno {linha.strip()} foi aprovado')
            


