# Autor: Daniele Simas Guimarães
import unittest
import json
from app import app
from models import reset_estoque

class TestEstoqueAPI(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()
        reset_estoque()

    def test_criar_produto_valido(self):
        resposta = self.client.post("/produtos", json={
            "nome": "Arroz",
            "categoria": "Alimentos",
            "quantidade_inicial": 10,
            "preco_unitario": 5.0
        })
        self.assertEqual(resposta.status_code, 201)
        self.assertIsNotNone(resposta.get_json()["id"])
        self.assertEqual(resposta.get_json()["nome"], "Arroz")

    def test_criar_produto_invalido_quantidade(self):
        resposta = self.client.post("/produtos", json={
            "nome": "Feijão",
            "categoria": "Alimentos",
            "quantidade_inicial": -5,
            "preco_unitario": 4.0
        })
        self.assertEqual(resposta.status_code, 400)
        self.assertIn("Quantidade ou preço inválido", resposta.get_data(as_text=True))

    def test_criar_produto_invalido_preco(self):
        resposta = self.client.post("/produtos", json={
            "nome": "Leite",
            "categoria": "Laticínios",
            "quantidade_inicial": 2,
            "preco_unitario": 0.0
        })
        self.assertEqual(resposta.status_code, 400)
        self.assertIn("Quantidade ou preço inválido", resposta.get_data(as_text=True))

    def test_listar_produtos_vazio(self):
        resposta = self.client.get("/produtos")
        self.assertEqual(resposta.status_code, 200)
        self.assertEqual(resposta.get_json(), [])

    def test_listar_produtos_com_itens(self):
        self.client.post("/produtos", json={"nome": "Pão", "categoria": "Padaria", "quantidade_inicial": 5, "preco_unitario": 3.0})
        self.client.post("/produtos", json={"nome": "Leite", "categoria": "Laticínios", "quantidade_inicial": 2, "preco_unitario": 6.0})
        resposta = self.client.get("/produtos")
        self.assertEqual(resposta.status_code, 200)
        self.assertEqual(len(resposta.get_json()), 2)
        self.assertEqual(resposta.get_json()[0]["nome"], "Pão")

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

    def test_entrada_estoque_produto_nao_encontrado(self):
        resposta = self.client.post("/produtos/999/entrada", json={"quantidade": 5})
        self.assertEqual(resposta.status_code, 400)

    def test_entrada_estoque_quantidade_invalida(self):
        self.client.post("/produtos", json={"nome": "Suco", "categoria": "Bebidas", "quantidade_inicial": 10, "preco_unitario": 4.0})
        resposta = self.client.post("/produtos/1/entrada", json={"quantidade": -5})
        self.assertEqual(resposta.status_code, 400)
        self.assertIn("Entrada inválida", resposta.get_data(as_text=True))

    def test_saida_estoque_valida(self):
        self.client.post("/produtos", json={
            "nome": "Carne",
            "categoria": "Açougue",
            "quantidade_inicial": 10,
            "preco_unitario": 30.0
        })
        resposta = self.client.post("/produtos/1/saida", json={"quantidade": 3})
        self.assertEqual(resposta.status_code, 200)
        self.assertEqual(resposta.get_json()["quantidade"], 7)

    def test_saida_estoque_insuficiente(self):
        self.client.post("/produtos", json={
            "nome": "Frango",
            "categoria": "Açougue",
            "quantidade_inicial": 5,
            "preco_unitario": 15.0
        })
        resposta = self.client.post("/produtos/1/saida", json={"quantidade": 999})
        self.assertEqual(resposta.status_code, 400)
        self.assertIn("Saída inválida ou estoque insuficiente", resposta.get_data(as_text=True))

    def test_saida_estoque_produto_nao_encontrado(self):
        resposta = self.client.post("/produtos/999/saida", json={"quantidade": 5})
        self.assertEqual(resposta.status_code, 400)

    def test_remover_produto(self):
        self.client.post("/produtos", json={
            "nome": "Café",
            "categoria": "Bebidas",
            "quantidade_inicial": 2,
            "preco_unitario": 12.0
        })
        resposta = self.client.delete("/produtos/1")
        self.assertEqual(resposta.status_code, 200)
        self.assertIn("Produto removido com sucesso", resposta.get_data(as_text=True))

    def test_remover_produto_nao_existente(self):
        resposta = self.client.delete("/produtos/999")
        self.assertEqual(resposta.status_code, 404)
        self.assertIn("Produto não encontrado", resposta.get_data(as_text=True))

    def test_atualizar_produto(self):
        self.client.post("/produtos", json={"nome": "Bolacha", "categoria": "Lanche", "quantidade_inicial": 10, "preco_unitario": 2.5})
        resposta = self.client.put("/produtos/1", json={"nome": "Biscoito", "preco_unitario": 3.0})
        self.assertEqual(resposta.status_code, 200)
        self.assertEqual(resposta.get_json()["nome"], "Biscoito")
        self.assertEqual(resposta.get_json()["preco_unitario"], 3.0)

    def test_obter_produto_por_id(self):
        self.client.post("/produtos", json={"nome": "Refrigerante", "categoria": "Bebidas", "quantidade_inicial": 6, "preco_unitario": 7.0})
        resposta = self.client.get("/produtos/1")
        self.assertEqual(resposta.status_code, 200)
        self.assertEqual(resposta.get_json()["nome"], "Refrigerante")

    def test_obter_produto_por_id_nao_encontrado(self):
        resposta = self.client.get("/produtos/999")
        self.assertEqual(resposta.status_code, 404)
        self.assertIn("Produto não encontrado", resposta.get_data(as_text=True))


if __name__ == '__main__':
    unittest.main()