import streamlit as st
import requests as re

response = re.get("http://carlosg18.pythonanywhere.com/treino/list_treino/")


tela = 0

st.title("DATARUNNER")
st.sidebar.text("")
opcao = st.sidebar.selectbox("escolha uma opção", options=["adicionar dados", "visualizar dados", "criar novos treinos"])


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
    st.divider()
    st.text("data do treino:")
    st.date_input("data")
    st.divider()
    st.text("informe os dados do treino:")
    st.text_area("insira aqui", key="dados")
    button_send = st.button("enviar")
    if button_send:
        st.write("butao enviar apertado")
        request = re.post("http://carlosg18.pythonanywhere.com/treino/receber_dados", data={
            "title": st.session_state.titulo,
            "dados": st.session_state.dados,
        })
        st.write(request.json())
elif tela == 1:
    st.write(response.json())
else:
    st.text("informe o nome do treino:")
    st.text_input("insira aqui", key="titulo")
    st.text("informe os dados do treino:")
    st.text_input("insira aqui", key="dados")
    button_send = st.button("enviar")





