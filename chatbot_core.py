import os 
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Configura a API do LLM
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel('gemini-2.5-pro')


# Função central de interação com o LLM
def get_petbot_chatbot_response(user_message):
    system_instruction = (
        "Você é um chatbot amigável e prestativo, especializado em responder perguntas sobre "
        "cuidados básicos com cães (alimentação, higiene, comportamento simples). "
        "Forneça respostas concisas e úteis. Se a pergunta for sobre um problema de saúde grave ou diagnóstico, "
        "SEMPRE oriente o usuário a procurar um médico veterinário imediatamente e não tente diagnosticar. "
        "Mantenha um tom profissional e empático."
    )

    full_prompt = f"{system_instruction}\n\nPergunta do usuário: {user_message}"
    try:
        response = model.generate_content(full_prompt)
        return response.text if response.text else "Desculpe, não consegui gerar uma resposta para isso no momento."

    except Exception as e:
        print(f"Erro ao chamar a API do LLM: {e}")
        return "Desculpe, houve um erro ao processar sua solicitação. Por favor, tente novamente mais tarde."

# Teste
if __name__ == "main":
    print("Olá! Sou o Assistente PetBot. Pergunte-me sobre cuidados básicos com cães ou digite 'sair'.")
    while True:
        user_input = input("Você: ")
        if user_input.lower() == 'sair':
            break
        response = get_petbot_chatbot_response(user_input)
        print(f"Assistente PetBot: {response}")
