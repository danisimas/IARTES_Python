# analisador_texto.py
# Autor: Daniele Simas Guimarães



def textoCapitalizado(texto):
    print("Texto Capitalizado: ",texto.capitalize())

def textoMinusculo(texto):
    print("Texto Minusculo: ",texto.lower())


def textoMaiusculo(texto):
    print("Texto Maiusculo: ",texto.upper())



def numeroFrequenciaVogais(texto, vogal):
    numeroFrequencia = 0
    for caractere in texto:
        if caractere in vogal:
            numeroFrequencia+=1
    return numeroFrequencia


def frequenciaVogais(texto):
    vogais = "aeiou"
    textoMinusculo = texto.lower()
    saida = "Frequencia de vogais: "
    for vogal in vogais:
        contador = numeroFrequenciaVogais(textoMinusculo,vogal)
        saida += vogal + "=" + str(contador) + ", "
    print(saida)



def totalPalavras(texto):
    palavras = texto.split()
    print("Número de palavras:",len(palavras))



def totalLetrasComEspaco(texto):
     print("Número de caracteres (com espaços):",len(texto))


def totalLetrasSemEspaco(texto):
    textoSemEspaco =  texto.replace(" ", "")
    print("Número de caracteres (sem espaços):",len(textoSemEspaco))


def textoCurto(texto):
    palavras = texto.split()
    if len(palavras) < 10:
        texto_curto = "Texto muito curto"    
        print(texto_curto)


def textoMisto(texto):
    for caractere in texto:
     if caractere.isdigit():
            texto_misto = "Texto contém dados mistos"
            print(texto_misto)
            break


def textoLongo(texto):
    palavras = texto.split()
    palavras.sort(key=len, reverse=True)
    saida = "Três palavras mais longas: "
    contador = 0
    for palavra in palavras:
        if contador >=3:
            break
        saida += palavra + ", "
        contador+=1
    print(saida)



def ignorarPontuacao(texto):
    pontuacao = [".", ",", "?", "!"]
    for pontos in pontuacao:
        texto.replace(pontos,"")
    return texto


def analisar_texto(texto):
    texto = ignorarPontuacao(texto)
    textoCurto(texto)
    textoMisto(texto)

    while True:
        print("\nMenu de Análise de Texto")
        print("1. Texto Capitalizado")
        print("2. Texto Minúsculo")
        print("3. Texto Maiúsculo")
        print("4. Frequência de Vogais")
        print("5. Número Total de Palavras")
        print("6. Número Total de caracteres (com espaços)")
        print("7. Número Total de caracteres (sem espaços)")
        print("8. Mostrar Três Palavras Mais Longas")
        print("0. Sair")

        escolha = input("Escolha uma opção: ")

        match escolha:
            case "1":
                textoCapitalizado(texto)
            case "2":
                textoMinusculo(texto)
            case "3":
                textoMaiusculo(texto)
            case "4":
                frequenciaVogais(texto)
            case "5":
                totalPalavras(texto)
            case "6":
                totalLetrasComEspaco(texto)
            case "7":
                totalLetrasSemEspaco(texto)
            case "8":
                textoLongo(texto)
            case "0":
                print("Encerrando análise.")
                break
            case _:
                print("Opção inválida. Tente novamente.")


def main():
    continuar = True
    while continuar:
        texto = input("Digite um texto para análise: ")
        analisar_texto(texto)
        resposta = input("Deseja analisar outro texto? (s/n): ").strip().lower()
        continuar = resposta == 's'

if __name__ == "__main__":
    main()
