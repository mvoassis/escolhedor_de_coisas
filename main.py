import streamlit as st
import random
import time

def faz_a_escolha(lista):
    with st.spinner("Fazendo alguns cálculos complexos..."):
        time.sleep(5)
        escolha_final = random.choice(lista)
        st.markdown("## Sua escolha foi...")
        time.sleep(2)
        st.markdown(f'# :green[{escolha_final}] !')  # blue, green, orange, red, violet, gray/grey, rainbow

st.title("Escolhedor de coisas")

aba1, aba2 = st.tabs(["Simples", "N Valores"])

with aba1:
    opcao1 = st.text_input("Insira a opção 1:")
    opcao2 = st.text_input("Insira a opção 2:")
    opcao3 = st.text_input("Insira a opção 3:")

    if st.button("Escolher!", key="botao1"):
        lista_de_opcoes = [opcao1, opcao2, opcao3]
        faz_a_escolha(lista_de_opcoes)

with aba2:
    if "lista_n_opcoes" not in st.session_state:
        st.session_state.lista_n_opcoes = []

    st.markdown(f"## Opções: {st.session_state.lista_n_opcoes}")

    nova_opcao = st.text_input("Insira uma nova opção:")

    if st.button("Insirir opção"):
        st.session_state.lista_n_opcoes.append(nova_opcao)
        st.rerun()

    if st.button("Apagar lista"):
        st.session_state.lista_n_opcoes.clear()
        st.rerun()

    if st.button("Escolher!", key="botao2"):
        faz_a_escolha(st.session_state.lista_n_opcoes)
