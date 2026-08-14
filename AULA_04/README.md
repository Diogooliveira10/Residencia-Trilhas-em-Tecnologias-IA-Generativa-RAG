# Programa de Residência em IA Generativa & RAG | PUC-Rio

## IA - Aula 04

Este repositório faz parte do Programa de Residência em IA Generativa & RAG da PUC-Rio e contém o notebook `chunking.ipynb`, com o desafio **Avaliação de Estratégias de Chunking com LangChain**: um pipeline completo que converte PDFs reais em Markdown, aplica **10 estratégias diferentes de chunking**, gera embeddings para cada trecho e exporta os resultados em JSON, para comparar como cada estratégia afeta a qualidade da representação dos documentos.

O notebook cobre o pipeline completo:

```
PDF → Markdown → Chunking (10 estratégias) → Embeddings → JSON
```

1. Extração dos PDFs para Markdown estruturado via **Docling** (mesma ferramenta da Aula 02), avaliando como tabelas, imagens e headings sobrevivem à conversão;
2. Implementação das 10 estratégias de chunking com os splitters do **LangChain**: tamanho fixo (200/500/1000/2000 caracteres), tamanho fixo com overlap (leve e pesado), por parágrafo, por sentenças agrupadas, recursivo e por estrutura Markdown;
3. Geração de embeddings para cada chunk via API da OpenRouter, com rastreamento de tokens consumidos por teste;
4. Exportação de cada experimento em `chunks_embeddings.json`, e um `summary.json` comparativo entre os 10 testes de cada documento;
5. Execução do pipeline completo nos 11 PDFs reais da base de referência (8 papers de IA + 3 documentos reaproveitados da Aula 02).

O pipeline foi construído com foco em **resiliência**: falhas pontuais (um chunk que excede o limite de tokens do modelo, uma desconexão de runtime) não descartam o trabalho já feito — resultados são salvos incrementalmente, execuções interrompidas retomam de onde pararam, e o motivo do problema fica registrado no próprio `summary.json`.

> **Sobre o ambiente de desenvolvimento:** diferente da Aula 03, este notebook é desenvolvido e executado inteiramente no **Google Colab**. A extração de PDF via Docling baixa modelos do Hugging Face na primeira execução e é sensível ao hardware disponível (CPU vs. GPU), e o pipeline completo processa um volume grande de dados ao longo de várias horas — por isso o Google Drive é montado para persistir os resultados entre sessões, em vez de depender do disco efêmero da VM. Rodar localmente é possível, mas não é o caminho testado.

## 📂 Estrutura do Projeto

```
AULA_04/
├── chunking.ipynb   # Notebook principal: extração, chunking, embeddings, export
├── pdfs/                     # 11 PDFs de origem (entrada)
│   ├── attention_is_all_you_need.pdf
│   ├── bert_pretraining.pdf
│   ├── bioetica_e_ia.pdf
│   ├── escrita_academica_ia.pdf
│   ├── gpt3_language_models.pdf
│   ├── gpt4_technical_report.pdf
│   ├── instruct_gpt.pdf
│   ├── llama_foundation_models.pdf
│   ├── lora_low_rank_adaptation.pdf
│   ├── retrieval_augmented_generation.pdf
│   ├── scaling_laws_llm.pdf
│   └── twitter_algoritmo.pdf
└── requirements.txt          # Dependências (uso opcional, para execução local)
```

> Os resultados (`results/<documento>/markdown/`, `results/<documento>/test_XX/chunks_embeddings.json`, `results/summary.json`) são gerados pelo próprio notebook e persistidos no Google Drive do usuário — não fazem parte deste repositório.

## 🚀 Passo a Passo para Configuração e Execução

1. Faça upload de `chunking.ipynb` no Google Colab (ou abra diretamente pelo GitHub);
2. No menu lateral, clique no ícone de chave (🔑 _Secrets_) e adicione um secret chamado `OPENROUTER_API_KEY` com sua chave da OpenRouter;
3. Habilite o acesso do notebook a esse secret;
4. Execute a célula que monta o Google Drive (seção "Persist Results to Google Drive") e autorize o acesso quando solicitado;
5. Execute as células em ordem (`Runtime > Run all` ou célula por célula). Quando chegar na seção "Upload and Convert All PDFs", selecione os 11 arquivos da pasta `pdfs/`;
6. Se a execução for interrompida (desconexão, créditos insuficientes, etc.), basta rodar a célula do Passo 5 novamente — documentos já processados são identificados automaticamente e pulados, sem reprocessar (nem regastar tokens).

### Sobre a chave de API e créditos

O notebook usa o modelo `text-embedding-3-small` via OpenRouter. Contas gratuitas têm um limite de tokens por período — rodar os 11 documentos × 10 estratégias pode exceder esse limite. Se isso acontecer, o notebook para o processamento com uma mensagem clara indicando para adicionar créditos em [openrouter.ai/settings/credits](https://openrouter.ai/settings/credits) ou trocar `EMBEDDING_MODEL` por uma alternativa gratuita, como o [Hugging Face Inference API](https://huggingface.co/blog/getting-started-with-embeddings).

## 📝 Conteúdo do Notebook

### Estratégias de Chunking Avaliadas

| Teste | Estratégia     | Configuração                  | Variável isolada      |
| ----- | -------------- | ----------------------------- | --------------------- |
| 1     | Fixo           | 200 caracteres, sem overlap   | Tamanho extremo baixo |
| 2     | Fixo           | 500 caracteres, sem overlap   | Tamanho               |
| 3     | Fixo           | 1000 caracteres, sem overlap  | Tamanho               |
| 4     | Fixo           | 2000 caracteres, sem overlap  | Tamanho extremo alto  |
| 5     | Fixo + overlap | 500 caracteres, overlap 50    | Overlap leve          |
| 6     | Fixo + overlap | 500 caracteres, overlap 200   | Overlap pesado        |
| 7     | Por parágrafo  | Separação por parágrafos      | Estrutura natural     |
| 8     | Por sentença   | Sentenças agrupadas em 3      | Estrutura natural     |
| 9     | Recursivo      | Separadores hierárquicos      | Estratégia composta   |
| 10    | Markdown       | Separação por headings/seções | Estrutura semântica   |

### Pipeline

| Seção                             | Descrição                                                                                                                                                                     |
| --------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Configuração e contratos de dados | Definição de `TestConfig`, `ChunkMetadata`, `ChunkRecord` e dos caminhos de saída (`results/<documento>/...`).                                                                |
| PDF → Markdown (Docling)          | Conversão dos 11 PDFs com OCR desativado (texto nativo), com checagem estrutural de tabelas e imagens preservadas na conversão.                                               |
| 10 estratégias de chunking        | Implementação de cada estratégia usando os splitters do LangChain (`RecursiveCharacterTextSplitter`, `CharacterTextSplitter`, `MarkdownHeaderTextSplitter`, etc.).            |
| Geração de embeddings             | Embeddings em lote com rastreamento de tokens, fallback item a item quando um lote falha (ex: chunk grande demais), e parada imediata em caso de créditos insuficientes.      |
| Execução completa                 | Roda as 10 estratégias nos 11 documentos reais, salvando `chunks_embeddings.json` por teste e um `summary.json` comparativo — com retomada automática em caso de interrupção. |

## 📌 Status

🟡 Em andamento — o pipeline está implementado e validado, mas a execução completa nos 11 documentos ainda está em curso (interrompida por limite de créditos da API). Ainda faltam:

- Concluir a execução completa (todos os 11 documentos × 10 estratégias);
- Análise comparativa respondendo as 15 perguntas obrigatórias do desafio (qual estratégia gerou mais/menos chunks, tratamento de tabelas e imagens, estratégia mais adequada para RAG, etc.);
- Relatório final consolidando configurações, estatísticas e conclusões.
