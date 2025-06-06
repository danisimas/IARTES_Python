# Autor: Daniele Simas Guimarães
estoque = []
proximo_id = 1

def criar_produto(dados):
    global proximo_id
    if dados["quantidade_inicial"] < 0 or dados["preco_unitario"] <= 0:
        raise ValueError("Quantidade ou preço inválido.")

    produto = {
        "id": proximo_id,
        "nome": dados["nome"],
        "categoria": dados["categoria"],
        "quantidade": dados["quantidade_inicial"],
        "preco_unitario": dados["preco_unitario"]
    }
    estoque.append(produto)
    proximo_id += 1
    return produto

def listar_produtos(filtros=None):
    if not filtros:
        return estoque
    nome = filtros.get("nome")
    categoria = filtros.get("categoria")
    return [p for p in estoque if (not nome or nome.lower() in p["nome"].lower()) and
                                    (not categoria or categoria.lower() in p["categoria"].lower())]

def obter_produto_por_id(id):
    return next((p for p in estoque if p["id"] == id), None)

def atualizar_produto(id, dados):
    produto = obter_produto_por_id(id)
    if not produto:
        return None
    for chave in ["nome", "categoria", "preco_unitario"]:
        if chave in dados:
            if chave == "preco_unitario" and dados[chave] <= 0:
                raise ValueError("Preço inválido.")
            produto[chave] = dados[chave]
    return produto

def entrada_estoque(id, qtd):
    produto = obter_produto_por_id(id)
    if produto and qtd > 0:
        produto["quantidade"] += qtd
        return produto
    return None

def saida_estoque(id, qtd):
    produto = obter_produto_por_id(id)
    if produto and 0 < qtd <= produto["quantidade"]:
        produto["quantidade"] -= qtd
        return produto
    return None

def remover_produto(id):
    global estoque
    produto = obter_produto_por_id(id)
    if produto:
        estoque = [p for p in estoque if p["id"] != id]
        return True
    return False
