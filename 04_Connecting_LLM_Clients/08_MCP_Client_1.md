# 🧠 Lezione: Implementazione dell’MCP Client in `main.py`

## 🎯 Obiettivo

Configurare e avviare un **client MCP** che si connette al `math_server.py` tramite trasporto `stdio`, recupera i tool MCP esposti e li integra con **LangChain** e **LangGraph** per l’orchestrazione tramite un **ReAct Agent**.

---

## 📥 Step 1: Pulizia e Check del file `main.py`

1. ✅ Rimozione della stampa della variabile `OPENAI_API_KEY`
2. ✅ Esecuzione iniziale di sanity check:

   ```bash
   uv run main.py
   ```

---

## 🧱 Step 2: Importazione dei Moduli Necessari

### 🧩 MCP Core

```python
from mcp import ClientSession, StdioServerParameters
```

* `ClientSession`: Fornisce il framework per una applicazione Python per comportarsi come un client MCP. Dunque è il responsabile della connessione ad MCP server, per scambiare messaggi e rispondere alle richieste e notifiche del server tramite callbacks personalizzabili. Ha un metodo molto speciale chiamato `initialize()` che avvia la sessione.
* `initialize()`: avvia la comunicazione tra client e server. Invia una richiesta al server per stabilire i paramentri di connessione in base alle specifiche MCP.

* Ricordiamo che la connessione tra Client e Server MCP e di tipo 1 a 1, quindi quando inizializziamo il Client dobbiamo dirgli come leggere e scrivere i dati, quindi tramite quale canale, se è tramite StdIO o se tramite SSE.

* `StdioServerParameters`: è una classe Python che ha i campi "command" e "args" i quali specificano come runnare il server MCP. Quindi, il Client deve sapere come runnare il Server MCP, se runnarlo come un file Python o come Docker.

### 🖥️ MCP Stdio Client

* Ora che abbiamo la sessione MCP di comunicazione, dobbiamo creare Il Client MCP che prende e usa questa sessione per comunicare con il server MCP.

```python
from mcp.client.stdio import stdio_client
```

* Crea un processo figlio.
* Comunica con il server MCP tramite `stdin`/`stdout`. Quindi legge da standard in e scrive su standard out.

### 🔁 LangChain MCP Adapter

```python
from langchain_mcp_adapters import load_mcp_tools
```

* Funzione che converte i tool MCP in `Tool` LangChain-compliant.
* Il LangChain tool ha le stesse informazioni del MCP Tool, **Contenuto** identico (nome, argomenti, descrizione, ritorno), tuttavia il formato è un po diverso e anche la struttura, quindi questa funzione fa il lavoro di conversione.

### 🧠 LangGraph Agent

```python
from langgraph.prebuilt import create_react_agent
```

* Orchestratore intelligente che:

  * Interpreta i prompt.
  * Decide quale tool chiamare e quando.
  * Utilizza il pattern **ReAct (Reason + Act)**.
* Elegante integrazione LangGraph + LangChain.

---

## 🧼 Step 3: Ordinare gli import con `isort`

* Installazione:

  ```bash
  uv add isort
  ```
* Utilità:

  * Ordina alfabeticamente gli import.
  * Segue convenzione: standard lib → third-party → internal.

---

## 🤖 Step 4: Creazione del Modello LLM

```python
from langchain_openai import ChatOpenAI

llm = ChatOpenAI()
```

* Modello OpenAI default (es. `gpt-3.5-turbo` o `gpt-4`)
* Supporta `function calling`
* 🔄 Compatibile con altri LLM: Anthropic, Gemini, DeepSeek (basta supportino il function calling)

---

## 🔌 Step 5: Definizione dei Parametri del Server

### 🛠️ Costruzione dell’oggetto `stdio_server_params` per runnare il server

```python
stdio_server_params = StdioServerParameters(
    command="python", # dato che il nostro server è un file Python
    args=["C:/Users/felip/Desktop/import-pc/MCP/04_Connecting_LLM_Clients/langchain_mcp_adapters_project/servers/math_server.py"] # mettiamo il path assoluto al file del server
)
```

📌 **Nota importante:** il path deve essere assoluto, perché il client potrebbe essere lanciato da qualsiasi directory.

Per ottenere il path assoluto:

```bash
pwd o cd # per ottenere il path assoluto della cartella corrente
```

e incollarlo nel parametro `args`.

---

## 🛠️ Step 6: Fix Import e Test

⚠️ Bug:

```python
from langchain_mcp_adapters import load_mcp_tools
```

❌ Corretto:

```python
from langchain_mcp_adapters.tools import load_mcp_tools
```

✅ Dopo la correzione, rieseguire:

```bash
uv run main.py
```

Output positivo = tutto funziona correttamente ✅

---

## 📤 Step 7: Git Commit & Push

1. Aggiunta file modificati:

   ```bash
   git add .
   ```
2. Commit con messaggio autogenerato da Cursor:

   ```bash
   git commit -m "Setup MCP client connection and tool loading"
   ```
3. Push:

   ```bash
   git push
   ```

📌 Ora il commit è visibile nel repository GitHub con il diff completo.

---

## 🧠 Conclusione & Anticipazione

In questo modulo abbiamo:

✅ Creato il **client MCP**
✅ Definito i parametri per la connessione con un server `stdio`
✅ Integrato i tool MCP in LangChain
✅ Preparato l'orchestrazione con un ReAct Agent in LangGraph

🔜 **Prossimo step**: usare questi strumenti in pratica e comprendere **a fondo** le classi MCP in azione, con un'esecuzione **end-to-end** del flusso agentico.

---
