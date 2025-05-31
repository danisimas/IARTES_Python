class Funcionario:

    def __init__(self, salario, nome):
        self.__salario = salario 
        self._nome = nome

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def salario(self):
        return self.__salario

    @salario.setter
    def salario(self, salario):
        self.__salario = salario

    def __str__(self):
        return f"Nome: {self._nome}, Salário: {self.__salario:.2f}"

    def __calcular_bonus(self):
        return self.__salario * 0.1

    def aumentar_salario(self, percentual):
        self.__salario += self.__calcular_bonus() * percentual / 100
        return True



class Animal:
    def __init__(self, nome):
        self.nome = nome

    def emitir_som(self):
        return "Som genérico"

class Cachorro(Animal):
    def emitir_som(self):
        return "Au au"

class Gata(Animal):
    def emitir_som(self):
        return "Miau"


if __name__ == "__main__":
    funcionario = Funcionario(1000, "João")
    print(funcionario)

    funcionario.aumentar_salario(10)
    print(funcionario)

    funcionario.salario = 2000  
    print(funcionario)

    funcionario.nome = "Maria"  
    print(funcionario)
    funcionario.aumentar_salario(20)
    print(funcionario)
    rex = Cachorro("Rex")
    mimi = Gata("Mimi")

    print(f"{rex.nome} diz: {rex.emitir_som()}")
    print(f"{mimi.nome} diz: {mimi.emitir_som()}")


