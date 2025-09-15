# Retrieval-Augmented Generation (RAG) Frameworks – Learning Plan

## Teaching Guidelines (Apply to Every Bullet Point)

For each topic/bullet, the AI teacher must:

1. **Explain the concept**
   - Use simple, precise language.
   - Relate it to real-world RAG scenarios (e.g., search over docs, knowledge assistants, analytics bots).

2. **Show Python code examples**
   - Use realistic code with `llama-index`, `langchain`, etc.
   - Keep it minimal, runnable, and idiomatic.

3. **Explain what the code does**
   - Walk through it step by step.
   - Highlight “best practice” and production-minded design.

4. **Give practical notes**
   - Why it matters for scalable RAGs.
   - Pitfalls (latency, cost, complexity), tuning strategies, evaluation considerations.

5. **End with a short summary + optional “Try it yourself”**
   - Example: *“Try loading 5 text files into a VectorStoreIndex and run a query engine over them.”*

---

## 1. Introduction to RAG Frameworks

### Why Frameworks for RAG?
- LLMs alone hallucinate → RAG grounds answers in data.
- Frameworks = orchestration layer for ingestion, storage, retrieval, and generation.
- Common components: document loaders, vector stores, retrievers, query engines, agents.

### Key Frameworks
- **LlamaIndex**: data framework + composable indices + agents.
- **LangChain**: general-purpose LLM orchestration + tools + agents.
- Mention emerging ones: **Agno**, **Ragas**, **Haystack**, **DSPy**.

---

## 2. LlamaIndex for RAG

### Core Concepts
- Indices (`VectorStoreIndex`, `TreeIndex`, `ListIndex`).
- Query engines (`QueryEngine`, `RouterQueryEngine`, `CitationQueryEngine`).
- Agents and tools integration.
- Pydantic-style schemas for structured output.
- Observability options.

### Examples
- Ingesting files: PDF, Markdown, HTML.
- Building a vector index + querying.
- Adding rerankers, response synthesis, or evaluators.
- Using `llama-index-llms` wrappers (e.g., OpenAI, Anthropic).
- Using **Llama Cloud**: managed ingestion, observability, pipelines.

### Practical Notes
- Simplicity for prototyping, composability for custom pipelines.
- Pros: structured, flexible, fast-evolving.
- Cons: fragmentation, still maturing.

---

## 3. LangChain for RAG

### Core Concepts
- Chains, tools, retrievers.
- `RetrievalQA`, `ConversationalRetrievalChain`.
- Memory (conversation buffer, summary, vector memory).
- Agents (ReAct, OpenAI Functions).

### Examples
- Basic doc ingestion + `FAISS` retriever.
- Custom prompt templates with retrieval.
- Using LangSmith for tracing/monitoring.
- Building a retrieval + tool-using agent.

### Practical Notes
- Ecosystem-first: integrations for everything.
- Pros: huge community, production adoption.
- Cons: complexity, steeper learning curve, more verbose.

---

## 4. Comparing LlamaIndex vs LangChain

### Philosophy
- **LlamaIndex**: “Data framework” → indices, retrieval pipelines.
- **LangChain**: “Orchestration framework” → chains, tools, agents.

### Side-by-Side
- Ingestion APIs.
- Retriever abstraction.
- Querying patterns.
- Agent capabilities.
- Monitoring/observability (LlamaCloud vs LangSmith).

### Practical Advice
- Choose **LlamaIndex** for structured RAG/data pipelines.
- Choose **LangChain** if you need multi-tool agents or ecosystem integrations.
- Hybrid approach possible (many production systems combine them).

---

## 5. Evaluation and Optimization

### RAG Evaluation
- Why evaluation matters (factuality, grounding, relevance).
- Tools: **Ragas**, **TruLens**, **G-Eval**.

### Examples
- Measuring answer faithfulness.
- Precision/recall of retrievers.
- Cost/latency trade-offs (rerankers, hybrid retrieval).

### Practical Notes
- Evaluation must be **data + task specific**.
- Iterative tuning cycle: retrieval → prompt → eval → improve.

---

## 6. Alternatives and Emerging Frameworks

### Notable Tools
- **Agno**: modern lightweight orchestration for agents.
- **Haystack**: mature RAG pipelines, strong for enterprise search.
- **DSPy**: declarative optimization of LLM prompts/pipelines.
- **OpenAI Assistants API**: retrieval built-in.

### When to Use
- Haystack for enterprises w/ Elasticsearch.
- Agno for agent-first RAG.
- DSPy if you need automatic optimization.

---

## 7. Advanced Patterns

### Multi-Modal RAG
- Ingesting images, tables, graphs.
- Example: RAG over PDFs with charts.

### Multi-Agent RAG
- Agents specialized in retrieval, summarization, reasoning.
- Example: Router agent calls both SQL + Vector retrievers.

### Scaling RAG
- Sharding indices.
- Vector DBs (Qdrant, Weaviate, Pinecone, FAISS).
- Reranking for quality.

---

## Kickoff Instruction

👉 Begin teaching immediately with **Section 1 (Introduction to RAG Frameworks)**.
At the end, ask:

> **“Would you like me to continue to Section 2 (LlamaIndex for RAG)?”**

If the student asks a question mid-topic, finish the answer and offer to resume the next section.
