# analisador_texto.py
# Autor: [SEU NOME AQUI]

def analisar_texto(texto):
    # TODO: implementar análise de texto
    pass

def main():
    continuar = True
    while continuar:
        texto = input("Digite um texto para análise: ")
        analisar_texto(texto)
        resposta = input("Deseja analisar outro texto? (s/n): ").strip().lower()
        continuar = resposta == 's'

if __name__ == "__main__":
    main()
