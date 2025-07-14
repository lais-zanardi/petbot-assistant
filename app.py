import streamlit as st
from chatbot_core import get_petbot_chatbot_response

# Título e ícone da aba do navegador
st.set_page_config(page_title="Assistente PetBot", page_icon="🐾")

st.title("🐾 Chatbot de dúvidas")
st.markdown("Olá! Eu sou seu assistente virtual PetBot. Pergunte-me sobre **cuidados básicos com cães**")

# Caixa de texto para entradas do usuário
user_input = st.text_area("Sua pergunta: ", key="user_question")

# Botão para enviar a pergunta
if st.button("Perguntar ao PetBot"):
    if user_input:
        with st.spinner("Pensando na sua resposta... 🐶"):
            response = get_petbot_chatbot_response(user_input)
            st.markdown(f"**Resposta do PetBot:** \n\n{response}")
    else:
        st.warning("Por favor, digite uma pergunta antes de enviar.")

st.markdown("---")
st.markdown("💡 **Dica:** Se a pergunta for sobre um problema de saúde grave, sempre consulte um médico veterinário.")