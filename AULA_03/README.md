# Programa de Residência em IA Generativa & RAG da PUC-Rio

## IA - Aula 03

Este repositório faz parte do Programa de Residência em IA Generativa & RAG da PUC-Rio e contém o notebook `embeddings_analysis.ipynb`, com exercícios práticos sobre **embeddings** e **métricas de similaridade/distância**, aplicados a um caso real de geração de embeddings via API.

O notebook cobre:

1. Geração de um embedding real a partir da API da OpenRouter (modelo `text-embedding-3-small`);
2. Implementação da **distância euclidiana** entre dois vetores;
3. Implementação da **distância de cosseno** entre dois vetores;
4. Testes das duas métricas com vetores simples e com termos do domínio da aula (animais, veículos e frutas);
5. Aplicação das métricas a **embeddings reais** dos mesmos termos, com redução de dimensionalidade via **PCA** e visualização em um **gráfico 3D**.

Essas etapas são preparatórias para o entendimento de como sistemas de RAG (Retrieval-Augmented Generation) comparam e recuperam informações semanticamente semelhantes.

> **Sobre o ambiente de desenvolvimento:** o exercício foi originalmente solicitado para ser resolvido no **Google Colab**, e foi lá que o notebook foi desenvolvido e testado (incluindo o carregamento da chave de API via _Secrets_ do Colab). Posteriormente, o notebook foi trazido para o **VS Code** para organização do repositório e versionamento local. Por isso, a Opção A abaixo reflete o ambiente original de desenvolvimento, e a Opção B descreve os ajustes necessários para rodá-lo localmente no VS Code.

Para garantir a eficiência de recursos e o isolamento das dependências ao rodar localmente, recomendamos fortemente o uso de um Ambiente Virtual Python (Virtual Environment ou `venv`).

## 📂 Estrutura do Projeto

```
AULA_03/
├── embeddings_analysis.ipynb   # Notebook principal com os 5 exercícios
└── requirements.txt             # Dependências (uso opcional, para execução local)
```

## 🚀 Passo a Passo para Configuração e Execução

### Opção A — Google Colab (ambiente original do exercício)

Este exercício foi proposto para ser resolvido no Google Colab, e foi nele que o notebook foi desenvolvido, usando o gerenciador de _Secrets_ nativo para a chave de API.

1. Faça upload de `embeddings_analysis.ipynb` no Colab (ou abra diretamente pelo GitHub);
2. No menu lateral, clique no ícone de chave (🔑 _Secrets_) e adicione um secret chamado `OPENROUTER_API_KEY` com sua chave da OpenRouter;
3. Habilite o acesso do notebook a esse secret;
4. Execute todas as células em ordem (`Runtime > Run all` ou célula por célula).

### Opção B — VS Code / Jupyter local (ambiente atual do repositório)

Após o desenvolvimento no Colab, o notebook foi migrado para o VS Code. Para rodá-lo localmente:

#### 1. Criar o Ambiente Virtual (venv)

Abra o terminal na pasta raiz do projeto e execute:

```bash
# No Linux/macOS
python3 -m venv venv

# No Windows
python -m venv venv
```

#### 2. Ativar o Ambiente Virtual

```bash
# No Linux/macOS
source venv/bin/activate

# No Windows
venv\Scripts\activate
```

_(Você saberá que o ambiente está ativado porque o nome `(venv)` aparecerá no início da linha de comando do terminal)._

#### 3. Instalar as Dependências

Com o ambiente ativado, instale as bibliotecas necessárias:

```bash
pip install -r requirements.txt
```

As principais dependências são: `numpy`, `scikit-learn`, `matplotlib`, `requests` e `python-dotenv`.

#### 4. Configurar as Variáveis de Ambiente (Segurança)

Para proteger seus dados, a chave de API nunca deve ser inserida diretamente no código nem comitada em repositórios públicos.

Crie um arquivo `.env` na raiz do projeto com a seguinte estrutura:

```env
OPENROUTER_API_KEY=sua_chave_de_api_aqui
```

_(Importante: adicione o arquivo `.env` ao seu `.gitignore` para não enviá-lo para o GitHub)._

> **Nota:** o notebook, por padrão, carrega a chave via `google.colab.userdata` (Secrets do Colab). Para rodar localmente, substitua essa célula por uma leitura via `python-dotenv` (`os.getenv("OPENROUTER_API_KEY")`).

#### 5. Executar o Notebook

```bash
jupyter notebook embeddings_analysis.ipynb
```

Execute as células em ordem, de cima para baixo.

## 📝 Conteúdo do Notebook

| Seção                                 | Descrição                                                                                                                                                                          |
| ------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1. Geração de Embedding               | Chamada à API da OpenRouter (`text-embedding-3-small`) para gerar o embedding de uma frase de exemplo.                                                                             |
| 2. Distância Euclidiana               | Função `euclidean_distance()`, que calcula a distância euclidiana entre dois vetores de qualquer dimensão (desde que do mesmo tamanho).                                            |
| 3. Distância de Cosseno               | Função `cosine_distance()`, que calcula `1 - similaridade de cosseno` entre dois vetores.                                                                                          |
| 4. Testes com Vetores e Termos        | Validação das duas funções com vetores simples (`[1,0,0]`, `[0,1,0]`) e com termos do domínio da aula: gato, felino, cachorro, carro, caminhão, moto, banana, maçã e goiaba.       |
| 5. Embeddings Reais e Visualização 3D | Geração de embeddings reais (via API) para os mesmos termos, redução de dimensionalidade com PCA e visualização em um gráfico 3D, colorido por categoria (animal, veículo, fruta). |

---

### 🛑 Como sair do Ambiente Virtual?

Se estiver rodando localmente, ao terminar de programar, desative o ambiente virtual executando:

```bash
deactivate
```
