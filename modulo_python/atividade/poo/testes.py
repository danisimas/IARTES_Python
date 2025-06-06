
# Classe base: Veiculo 
# Autor: Daniele Simas Guimarães

import unittest
from carro import Carro
class TestCarro(unittest.TestCase):

    def setUp(self):
        self.carro = Carro("Toyota", "Corolla", 2022, 4, "Gasolina")

    def test_comportamento_ligar_acelerar(self):
        self.assertEqual(self.carro.ligar(), "Corolla ligado com sucesso.")
        self.assertEqual(self.carro.acelerar(30), "Corolla acelerou para 30 km/h.")

    def test_alteracao_estado_modo_economico(self):
        self.carro.ligar()
        ativar = self.carro.ativar_modo_economico()
        self.assertEqual(ativar, "Modo econômico ativado no Corolla.")
        desativar = self.carro.desativar_modo_economico()
        self.assertEqual(desativar, "Modo econômico desativado no Corolla.")

    def test_encapsulamento_ligado(self):
        self.assertFalse(self.carro.esta_ligado())
        self.carro.ligar()
        self.assertTrue(self.carro.esta_ligado())

if __name__ == '__main__':
    unittest.main()
