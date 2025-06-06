# Autor: Daniele Simas Guimarães

from flask import Blueprint, jsonify, request
from models import (
    criar_produto, listar_produtos, obter_produto_por_id,
    atualizar_produto, entrada_estoque, saida_estoque, remover_produto
)

inventario_routes = Blueprint("inventario", __name__)

@inventario_routes.route("/produtos", methods=["GET"])
def rota_listar():
    filtros = request.args
    return jsonify(listar_produtos(filtros))

@inventario_routes.route("/produtos", methods=["POST"])
def rota_criar():
    try:
        dados = request.get_json()
        produto = criar_produto(dados)
        return jsonify(produto), 201
    except Exception as e:
        return jsonify({"erro": str(e)}), 400

@inventario_routes.route("/produtos/<int:id>", methods=["GET"])
def rota_obter(id):
    produto = obter_produto_por_id(id)
    if produto:
        return jsonify(produto)
    return jsonify({"erro": "Produto não encontrado"}), 404

@inventario_routes.route("/produtos/<int:id>", methods=["PUT"])
def rota_atualizar(id):
    try:
        dados = request.get_json()
        produto = atualizar_produto(id, dados)
        if produto:
            return jsonify(produto)
        return jsonify({"erro": "Produto não encontrado"}), 404
    except Exception as e:
        return jsonify({"erro": str(e)}), 400

@inventario_routes.route("/produtos/<int:id>/entrada", methods=["POST"])
def rota_entrada(id):
    qtd = request.json.get("quantidade", 0)
    produto = entrada_estoque(id, qtd)
    if produto:
        return jsonify(produto)
    return jsonify({"erro": "Entrada inválida"}), 400

@inventario_routes.route("/produtos/<int:id>/saida", methods=["POST"])
def rota_saida(id):
    qtd = request.json.get("quantidade", 0)
    produto = saida_estoque(id, qtd)
    if produto:
        return jsonify(produto)
    return jsonify({"erro": "Saída inválida ou estoque insuficiente"}), 400

@inventario_routes.route("/produtos/<int:id>", methods=["DELETE"])
def rota_remover(id):
    if remover_produto(id):
        return jsonify({"mensagem": "Produto removido com sucesso."})
    return jsonify({"erro": "Produto não encontrado"}), 404
