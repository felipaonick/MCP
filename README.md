# 🧠 Model Context Protocol (MCP) — Appunti e Sperimentazioni

Questo repository raccoglie appunti, esempi di codice, configurazioni e sperimentazioni realizzate durante il corso [MCP Crash Course: Complete Model Context Protocol in a Day](https://www.udemy.com/course/model-context-protocol/) tenuto da Eden Marco.

## 📚 Contenuti del Corso

Il corso si concentra su:

- **Teoria del MCP**: Introduzione al protocollo e alla sua architettura.
- **Componenti principali**:
  - **MCP Hosts**: Applicazioni come Claude Desktop, Cursor, Windsurf.
  - **MCP Clients**: Client che mantengono connessioni 1:1 con i server MCP.
  - **MCP Servers**: Programmi leggeri che espongono capacità specifiche tramite MCP.
  - **Fonti di dati locali**: File, database e servizi locali accessibili dai server MCP.
  - **Servizi remoti**: Sistemi esterni disponibili via internet (es. tramite API) connessi ai server MCP.
- **Capacità chiave**:
  - **Resources**: Componenti che espongono dati e contenuti dai server agli LLM.
  - **Prompts**: Creazione di template di prompt riutilizzabili e workflow.
  - **Tools**: Funzionalità che permettono agli LLM di eseguire azioni tramite il server.
  - **Sampling**: Capacità dei server di richiedere completamenti agli LLM.
  - **Transports**: Meccanismo di comunicazione tra client e server MCP.
- **Argomenti trattati**:
  - Best practices per la sicurezza degli agenti MCP.
  - Containerizzazione dei server MCP.
  - Flusso del protocollo MCP.
  - Integrazione di MCP con Docker e LangChain.
  - Implementazione di OAuth 2.0 con MCP utilizzando Auth0.
  - Deployment di MCP su Cloudflare.
  - Protocollo Agent-to-Agent (A2A) in fase di sviluppo.:contentReference[oaicite:40]{index=40}

## 🗂 Struttura del Repository

- `notes/`: :contentReference[oaicite:42]{index=42}
- `examples/`: :contentReference[oaicite:45]{index=45}
- `docker/`: :contentReference[oaicite:48]{index=48}
- `auth/`: :contentReference[oaicite:51]{index=51}
- `langchain/`: :contentReference[oaicite:54]{index=54}
- `deployment/`: :contentReference[oaicite:57]{index=57}
- `a2a/`: :contentReference[oaicite:60]{index=60}:contentReference[oaicite:62]{index=62}

## 🛠 Prerequisiti

Per seguire e replicare gli esempi presenti in questo repository, è necessario avere:

- :contentReference[oaicite:64]{index=64}
- :contentReference[oaicite:67]{index=67}
- :contentReference[oaicite:70]{index=70}
- :contentReference[oaicite:73]{index=73}
- :contentReference[oaicite:76]{index=76}
- :contentReference[oaicite:79]{index=79}:contentReference[oaicite:81]{index=81}

## 👤 Note Personali

Questo repository è una raccolta personale di materiali studiati e sperimentazioni effettuate durante il corso. Non rappresenta materiale ufficiale del corso né è destinato alla distribuzione.

