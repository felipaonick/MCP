# Introduzione al MCP Server con LLM.txt 🌍

## Cos'è il MCP Server? 🖥️

Il **MCP server** è una componente fondamentale che **espone strumenti, risorse e funzionalità** tramite il protocollo **MCP**. In questo caso, il server è utilizzato per fornire accesso dinamico alla **documentazione ufficiale** di pacchetti, come **LangChain** o altri framework, tramite il file **LLM.txt**.

### Obiettivo Principale 🔍

Il server sfrutta **LLM.txt** per accedere alla documentazione pubblica e aggiornata di pacchetti open source, come **LangChain**:

* **Documentazione aggiornata**: Le documentazioni di pacchetti come **LangChain** cambiano frequentemente, e **LLM.txt** aiuta a mantenere sempre il sistema aggiornato, evitando che i dati diventino obsoleti.

---

## Funzionamento del MCP Server con LLM.txt 🚀

### 1. **Accesso a LLM.txt** 📂

* **LLM.txt** contiene una lista di **URL** e descrizioni brevi dei contenuti che questi URL rappresentano.
* Analogamente a un **indice di libro**, **LLM.txt** fornisce un sommario dei contenuti del sito web, permettendo all'AI di decidere quale URL visitare in base alla richiesta dell'utente.

### 2. **Fase di Recupero** 🧑‍💻

* Una volta che il server ha l'elenco dei **URL** da **LLM.txt**, il server MCP può fare una richiesta **curl** per **scaricare** dinamicamente la documentazione aggiornata.

**Esempio**:

* Se un utente chiede informazioni sulla **memoria di LangChain**, il server scarica il contenuto del file **LLM.txt**, estrae l'**URL rilevante** e recupera la documentazione specifica.

---

## Come Funziona il Server MCP 🔄

### 1. **Clonazione del Repository e Installazione** ⚙️

Per avviare il server MCP, bisogna:

1. **Clonare il repository GitHub** [repository mcpdoc](https://github.com/langchain-ai/mcpdoc).
2. **Installare le dipendenze** usando **UV** (un framework Python) e configurare l'ambiente.

### 2. **Avvio del Server Localmente** 💻

```bash
uvx --from mcpdoc mcpdoc \
    --urls "LangGraph:https://langchain-ai.github.io/langgraph/llms.txt" "LangChain:https://python.langchain.com/llms.txt" \
    --transport sse \
    --port 8082 \
    --host localhost
```

Una volta che il server è configurato:

* Viene eseguito sulla **porta 8082**.
* Utilizza **LLM.txt** per determinare dinamicamente quale documentazione scaricare in base alla richiesta dell'utente.

---

## Debugging con MCP Inspector 🛠️

### 1. **Connessione al Server con MCP Inspector** 🌐

```bash
npx @modelcontextprotocol/inspector
```

Ora vogliamo collegarci al **mcpdoc** che è un SSE Server in esecuzione sulla porta 8082.

MCP Inspector è un tool che permette di **debuggare** e **testare** il server MCP, visualizzando gli strumenti esposti:

* Il **pannello "List Tools"** mostra gli strumenti disponibili nel server, come **"list_doc_sources"** e **"fetch_docs"**.
* **Strumento "Fetch Docs"**: Recupera i dati dinamicamente dai **URL** estratti da LM.txt.

### 2. **Test degli Strumenti** 🔍

MCP Inspector consente di:

* **Visualizzare i tool** esposti dal server.
* **Testare gli strumenti** con **input dinamici**, permettendo di **scrapare** il contenuto direttamente da LM.txt.


---

## Integrazione con Cloud Desktop 🌥️

### 1. **Integrazione del Server MCP** 🔗

Dopo aver configurato correttamente il server MCP (file `claude_desktop_config.json`) Tale file dice al client come runnare l'MCP Server:

```json
{
  "mcpServers": {
    "langgraph-docs-mcp": {
      "command": "uvx",
      "args": [
        "--from",
        "C:/Users/felip/Desktop/import-pc/MCP/02_MCP_Servers/mcpdoc",
        "mcpdoc",
        "--urls",
        "LangGraph:https://langchain-ai.github.io/langgraph/llms.txt",
        "--transport",
        "stdio",
        "--port",
        "8081",
        "--host",
        "localhost"
      ]
    }
  }
}
```

* Si integra con **Claude Desktop** per migliorare le risposte dell'AI utilizzando documentazione aggiornata in tempo reale.
* Senza l'integrazione, l'AI risponde solo con **dati statici** o **addestrati**, che potrebbero diventare obsoleti molto rapidamente.

### 2. **Funzionamento della Risposta** 💬

Quando l'AI riceve una richiesta (ad esempio: "What is LangChain memory?"):

* Senza l'integrazione **MCP**, l'AI fornisce una risposta basata solo sul **training precedente**.
* Con **MCP**, l'AI può rispondere con **dati aggiornati in tempo reale** prelevati dal sito ufficiale tramite **LM.txt**.

---

## Debugging del Server MCP 🐞

### 1. **Correzione degli Errori** 🔧

Se l'integrazione non funziona correttamente, il sistema restituisce errori. Nel caso di **Cloud Desktop**, l'errore potrebbe essere legato al **comando UV**:

* È necessario **specificare il percorso completo** del comando **UV** per garantire che il server venga eseguito correttamente.

### 2. **Verifica dell'Attivazione del Tool** ✅

Una volta risolto l'errore, l'AI dovrebbe essere in grado di:

* **Attivare il tool "List Document Sources"** per ottenere l'**URL di LLM.txt**.
* **Scrapare la documentazione** da quell'URL per ottenere informazioni precise e aggiornate.

---

## Flusso Completo del Processo 🔄

1. **Richiesta dell'utente**: L'utente chiede informazioni (ad esempio, "What is LangGraph memory?").
2. **Strumento di scraping**: Il server MCP esegue il tool **"List Document Sources"** per ottenere l'**URL corretto** da LLM.txt.
3. **Recupero della documentazione**: Il server utilizza **"Fetch Docs"** per scaricare la documentazione dinamicamente.
4. **Risposta aggiornata**: L'AI fornisce una risposta basata sui **dati real-time**.

---

## Conclusione 🎯

Il **MCP server** con **LM.txt** consente di migliorare enormemente le capacità di **AI agents** come **Cloud Desktop**, **Cursor**, e **Windsurf**:

* **Documentazione aggiornata** in tempo reale.
* **Recupero dinamico** delle informazioni senza dover dipendere da dati statici.
* **Maggiore precisione** nelle risposte, grazie all'accesso a **contenuti sempre aggiornati**.

Con l'integrazione di **MCP**, gli **AI agents** possono interagire in modo molto più intelligente e preciso, migliorando le loro performance complessive. 🚀

