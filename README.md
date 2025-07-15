# Assistente Petbot: um chatbot de dúvidas com IA Generativa
## 📖 Sobre o Projeto
O Assistente PetBot é um chatbot desenvolvido para simular um assistente virtual. Utilizando o poder da Inteligência Artificial Generativa (LLMs), ele foi projetado para responder a perguntas comuns de tutores de pets, focando em cuidados básicos com cães (saúde e bem-estar).

Este projeto demonstra a capacidade de integrar modelos de linguagem avançados para criar interfaces de conversação intuitivas, com foco em automações e suporte ao cliente no segmento de pets.

## ✨ Recursos e Funcionalidades
- Interação Conversacional: Responde a perguntas em linguagem natural sobre tópicos pré-definidos.

- IA Generativa: Utiliza um Modelo de Linguagem Grande (LLM) para gerar respostas dinâmicas e contextuais.

- Alertas de Saúde: Inclui disclaimers importantes para problemas de saúde, orientando a busca por um médico veterinário.

- Interface Web Amigável: Desenvolvido com Streamlit para uma fácil interação via navegador.

- Versionamento de Código: Todo o projeto é versionado utilizando Git.

## 🚀 Tecnologias Utilizadas
<div>
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg" alt="Python" width='40' height='40'/>
  <img src="https://upload.wikimedia.org/wikipedia/commons/8/8a/Google_Gemini_logo.svg" alt="Google Gemini" width='40' height='40'/>
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/streamlit/streamlit-original.svg" alt="Streamlit" width='40' height='40'/>
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/git/git-original.svg" alt="Git" width='40' height='40'/>
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/github/github-original.svg" alt="Github" width='40' height='40'/>
</div>


## 🛠️ Como Executar o Projeto

**Pré-requisitos**
- Python 3.8+ instalado.
- Conta no Google AI Studio (para obter a API Key do Gemini).

**1. Clonar o Repositório**
```
git clone https://github.com/lais-zanardi/petbot-assistant
cd petbot-assistant
```

**2. Configurar o Ambiente Virtual**

Recomendamos criar e ativar um ambiente virtual para gerenciar as dependências do projeto.

```
python -m venv venv
```

Ativar o ambiente virtual:

- No Windows:
 ```
 .\venv\Scripts\activate
 ```

- No macOS / Linux:
 ```
 source venv/bin/activate
 ```

**3. Instalar as Dependências**

Com o ambiente virtual ativado, instale as bibliotecas necessárias usando o requirements.txt:
```
pip install -r requirements.txt
```

**4. Configurar a Chave da API do Google Gemini**

Obtenha sua chave de API no Google AI Studio.

Crie um arquivo chamado .env na raiz do seu projeto (na mesma pasta onde está app.py e chatbot_core.py).

Dentro do arquivo .env, adicione sua chave de API da seguinte forma:

```
GOOGLE_API_KEY="SUA_CHAVE_DE_API_AQUI"
```

**5. Executar o Chatbot**

Com o ambiente virtual ativado e a chave de API configurada, você pode rodar o aplicativo Streamlit:

```
streamlit run app.py
```
Isso abrirá o chatbot no seu navegador padrão (geralmente em http://localhost:8501).

## 🚀 Melhorias Futuras
Este é só o começo! Há muitas ideias para fazer este projeto crescer.

- **Gerenciamento de contexto e memória**: implementação do módulo *Memory* (LangChain) para que o chatbot se lembre do contexto da conversa anterior para um diálogo mais fluido.




## 📧 Contato
Se tiver qualquer pergunta, sugestão ou quiser saber mais, fique à vontade para entrar em contato.

[<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/linkedin/linkedin-original.svg" height='40'/>](https://www.linkedin.com/in/lais-zanardi-inocencio/)

## 📄 Licença
Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.