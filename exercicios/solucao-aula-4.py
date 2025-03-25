# 1. Contador de Linhas
def contar_linhas(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo:
            return len(arquivo.readlines())
    except FileNotFoundError:
        return "Arquivo não encontrado"

# 2. Gerador de Lista de Compras
def adicionar_item(item):
    with open('lista_compras.txt', 'a') as arquivo:
        arquivo.write(item + '\n')

def ver_lista():
    try:
        with open('lista_compras.txt', 'r') as arquivo:
            return arquivo.read()
    except FileNotFoundError:
        return "Lista vazia"

# 3. Mesclador de Arquivos
def mesclar_arquivos(arquivo1, arquivo2, arquivo_destino):
    with open(arquivo_destino, 'w') as destino:
        for arquivo in [arquivo1, arquivo2]:
            with open(arquivo, 'r') as f:
                destino.write(f.read() + '\n')

# 4. Filtro de Palavras
#crie uma frase com 10 palavras
frase = "Aprendendo Python é muito divertido"
#palavras = ["Aprendendo", "Python", "é", "muito", "divertido"]
def filtrar_palavras(arquivo_origem, arquivo_destino):
    with open(arquivo_origem, 'r') as origem:
        palavras = origem.read().split()
        palavras_filtradas = [p for p in palavras if len(p) > 5]
        # for palavra in palavras:
        #     if len(palavra) > 5:
        #         palavras_filtradas = palavras_filtradas.append(palavra)
        #         print(palavras_filtradas)

        with open(arquivo_destino, 'w') as destino:
            destino.write(' '.join(palavras_filtradas))

#chamar a função filtrar_palavras
filtrar_palavras('frase.txt', 'frase_filtrada.txt')

# 5. Registro de Acesso
from datetime import datetime

def registrar_acesso():
    with open('acessos.txt', 'a') as arquivo:
        data_hora = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        arquivo.write(f"Acesso em: {data_hora}\n")

# 6. Calculadora de Médias
def calcular_medias(arquivo_notas, arquivo_medias):
    with open(arquivo_notas, 'r') as notas:
        with open(arquivo_medias, 'w') as medias:
            for linha in notas:
                nome, *notas = linha.strip().split(',')
                media = sum(float(n) for n in notas) / len(notas)
                medias.write(f"{nome}: {media:.2f}\n")

#outra solução do exercicio 6
def calcular_media(arquivo_origem, arquivo_destino):
    with open(arquivo_origem, "r") as origem:
        with open(arquivo_destino, "w") as destino:
            for linha in origem:
                nome, *notas = linha.strip().split(',')
                nota_convertida = 0
                print(type(notas))
                for nota in notas:
                    nota_convertida += float(nota)
                    print(type(nota_convertida))
                media = nota_convertida/len(notas)
                print(media)
                print(type(media))
                destino.write(f"{nome}: {media:.2f}\n")

calcular_media('notas.txt','notasfinal.txt')

# 7. Organizador de Contatos
def adicionar_contato(nome, telefone, email):
    with open('contatos.txt', 'a') as arquivo:
        arquivo.write(f"{nome},{telefone},{email}\n")

def buscar_contatos(termo):
    with open('contatos.txt', 'r') as arquivo:
        return [linha for linha in arquivo if termo in linha]

# 8. Contador de Palavras
from collections import Counter

def contar_palavras(arquivo_origem, arquivo_destino):
    with open(arquivo_origem, 'r') as origem:
        palavras = origem.read().lower().split()
        contagem = Counter(palavras)
        with open(arquivo_destino, 'w') as destino:
            for palavra, quantidade in contagem.items():
                destino.write(f"{palavra}: {quantidade}\n")

# 9. Editor de Configurações
def alterar_configuracao(chave, valor):
    configs = {}
    with open('config.txt', 'r') as arquivo:
        for linha in arquivo:
            k, v = linha.strip().split('=')
            configs[k] = v
    
    configs[chave] = valor
    
    with open('config.txt', 'w') as arquivo:
        for k, v in configs.items():
            arquivo.write(f"{k}={v}\n")

# 10. Backup Simples
import shutil
from datetime import datetime

def fazer_backup(arquivo):
    data_hora = datetime.now().strftime('%Y%m%d_%H%M%S')
    nome_backup = f"{arquivo}_{data_hora}.bak"
    shutil.copy2(arquivo, nome_backup)
    
    with open('registro_backups.txt', 'a') as registro:
        registro.write(f"Backup de {arquivo} criado em {data_hora}\n")