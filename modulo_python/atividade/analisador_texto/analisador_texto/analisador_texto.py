# analisador_texto.py
# Autor: Daniele Simas Guimarães

def analisar_texto(texto):

    textMauisculo = []
    textMinusculo = []
    numeroFrequencia = 0
    texto_curto = ""
    texto_misto = ""
    
    vogais = "aeiouAEIOU"

    palavras = texto.split()

    for caractere in texto:
        if caractere.isupper():
            textMauisculo.append(caractere)
        else:
            textMinusculo.append(caractere)
        
        if caractere.isdigit():
            texto_misto = "Texto contém dados mistos"

    
    for caractere in texto:
        if caractere in vogais:
            numeroFrequencia+=1
    
    if len(palavras) < 10:
        texto_curto = "Texto muito curto"

    print(texto_curto)
    print("Texto em maiúsculas", textMauisculo)
    print("Número de palavras:",len(palavras))
    print("Número de caracteres (com espaços):",len(texto))
    print(numeroFrequencia)
    print(texto_misto)
   
    


def main():
    continuar = True
    while continuar:
        texto = input("Digite um texto para análise: ")
        analisar_texto(texto)
        resposta = input("Deseja analisar outro texto? (s/n): ").strip().lower()
        continuar = resposta == 's'

if __name__ == "__main__":
    main()
