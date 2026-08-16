# Programa de Residência em IA Generativa & RAG | PUC-Rio

## IA - Aula 05

![Python](https://img.shields.io/badge/Python-3.11%2B-blue?style=flat-square&logo=python)
![LangChain](https://img.shields.io/badge/LangChain-Core%20%7C%20HuggingFace-1C3C3C?style=flat-square)
![Sentence Transformers](https://img.shields.io/badge/Sentence--Transformers-all--MiniLM--L6--v2-FF6F00?style=flat-square)
![Google Colab](https://img.shields.io/badge/Google%20Colab-compatible-F9AB00?style=flat-square&logo=googlecolab)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)

Este repositório faz parte do Programa de Residência em IA Generativa & RAG da PUC-Rio e contém o notebook `documents.ipynb`, com o desafio **Documents, Metadados e Busca Vetorial com LangChain**: migrar a estrutura manual de chunk construída "na mão" na Aula 04 para o formato padrão `Document` do LangChain, projetar um schema de metadados e (em etapas futuras) indexar os documentos numa vector store para busca semântica com filtros.

O notebook cobre, até o momento:

1. **Exercício 1 — Documents na mão**: criação manual de uma lista de `Document` (`page_content` + `metadata`), cobrindo pelo menos dois temas do curso, e investigação de dois comportamentos do `Document`: quais tipos de dado `metadata` aceita (incluindo listas e dicionários aninhados) e o que acontece ao criar um `Document` sem passar `metadata`;
2. **Exercício 2 — Schema de metadados**: definição de um schema de metadados para os chunks gerados na Aula 04, com os 7 campos mínimos exigidos mais 3 campos próprios (`n_tokens`, `overlap_percentual`, `hash_conteudo`), cada um justificado a partir de uma necessidade real do pipeline (orçamento de contexto do LLM, redundância entre chunks vizinhos, deduplicação entre estratégias).

> **Sobre o `Document`:** diferente da estrutura manual da Aula 04, o `Document` do LangChain tem apenas dois campos — `page_content` e `metadata`. Não existe campo de embedding: o vetor é responsabilidade da vector store, não do documento.

## 📂 Estrutura do Projeto

```
AULA_05/
├── documents.ipynb     # Notebook principal: Documents e metadados
└── requirements.txt    # Dependências (uso opcional, para execução local)
```

## 🚀 Passo a Passo para Configuração e Execução

1. Abra `documents.ipynb` no Google Colab ou em um Jupyter local;
2. Execute a primeira célula para instalar as dependências (`langchain-core`, `langchain-text-splitters`, `sentence-transformers`, `langchain-huggingface`);
3. Execute as células em ordem — os Exercícios 1 e 2 não dependem de chave de API nem de arquivos externos, rodam de forma independente.

> **Nota:** etapas futuras deste desafio (indexação numa vector store e geração de embeddings com o modelo local `sentence-transformers/all-MiniLM-L6-v2`) reaproveitam os `.md` e chunks gerados na Aula 04 e podem exigir mais poder de processamento — o enunciado recomenda usar o Google Colab caso não tenha um PC apropriado.

## 📝 Conteúdo do Notebook

| Seção                             | Descrição                                                                                                                                                                                                                                                                   |
| --------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Exercício 1 — Documents na mão    | Cria manualmente 5 `Document` (temas: embeddings e chunking), lista `page_content`/`metadata` de cada um, e investiga o comportamento do campo `metadata` (tipos aceitos e valor padrão quando omitido).                                                                    |
| Exercício 2 — Schema de metadados | Projeta o schema de metadados dos chunks da Aula 04: tabela com os 7 campos mínimos + 3 próprios, justificativa de cada campo próprio, exemplo JSON preenchido com dados realistas do pipeline da Aula 04, e respostas sobre citação de fonte e utilidade do `chunk_index`. |
