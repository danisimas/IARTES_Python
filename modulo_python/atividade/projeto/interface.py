# Autor: Daniele Simas Guimarães
import streamlit as st
import requests

BASE_URL = "http://127.0.0.1:5000"

st.title("📦 Sistema de Inventário")

# Listar produtos com expanders para ações
st.subheader("📋 Lista de Produtos")
nome_filtro = st.text_input("Filtrar por nome", key="filtro_nome")
categoria_filtro = st.text_input("Filtrar por categoria", key="filtro_categoria")

params = {}
if nome_filtro:
    params["nome"] = nome_filtro
if categoria_filtro:
    params["categoria"] = categoria_filtro

resp = requests.get(f"{BASE_URL}/produtos", params=params)
if resp.ok:
    produtos = resp.json()

    # --- Seção de Cadastro de Novo Produto usando st.form ---
    with st.expander("🆕 Cadastrar Novo Produto"):
        # Criamos o formulário de cadastro
        with st.form(key="form_cadastro_produto", clear_on_submit=True):
            # Os campos de entrada do formulário
            # Não precisamos inicializar no session_state para limpeza aqui,
            # pois clear_on_submit=True fará o trabalho.
            nome = st.text_input("Nome do novo produto", key="cad_nome_form")
            categoria = st.text_input("Categoria", key="cad_categoria_form")
            quantidade = st.number_input("Quantidade Inicial", min_value=0, key="cad_quantidade_form")
            preco = st.number_input("Preço Unitário", min_value=0.01, key="cad_preco_form")

            # Botão de submit do formulário
            submit_button = st.form_submit_button(label="Cadastrar")

            # Lógica para processar o formulário quando o botão é clicado
            if submit_button:
                dados = {
                    "nome": nome,
                    "categoria": categoria,
                    "quantidade_inicial": quantidade,
                    "preco_unitario": preco
                }
                resp_post = requests.post(f"{BASE_URL}/produtos", json=dados)
                if resp_post.status_code == 201:
                    st.success("Produto cadastrado com sucesso!")
                    # O clear_on_submit=True do st.form() se encarrega de limpar os campos
                    # Precisamos apenas recarregar a lista de produtos para ver o novo item
                    st.rerun() # Reexecuta o script para atualizar a lista de produtos
                else:
                    st.error(resp_post.text)

    # --- Restante do código (Listar, Atualizar, Entrada, Saída, Remover) permanece o mesmo ---
    if produtos:
        for produto in produtos:
            with st.expander(f"🔧 Produto ID {produto['id']} - {produto['nome']}"):
                st.write(f"**Categoria**: {produto['categoria']}")
                st.write(f"**Quantidade**: {produto['quantidade']}")
                st.write(f"**Preço Unitário**: R${produto['preco_unitario']:.2f}")

                # Atualização
                st.markdown("---")
                st.markdown("**✏️ Atualizar Dados**")
                novo_nome = st.text_input("Nome", value=produto['nome'], key=f"nome_{produto['id']}")
                nova_categoria = st.text_input("Categoria", value=produto['categoria'], key=f"categoria_{produto['id']}")
                novo_preco = st.number_input("Preço Unitário", value=float(produto['preco_unitario']), min_value=0.01, key=f"preco_{produto['id']}")
                if st.button("Atualizar", key=f"att_{produto['id']}"):
                    dados = {
                        "nome": novo_nome,
                        "categoria": nova_categoria,
                        "preco_unitario": novo_preco
                    }
                    resp = requests.put(f"{BASE_URL}/produtos/{produto['id']}", json=dados)
                    if resp.ok:
                        st.success("Produto atualizado!")
                        st.rerun()
                    else:
                        st.error(resp.text)

                # Entrada no estoque
                st.markdown("---")
                st.markdown("**📥 Entrada no Estoque**")
                entrada = st.number_input("Quantidade a adicionar", min_value=1, step=1, key=f"entrada_{produto['id']}")
                if st.button("Registrar Entrada", key=f"ent_btn_{produto['id']}"):
                    resp = requests.post(f"{BASE_URL}/produtos/{produto['id']}/entrada", json={"quantidade": entrada})
                    if resp.ok:
                        st.success("Entrada registrada!")
                        st.rerun()
                    else:
                        st.error(resp.text)

                # Saída no estoque
                st.markdown("---")
                st.markdown("**📤 Saída do Estoque**")
                saida = st.number_input("Quantidade a remover", min_value=1, step=1, key=f"saida_{produto['id']}")
                if st.button("Registrar Saída", key=f"saida_btn_{produto['id']}"):
                    resp = requests.post(f"{BASE_URL}/produtos/{produto['id']}/saida", json={"quantidade": saida})
                    if resp.ok:
                        st.success("Saída registrada!")
                        st.rerun()
                    else:
                        st.error(resp.text)

                # Remover produto
                st.markdown("---")
                st.markdown("**🗑️ Remover Produto**")
                if st.button("Remover Produto", key=f"del_{produto['id']}"):
                    resp = requests.delete(f"{BASE_URL}/produtos/{produto['id']}")
                    if resp.ok:
                        st.success("Produto removido com sucesso!")
                        st.rerun()
                    else:
                        st.error("Erro ao remover produto")

    else:
        st.info("Nenhum produto encontrado.")
else:
    st.error("Erro ao buscar produtos")