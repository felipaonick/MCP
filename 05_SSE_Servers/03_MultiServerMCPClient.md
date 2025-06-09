# 🧠 Appunti dettagliati – Connessione Multi-MCP Client e deploy su branch

## 🧩 Obiettivo

Creare un **LangChain Multi-MCP Client** che si collega a **due server MCP**:

* ➗ uno **locale** via `stdio` (math server)
* ☁️ uno **remoto** via `ssc` (weather server)

---

## 🛠️ 1. Costruzione del client multi-server

👨‍💻 Dentro il file `langchain_client.py`, viene creata una struttura asincrona con:

```python
async def main():
    async with MultiServerMCPClient(...) as client:
    ...
```

🔧 Viene passata un **dizionario di configurazione** contenente i server MCP da usare.

### 📐 Math Server – Stdio


```python
"math": {
    "command": "python",
    "args": ["<path-assoluto>/servers/math_server.py"]
}
```

🧠 Questo è il classico server eseguito localmente tramite stdio.

### 🌤️ Weather Server – SSE

```python
"weather": {
    "url": "http://localhost:8000/sse",
    "transport": "sse"
}
```

📌 Qui si usa la **comunicazione SSE** per parlare con un server esposto via HTTP (porta 8000).
Questo pattern è simile a quello visto in **Cursor** o **Claude Desktop**, dove si usano file JSON per definire l'integrazione MCP.

---

## 🤖 2. Creazione del React Agent

Il React Agent viene creato come segue:

```python
agent = create_react_agent(model=llm, tools=client.get_tools())
```

📬 Quindi il client:

* Scopre i tool disponibili (`get_tools`)
* Li passa all'agente LangChain
* Gli permette di **invocare strumenti** remoti in modo trasparente

---

## 💬 3. Prompting e invocazione

📤 **Messaggio di test:**

```python
result = await agent.ainvoke({"messages": [{"role": "user", "content": "What is 2 + 2?"}]})
```

✅ Risultato corretto restituito.

📤 **Secondo messaggio:**

```python
result = await agent.ainvoke({"messages": [{"role": "user", "content": "What is the weather in San Francisco?"}]})
```

☀️ Output (dal server SSE): `"Hot as hell"`
📈 Viene mostrato **il log del server**, con:

* Lista dei tools (`POST /list-tools`)
* Invocazione (`POST /call-tool`)
* Nuova **sessione generata** dal client

---

## 🪵 4. Logging interno al server

🛠️ Viene aggiunto un `print()` nel file `weather_server.py` per loggare le richieste:

```python
print("This is a log from the SSE server")
```

🚀 Dopo aver **riavviato il server**, si può vedere il log lato console ogni volta che arriva una chiamata.

🧩 Questa funzionalità è utile per:

* Debug 🐞
* Monitoraggio 🖥️
* Logging strutturato 📝
* Deploy in produzione con tracciabilità 🔐

---

## 🗂️ 5. Git: nuovo branch e push

📁 Viene creato un nuovo branch Git per il progetto:

```bash
git checkout --orphan project/se
git add .
git commit -m "Initial commit for Multi-MCP Client with stdio and ssc servers"
git push origin project/se
```

📌 Tutto il codice aggiornato è disponibile in questo nuovo branch.

---

## ✅ Riepilogo finale

| Elemento                  | Descrizione                                |
| ------------------------- | ------------------------------------------ |
| 🔗 `MultiServerMCPClient` | Connessione contemporanea a più MCP server |
| 🧠 React Agent            | Composizione automatica LLM + tools remoti |
| 🧮 Math Server (stdio)    | Server locale con comando Python           |
| ☁️ Weather Server (ssc)   | Server HTTP su porta 8000                  |
| 📤 Prompt test            | Eseguite domande su calcoli e meteo        |
| 🪵 Logging                | Debug visibile nel terminale del server    |
| 🔀 Git branch             | Codice salvato su `project/se`             |

---

💡 **Prossimi step suggeriti:**

1. Aggiungere gestione degli errori e fallback nei tool.
2. Implementare autenticazione/autorizzazione per i server SSC.
3. Deploy in cloud di uno o più server MCP per test su rete pubblica.
4. Monitoraggio avanzato con `logging` Python + sistemi come Logtail o Prometheus.

---
