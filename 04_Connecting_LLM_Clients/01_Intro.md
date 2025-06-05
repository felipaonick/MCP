# 🧠 **Contesto storico e confronto MCP vs LangChain**

## 🎯 Obiettivo della sezione

In questa parte del corso:

1. 📜 Ripercorrere la *storia pre-MCP* nel mondo delle applicazioni AI
2. 🧠 Chiarire i concetti di **agentic behavior**, tool calling e tool invocation
3. ⚖️ Confrontare **MCP** con **LangChain**
4. 🤝 Mostrare come **MCP + LangChain** possano essere integrati sinergicamente
5. 🧩 Introdurre il pacchetto **LangChain MCP Adapters**, una bridge library open-source

---

## 🔍 1. Il mondo *prima* di MCP

Prima dell’adozione di protocolli come MCP:

* Gli agenti AI erano **implementati ad-hoc**
* Ogni sistema di tool calling aveva una **struttura proprietaria**
* Non esisteva un protocollo standard per:

  * Invocare tool dinamicamente 🛠️
  * Scambiare metadata tra client e server 📡
  * Isolare le risorse o i moduli agentici 🧩

📌 Risultato: una grande **frammentazione** e molto **codice ripetitivo o non riusabile**.

---

## 🤖 2. Agentic Behavior & Tool Invocation: come funziona sotto il cofano

### ✳️ Cos'è *Agentic behavior*?

* Comportamento in cui un LLM può **decidere e agire autonomamente**, invocando strumenti per completare un compito.

### 🔁 Come funziona la *tool invocation*?

1. LLM riceve un prompt utente
2. Ragiona sul compito (es. Planning)
3. Decide di invocare uno o più **tool**
4. Riceve la risposta dal tool e **continua il ragionamento**
5. Ritorna la risposta finale all’utente

### 📦 Con MCP:

* Tutto questo è **formalizzato** in un protocollo coerente
* I tool sono entità **standardizzate** con:

  * input/output descritti
  * metadata e descrizioni
  * gestiti come **resource** o **funzioni RPC**

---

## ⚖️ 3. MCP vs LangChain: *similitudini e differenze*

| Caratteristica         | MCP                                | LangChain               |
| ---------------------- | ---------------------------------- | ----------------------- |
| 🧠 Architettura        | Protocollo                         | Framework               |
| 🛠️ Tool Calling       | Standardizzato                     | Custom pipeline         |
| 🌐 Client/Server       | Sì (JSON-RPC 2.0)                  | No (local chaining)     |
| 🤝 Tool Reusability    | Alta                               | Variabile               |
| 🧩 Componenti modulari | Tool, Resources, Prompt            | Agents, Chains, Tools   |
| 🔁 Invocazione esterna | Sì (via CLI / Docker / MPC client) | No (interno a processo) |

💡 **Punto chiave**:

> MCP è un **protocollo interoperabile**
> LangChain è un **framework componibile**

---

## 🤝 4. MCP + LangChain: *meglio insieme*

> MCP non è alternativo a LangChain, è **complementare** ✅

Puoi usare:

* 🧠 LangChain per orchestrare agenti, chains e memory
* 📡 MCP per gestire **comunicazione standardizzata** tra tool agentici, container, server remoti

---

## 🧩 5. LangChain MCP Adapters

🆕 Introduce il pacchetto:

```plaintext
langchain-mcp-adapters
```

### 📌 Cos’è?

* Una **libreria open source** che permette a LangChain di:

  * **Invocare MCP tools** come se fossero tool LangChain
  * **Incorporare MCP resources** come contesto in chains
  * **Collegare agenti LangChain** a server MCP tramite bridge

### ✨ Vantaggi:

* Sfrutta tutta la **modularità di LangChain**
* Usa la **standardizzazione di MCP**
* Facilita lo sviluppo di **agenti distribuiti**, anche via Docker o remoto

---

## 🔜 Prossimi step (anticipazione)

Nella prossima parte del corso vedremo:

* Come installare e configurare `langchain-mcp-adapters`
* Come creare un **LangChain agent** che usa tool MCP
* Come creare flussi **ibridi** tra agenti LangChain e tool esposti via MCP

---

## ✅ Conclusione

> **“MCP risolve il problema dell’interoperabilità. LangChain organizza la logica agentica. Insieme, rendono lo sviluppo AI più scalabile, modulare e robusto.”** 🚀

---
