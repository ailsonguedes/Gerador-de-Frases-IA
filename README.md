<h1 align='center'> Gerador de Frases Motivacionais </h1> 

<p align='center'>Este é um gerador de frases motivacionais desenvolvido em Python, utilizando o modelo de linguagem <strong>FLAN-T5</strong> da Hugging Face. A aplicação recebe um tema e retorna uma frase curta e inspiradora relacionada ao tema escolhido.</p> 

<div align='center'> 
    <a href="https://www.python.org/" target="_blank"> 
        <img src="./img/python_logo.png" width="150" height="150" /> 
    </a> 
    <a href="https://huggingface.co/docs/transformers/index" target="_blank"> 
        <img src="https://huggingface.co/front/assets/huggingface_logo.svg" width="150" height="150" /> 
    </a> 
</div>



## 🔧 Ferramentas

-   Python: é uma linguagem de programação de alto nível, interpretada, orientada a objetos e de propósito geral.
-   Transformers (Hugging Face): Biblioteca para trabalhar com modelos de linguagem pré-treinados, como o FLAN-T5.
-   Python-dotenv: Biblioteca para carregar variáveis de ambiente a partir de arquivos .env.

## 💻 Como Executar o Projeto

Siga estas etapas para configurar e executar a API em seu ambiente:

1. Clone este repositório:

  ```shell
  git clone https://github.com/seu-usuario/gerador-frases.git
  ```
2. Navegue até o diretório do projeto:

  ```shell
  cd gerador-frases/
  ```
3. Crie e ative um ambiente virtual:

  ```shell
  python -m venv venv
  source venv/bin/activate  # No Windows, use 'venv\Scripts\activate'
  ```
4. Instale as dependências:

  ```shell
  pip install -r requirements.txt
  ```
5. Crie um arquivo .env e adicione:

  ```shell
  HF_TOKEN=seu_token_aqui
  ```
6. Execute o script principal:

  ```shell
  python main.py
  ```
## 📝 Como Usar:
    Ao rodar o script, digite um tema quando solicitado, por exemplo: focus, courage, perseverance.
    O gerador retornará uma frase motivacional curta baseada no tema escolhido.


## 🙏 Contribuição:

Contribuições são bem-vindas! Você pode:
- Abrir issues para relatar problemas ou melhorias.
- Enviar pull requests com novas funcionalidades ou correções.
- Dar feedback sobre a aplicação.