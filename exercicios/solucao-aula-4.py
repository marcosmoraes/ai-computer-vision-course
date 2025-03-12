def calcular_media(numeros):
    if not numeros:
        return 0
    return sum(numeros) / len(numeros)

def contar_vogais(texto):
    vogais = 'aeiouAEIOU'
    return sum(1 for letra in texto if letra in vogais)

def criar_tabuada(numero):
    tabuada = []
    i = 1
    while i <= 10:
        tabuada.append(numero * i)
        i += 1
    return tabuada

def verificar_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

def inverter_lista(lista):
    return [lista[i] for i in range(len(lista)-1, -1, -1)]

def contar_palavras(texto):
    palavras = texto.lower().split()
    contagem = {}
    for palavra in palavras:
        contagem[palavra] = contagem.get(palavra, 0) + 1
    return contagem

def filtrar_pares(numeros):
    return [num for num in numeros if num % 2 == 0]

def celsius_para_fahrenheit(temperaturas):
    return [(temp * 9/5) + 32 for temp in temperaturas]

def verificar_senha(senha):
    if len(senha) < 8:
        return False
    tem_maiuscula = any(c.isupper() for c in senha)
    tem_numero = any(c.isdigit() for c in senha)
    tem_especial = any(not c.isalnum() for c in senha)
    return tem_maiuscula and tem_numero and tem_especial

def ordenar_por_tamanho(palavras):
    return sorted(palavras, key=lambda x: (len(x), x))


