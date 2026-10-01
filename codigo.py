# Chat bot com IA
# Bibliotecas pra baixar: streamlit openai

import streamlit as st
from openai import OpenAI

# Configuração da página
st.set_page_config(
    page_title="ChatBot IA",
    page_icon="🤖",
    layout="centered"
)

modelo_ia = OpenAI(
    api_key="minha_chave_API",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai"
)

# Css

st.markdown("""
<style>

    /* Fundo da página */
    .stApp {
        background: linear-gradient(135deg, #0f172a, #1e1b4b, #312e81);
        color: white;
    }

    /* Container principal */
    .main .block-container {
        max-width: 850px;
        padding-top: 3rem;
        padding-bottom: 3rem;
    }

    /* Título */
    .titulo {
        text-align: center;
        font-size: 42px;
        font-weight: 800;
        margin-bottom: 5px;
        color: #ffffff;
    }

    /* Subtítulo */
    .subtitulo {
        text-align: center;
        font-size: 17px;
        color: #c7d2fe;
        margin-bottom: 35px;
    }

    /* Caixa de apresentação */
    .welcome {
        background: rgba(255, 255, 255, 0.08);
        border: 1px solid rgba(255, 255, 255, 0.15);
        border-radius: 20px;
        padding: 25px;
        text-align: center;
        margin-bottom: 25px;
        backdrop-filter: blur(10px);
    }

    .welcome h2 {
        margin-bottom: 8px;
        color: #ffffff;
    }

    .welcome p {
        color: #cbd5e1;
        margin: 0;
    }

    /* Campo de mensagem */
    .stChatInput {
        border-radius: 15px;
    }

    /* Mensagens */
    [data-testid="stChatMessage"] {
        border-radius: 18px;
        padding: 10px;
        margin-bottom: 10px;
    }

    /* Rodapé */
    .footer {
        text-align: center;
        color: #94a3b8;
        font-size: 13px;
        margin-top: 30px;
    }

</style>
""", unsafe_allow_html=True)


## Header

st.markdown(
    '<div class="titulo">🤖 ChatBot IA</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitulo">Seu assistente inteligente para conversar e tirar dúvidas.</div>',
    unsafe_allow_html=True
)


if "lista_mensagens" not in st.session_state:
    st.session_state["lista_mensagens"] = []

if len(st.session_state["lista_mensagens"]) == 0:

    st.markdown("""
    <div class="welcome">
        <h2>👋 Olá! Como posso ajudar?</h2>
        <p>Digite uma mensagem abaixo e converse com a inteligência artificial.</p>
    </div>
    """, unsafe_allow_html=True)


#campo de mensagem
mensagem_usuario = st.chat_input(
    "💬 Digite sua mensagem..."
)



# Historico de mensagens
for mensagem in st.session_state["lista_mensagens"]:

    quem_enviou = mensagem["role"]
    texto_mensagem = mensagem["content"]

    st.chat_message(
        quem_enviou
    ).write(texto_mensagem)


#envio de mensagem
if mensagem_usuario:

    # Exibir mensagem do usuario
    st.chat_message("user").write(mensagem_usuario)

    mensagem1 = {
        "role": "user",
        "content": mensagem_usuario
    }

    st.session_state["lista_mensagens"].append(mensagem1)


    # Modelo da mensagem IA
    resposta_modelo = modelo_ia.chat.completions.create(

        messages=st.session_state["lista_mensagens"],

        model="gemini-flash-lite-latest"
    )


    # Resposta da IA
    resposta_ia = resposta_modelo.choices[0].message.content


    # Exibir resposta da IA
    st.chat_message("assistant").write(resposta_ia)


    mensagem2 = {
        "role": "assistant",
        "content": resposta_ia
    }

    st.session_state["lista_mensagens"].append(mensagem2)


# rodapé
st.markdown("""
<div class="footer">
    Desenvolvido com Python + Streamlit 
</div>
""", unsafe_allow_html=True)