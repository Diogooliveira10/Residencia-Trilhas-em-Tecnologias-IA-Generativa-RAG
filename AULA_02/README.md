# Programa de Residência em IA Generativa & RAG da PUC-Rio

## Introdução à IA - Aula 02

Este repositório faz parte do Programa de Residência em IA Generativa & RAG da PUC-Rio e contém o código para:

1. Conversão de arquivos PDF em Markdown utilizando a biblioteca [Docling](https://github.com/docling-project/docling);
2. Extração de metadados (título, autores, ano, resumo e palavras-chave) dos arquivos Markdown gerados, utilizando Structured Outputs da API da OpenAI.

Essas etapas são preparatórias para pipelines de RAG (Retrieval-Augmented Generation).

Para garantir a eficiência de recursos e o isolamento das dependências, recomendamos fortemente o uso de um Ambiente Virtual Python (Virtual Environment ou `venv`).

## 📂 Estrutura do Projeto

```
AULA_02/
├── pdfs/                    # PDFs de origem (entrada)
│   ├── bioetica_e_ia.pdf
│   ├── escrita_academica_ia.pdf
│   └── twitter_algoritmo.pdf
├── markdown/                 # Arquivos .md gerados (saída da conversão)
├── json/                      # Arquivos .json com metadados extraídos (saída da extração)
├── pdf_converter.py            # Script de conversão PDF → Markdown
└── extract_metadata.py          # Script de extração de metadados Markdown → JSON
```

## 🚀 Passo a Passo para Configuração e Execução

### 1. Criar o Ambiente Virtual (venv)

Abra o seu terminal na pasta raiz do projeto (`/IA`) e execute o seguinte comando para criar o ambiente virtual:

```bash
# No Linux/macOS
python3 -m venv venv

# No Windows
python -m venv venv
```

### 2. Ativar o Ambiente Virtual

Sempre que for trabalhar no projeto ou rodar os códigos, você precisa ativar o `venv`.

```bash
# No Linux/macOS
source venv/bin/activate

# No Windows
venv\Scripts\activate
```

_(Você saberá que o ambiente está ativado porque o nome `(venv)` aparecerá no início da linha de comando do terminal)._

### 3. Instalar as Dependências

Com o ambiente ativado, instale as bibliotecas necessárias (`docling`, `openai` e `python-dotenv`) a partir do arquivo `requirements.txt` que está na raiz do projeto:

```bash
pip install -r requirements.txt
```

_(Na primeira execução, o Docling baixa automaticamente o modelo de análise de layout a partir do Hugging Face — é necessário ter conexão com a internet nesse primeiro momento; depois disso, o modelo fica em cache local)._

### 4. Configurar as Variáveis de Ambiente (Segurança)

Para proteger seus dados e garantir a segurança, as chaves de API nunca devem ser inseridas diretamente no código nem comitadas em repositórios públicos.

Certifique-se de que o arquivo `.env` exista na raiz do projeto (ou dentro de `AULA_02`, dependendo de onde for executar) com a seguinte estrutura:

```env
OPENAI_API_KEY=sua_chave_de_api_aqui
OPENAI_BASE_URL=https://openrouter.ai/api/v1
OPENAI_MODEL=nome_do_modelo_aqui
```

_(`OPENAI_BASE_URL` só é necessário se você estiver usando um provedor compatível com a API da OpenAI, como o OpenRouter. Usando a OpenAI diretamente, essa linha pode ser removida)._

_(Importante: adicione o arquivo `.env` ao seu `.gitignore` para não enviá-lo para o GitHub)._

### 5. Converter os PDFs em Markdown

Coloque os arquivos PDF que deseja converter dentro da pasta `pdfs/`, na raiz do projeto, e execute:

```bash
cd AULA_02
python pdf_converter.py
```

O script converte **um PDF por vez**: o caminho do arquivo de entrada é definido na chamada de `convert_pdf()` dentro do bloco `if __name__ == "__main__":`. Para converter outro PDF, basta atualizar o caminho passado como primeiro argumento.

O arquivo `.md` resultante é salvo na pasta `markdown/`, com o mesmo nome do PDF original.

**Sobre o OCR:** por padrão, o script roda com `do_ocr=False`, pois os PDFs utilizados possuem texto nativo (não são digitalizados/escaneados). Isso evita erros de estouro de memória (`std::bad_alloc`) que podem ocorrer ao processar imagens em alta resolução durante o OCR. Caso precise converter PDFs escaneados, ative o OCR alterando essa opção no script.

### 6. Extrair Metadados dos Arquivos Markdown

Com os arquivos `.md` já gerados na pasta `markdown/`, execute:

```bash
python extract_metadata.py
```

Assim como o conversor de PDF, o script processa **um arquivo por vez**: o caminho do markdown de entrada é definido na chamada de `extract_metadata()` dentro do bloco `if __name__ == "__main__":`.

O script utiliza Structured Outputs da API da OpenAI para extrair, de forma estruturada e validada por schema, os seguintes campos:

- `titulo`
- `autores` (lista de strings)
- `ano`
- `resumo`
- `palavras_chave` (lista de strings)

O modelo é instruído, via _system prompt_, a seguir regras estritas de extração:

- Extrair apenas informações explicitamente presentes no documento;
- Nunca inventar ou inferir dados;
- Retornar `null` quando um campo estiver ausente;
- Preservar o texto original do documento (sem parafrasear);
- Não incluir explicações ou texto adicional na resposta.

O arquivo `.json` resultante é salvo na pasta `json/`, com o mesmo nome do markdown original.

---

### 🛑 Como sair do Ambiente Virtual?

Quando terminar de programar, você pode desativar o ambiente virtual executando simplesmente:

```bash
deactivate
```
