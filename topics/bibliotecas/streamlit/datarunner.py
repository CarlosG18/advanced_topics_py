import streamlit as st

tela = 0

st.text("site DATARUNNER")
st.sidebar.text("escolha uma opção")
opcao = st.sidebar.selectbox("", options=["adicionar dados", "visualizar dados", "criar novos treinos"])


if opcao == "adicionar dados":
    tela = 0
elif opcao == "visualizar dados":
    tela = 1
else:
    tela = 2

if tela == 0:
    st.text("\n")
    st.text("informe o nome do treino:")
    st.text_input("insira aqui", key="titulo")
    st.text("informe os dados do treino:")
    st.text_input("insira aqui", key="dados")
    button_send = st.button("enviar")
elif tela == 1:
    pass
else:
    st.text("informe o nome do treino:")
    st.text_input("insira aqui", key="titulo")
    st.text("informe os dados do treino:")
    st.text_input("insira aqui", key="dados")
    button_send = st.button("enviar")



