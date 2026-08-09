# 🤖 Programa de Residência em IA Generativa & RAG | PUC-Rio

> Repositório com os estudos, exercícios, projetos e anotações desenvolvidos durante o Programa de Residência em IA Generativa & RAG da PUC-Rio.

## 👨‍💻 Aluno

**Diogo Oliveira Vieira**

## 📖 Sobre

Este repositório reúne todo o material produzido ao longo da residência, incluindo:

- 📚 Conteúdo das aulas
- 💻 Exercícios práticos
- 📝 Resumos e anotações
- 🚀 Projetos desenvolvidos
- 🤖 Experimentos com Inteligência Artificial Generativa, LLMs e RAG
  O objetivo é documentar minha evolução durante o programa e servir como portfólio de aprendizado.

---

# 📚 Conteúdo das Aulas

## 📁 Aula 01 — configuracao-openai

### Conteúdos abordados

- Configuração do ambiente de desenvolvimento
- Integração da API da OpenAI utilizando variáveis de ambiente (`.env`)
- Primeiros testes de requisições via terminal
- Configuração e utilização da OpenAI como provedor de modelos de IA

### Tecnologias

- Python
- OpenAI API
- OpenRouter
- jupyter
- python-dotenv

---

## 📁 Aula 02 — conversao-pdf-e-extracao-metadados

### Conteúdos abordados

- Conversão de arquivos PDF em Markdown utilizando a biblioteca Docling
- Ajuste de pipeline options do Docling (desativação de OCR) para evitar erros de memória em PDFs com texto nativo
- Extração estruturada de metadados (título, autores, ano, resumo e palavras-chave) dos arquivos Markdown gerados
- Uso de Structured Outputs da API da OpenAI, com schema JSON estrito, para garantir a validade e o formato dos dados extraídos
- Escrita de _system prompts_ com regras explícitas para evitar alucinação do modelo (nunca inventar dados, preservar texto original, retornar `null` para campos ausentes)

### Tecnologias

- Python
- Docling
- OpenAI API (Structured Outputs)
- OpenRouter
- python-dotenv

---

## 📁 Aula 03 — embeddings-e-metricas-de-similaridade

### Conteúdos abordados

- Geração de embeddings reais via API da OpenRouter (modelo `text-embedding-3-small`)
- Implementação, do zero, da **distância euclidiana** entre dois vetores de qualquer dimensão
- Implementação, do zero, da **distância de cosseno** (1 − similaridade de cosseno) entre dois vetores
- Validação das métricas com vetores de teste simples e com termos de domínio (animais, veículos e frutas)
- Aplicação das métricas a embeddings reais dos mesmos termos, com redução de dimensionalidade via **PCA** e visualização em gráfico **3D**
- Exercício desenvolvido originalmente no Google Colab e posteriormente migrado para o VS Code

### Tecnologias

- Python
- OpenRouter API (embeddings)
- NumPy
- scikit-learn (PCA)
- Matplotlib
- Google Colab
- python-dotenv

---

## 🚀 Objetivos da Residência

Ao longo do programa serão explorados temas como:

- Engenharia de Prompt
- Large Language Models (LLMs)
- Retrieval-Augmented Generation (RAG)
- Agentes de IA
- LangChain
- LangGraph
- Bancos Vetoriais
- Embeddings
- APIs de IA
- Boas práticas de desenvolvimento com IA Generativa

---

## 📌 Status

🟢 Em andamento
Novos conteúdos serão adicionados conforme o avanço da residência.

---

## 📄 Licença

Este projeto possui finalidade exclusivamente educacional.
