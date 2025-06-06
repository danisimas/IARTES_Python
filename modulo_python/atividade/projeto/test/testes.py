# Autor: Daniele Simas Guimarães
import unittest
import app

class TestEstoqueAPI(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_criar_produto_valido(self):
        resposta = self.client.post("/produtos", json={
            "nome": "Arroz",
            "categoria": "Alimentos",
            "quantidade_inicial": 10,
            "preco_unitario": 5.0
        })
        self.assertEqual(resposta.status_code, 201)

    def test_criar_produto_invalido(self):
        resposta = self.client.post("/produtos", json={
            "nome": "Feijão",
            "categoria": "Alimentos",
            "quantidade_inicial": -5,
            "preco_unitario": 4.0
        })
        self.assertEqual(resposta.status_code, 400)

    def test_entrada_estoque(self):
        self.client.post("/produtos", json={
            "nome": "Óleo",
            "categoria": "Alimentos",
            "quantidade_inicial": 5,
            "preco_unitario": 7.5
        })
        resposta = self.client.post("/produtos/1/entrada", json={"quantidade": 5})
        self.assertEqual(resposta.status_code, 200)
        self.assertEqual(resposta.get_json()["quantidade"], 10)

    def test_saida_estoque_erro(self):
        resposta = self.client.post("/produtos/1/saida", json={"quantidade": 999})
        self.assertEqual(resposta.status_code, 400)

    def test_remover_produto(self):
        resposta = self.client.delete("/produtos/1")
        self.assertEqual(resposta.status_code, 200)
