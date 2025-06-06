# Classe base: Veiculo 
# Autor: Daniele Simas Guimarães

class Veiculo:
    def __init__(self, marca, modelo, ano):
        self._marca = marca
        self._modelo = modelo
        self._ano = ano
        self.__ligado = False
        self.__velocidade = 0

    def ligar(self):
        if not self.__ligado:
            self.__ligado = True
            return f"{self._modelo} ligado com sucesso."
        return f"{self._modelo} já está ligado."

    def desligar(self):
        if self.__ligado:
            self.__ligado = False
            self.__velocidade = 0
            return f"{self._modelo} desligado com sucesso."
        return f"{self._modelo} já está desligado."

    def acelerar(self, kmh):
        if self.__ligado:
            self.__velocidade += kmh
            return f"{self._modelo} acelerou para {self.__velocidade} km/h."
        return "Não é possível acelerar com o veículo desligado."

    def frear(self):
        if self.__velocidade > 0:
            self.__velocidade = 0
            return f"{self._modelo} freiou completamente."
        return f"{self._modelo} já está parado."

    def esta_ligado(self):
        return self.__ligado

    def info(self):
        return f"{self._marca} {self._modelo}, {self._ano}"


class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, portas, combustivel):
        super().__init__(marca, modelo, ano)
        self._portas = portas
        self._combustivel = combustivel
        self._modo_economico = False

    def ativar_modo_economico(self):
        if self.esta_ligado():
            self._modo_economico = True
            return f"Modo econômico ativado no {self._modelo}."
        return "Ligue o carro para ativar o modo econômico."

    def desativar_modo_economico(self):
        if self._modo_economico:
            self._modo_economico = False
            return f"Modo econômico desativado no {self._modelo}."
        return "O modo econômico já está desativado."

    def info(self):
        return (f"Carro: {self._marca} {self._modelo} ({self._ano}) - "
                f"{self._portas} portas, Combustível: {self._combustivel}")

    def buzinar(self):
        return "Bibi!"


def criar_carros():
    carros = []

    quantidade = int(input("Quantos carros deseja cadastrar? "))
    for i in range(quantidade):
        print(f"\nCadastro do {i+1}º carro:")
        marca = input("Marca: ")
        modelo = input("Modelo: ")
        ano = int(input("Ano: "))
        portas = int(input("Número de portas: "))
        combustivel = input("Tipo de combustível: ")

        carro = Carro(marca, modelo, ano, portas, combustivel)
        carros.append(carro)

    return carros


def demonstrar_veiculos():
    carros = criar_carros()

    for c in carros:
        print("\nInformações:", c.info())
        print(c.ligar())
        velocidade = int(input(f"Com qual velocidade deseja acelerar o {c._modelo}? "))
        print(c.acelerar(velocidade))
        print(c.ativar_modo_economico())
        print(c.buzinar())
        print(c.frear())
        print(c.desligar())
        print("-" * 40)

if __name__ == "__main__":
    demonstrar_veiculos()
