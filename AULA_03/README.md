# Programa de Residência em IA Generativa & RAG da PUC-Rio

## IA - Aula 03

Este repositório faz parte do Programa de Residência em IA Generativa & RAG da PUC-Rio e contém o notebook `embeddings_and_semantic_search.ipynb`, dividido em duas partes:

1. **Fundamentos de embeddings** — geração de embeddings via API, métricas de distância/similaridade e visualização;
2. **Desafio — Busca Semântica Manual** — implementação de um pipeline de busca semântica do zero, comparando três estratégias de fragmentação (chunking) de documentos.

O notebook cobre:

1. Geração de um embedding real a partir da API da OpenRouter (modelo `text-embedding-3-small`);
2. Implementação da **distância euclidiana** entre dois vetores;
3. Implementação da **distância de cosseno** entre dois vetores;
4. Testes das duas métricas com vetores simples e com termos do domínio da aula (animais, veículos e frutas);
5. Aplicação das métricas a **embeddings reais** dos mesmos termos, com redução de dimensionalidade via **PCA** e visualização em um **gráfico 3D**;
6. **Desafio de Busca Semântica Manual**: fragmentação dos documentos Markdown da AULA_02 em três granularidades (linha, parágrafo e capítulo), geração de embeddings em lote com controle de consumo de tokens, e recuperação dos TOP 3 trechos mais similares a uma query via Similaridade de Cosseno, comparando a qualidade dos resultados entre as três estratégias.

Essas etapas são preparatórias para o entendimento de como sistemas de RAG (Retrieval-Augmented Generation) fragmentam, comparam e recuperam informações semanticamente semelhantes.

> **Sobre o ambiente de desenvolvimento:** o exercício foi originalmente solicitado para ser resolvido no **Google Colab**, e foi lá que o notebook foi desenvolvido e testado (incluindo o carregamento da chave de API e o upload dos documentos via recursos nativos do Colab). Posteriormente, o notebook foi trazido para o **VS Code** para organização do repositório e versionamento local. Por isso, a Opção A abaixo reflete o ambiente original de desenvolvimento, e a Opção B descreve os ajustes necessários para rodá-lo localmente no VS Code.

Para garantir a eficiência de recursos e o isolamento das dependências ao rodar localmente, recomendamos fortemente o uso de um Ambiente Virtual Python (Virtual Environment ou `venv`).

## 📂 Estrutura do Projeto

```
AULA_03/
├── embeddings_and_semantic_search.ipynb   # Notebook principal: fundamentos de embeddings + desafio de busca semântica
└── requirements.txt                       # Dependências (uso opcional, para execução local)
```

> Os documentos Markdown usados no desafio (`twitter_algoritmo.md`, `escrita_academica_ia.md`, `bioetica_e_ia.md`) são os mesmos gerados na **AULA_02** a partir dos PDFs de origem, e não fazem parte deste repositório — eles são carregados manualmente durante a execução do notebook (veja o passo 6 abaixo).

## 🚀 Passo a Passo para Configuração e Execução

### Opção A — Google Colab (ambiente original do exercício)

Este exercício foi proposto para ser resolvido no Google Colab, e foi nele que o notebook foi desenvolvido, usando o gerenciador de _Secrets_ nativo para a chave de API e o widget de upload de arquivos.

1. Faça upload de `embeddings_and_semantic_search.ipynb` no Colab (ou abra diretamente pelo GitHub);
2. No menu lateral, clique no ícone de chave (🔑 _Secrets_) e adicione um secret chamado `OPENROUTER_API_KEY` com sua chave da OpenRouter;
3. Habilite o acesso do notebook a esse secret;
4. Execute as células em ordem (`Runtime > Run all` ou célula por célula);
5. Quando chegar na célula de upload (seção "Upload the Class Documents"), selecione os três arquivos `.md` gerados na AULA_02.

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

As principais dependências são: `numpy`, `pandas`, `scikit-learn`, `matplotlib`, `requests` e `python-dotenv`.

#### 4. Configurar as Variáveis de Ambiente (Segurança)

Para proteger seus dados, a chave de API nunca deve ser inserida diretamente no código nem comitada em repositórios públicos.

Crie um arquivo `.env` na raiz do projeto com a seguinte estrutura:

```env
OPENROUTER_API_KEY=sua_chave_de_api_aqui
```

_(Importante: adicione o arquivo `.env` ao seu `.gitignore` para não enviá-lo para o GitHub)._

> **Nota:** o notebook, por padrão, carrega a chave via `google.colab.userdata` (Secrets do Colab) e faz o upload dos documentos via `google.colab.files` (Widget de upload). Nenhum dos dois está disponível fora do Colab. Para rodar localmente, substitua:
>
> - a célula de carregamento da chave por uma leitura via `python-dotenv` (`os.getenv("OPENROUTER_API_KEY")`);
> - a célula de upload por uma simples cópia dos três arquivos `.md` da AULA_02 para a mesma pasta do notebook (o código já lê os arquivos pelo nome, sem depender do widget).

#### 5. Executar o Notebook

```bash
jupyter notebook embeddings_and_semantic_search.ipynb
```

Execute as células em ordem, de cima para baixo.

## 📝 Conteúdo do Notebook

### Parte 1 — Fundamentos de Embeddings

| Seção                                 | Descrição                                                                                                                                                                          |
| ------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 1. Geração de Embedding               | Chamada à API da OpenRouter (`text-embedding-3-small`) para gerar o embedding de uma frase de exemplo.                                                                             |
| 2. Distância Euclidiana               | Função `euclidean_distance()`, que calcula a distância euclidiana entre dois vetores de qualquer dimensão (desde que do mesmo tamanho).                                            |
| 3. Distância de Cosseno               | Função `cosine_distance()`, que calcula `1 - similaridade de cosseno` entre dois vetores.                                                                                          |
| 4. Testes com Vetores e Termos        | Validação das duas funções com vetores simples (`[1,0,0]`, `[0,1,0]`) e com termos do domínio da aula: gato, felino, cachorro, carro, caminhão, moto, banana, maçã e goiaba.       |
| 5. Embeddings Reais e Visualização 3D | Geração de embeddings reais (via API) para os mesmos termos, redução de dimensionalidade com PCA e visualização em um gráfico 3D, colorido por categoria (animal, veículo, fruta). |

### Parte 2 — Desafio: Busca Semântica Manual

| Seção                        | Descrição                                                                                                                                                                 |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Funções de distância (NumPy) | Versões otimizadas com NumPy das métricas da Parte 1, usadas para lidar com centenas de embeddings reais de forma eficiente.                                              |
| Helpers de embedding         | Funções para gerar embeddings individuais e em lote, com rastreamento do total de tokens consumidos em cada requisição.                                                   |
| Termos e frases reais        | Reaplica as métricas a embeddings reais dos termos da aula e a um exemplo de comparação entre frases (similar, relacionado, diferente e oposto).                          |
| Chunking por Linha           | Divide os documentos `.md` linha a linha, gera os embeddings e recupera o TOP 3 mais similar a uma query.                                                                 |
| Chunking por Parágrafo       | Divide os documentos por blocos separados por linha em branco, filtrando blocos muito curtos.                                                                             |
| Chunking por Capítulo        | Divide os documentos por seções marcadas com `## ` no Markdown.                                                                                                           |
| Comparação das estratégias   | Roda a mesma query nas três granularidades lado a lado, para observar o impacto do tamanho do trecho na relevância, contexto e especificidade dos resultados recuperados. |

---

### 🛑 Como sair do Ambiente Virtual?

Se estiver rodando localmente, ao terminar de programar, desative o ambiente virtual executando:

```bash
deactivate
```
