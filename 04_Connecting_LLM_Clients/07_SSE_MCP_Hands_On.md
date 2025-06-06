# 📦 Creazione dei primi MCP Server: Math e Weather

## 🧭 Obiettivo della Lezione

Prima di scrivere i client MCP, è necessario creare due server MCP basilari:

1. 🔢 **`math_server.py`** – Server che espone due strumenti matematici, comunica tramite **Stdio**.
2. 🌤 **`weather_server.py`** – Server che restituisce una risposta statica sul meteo, comunica tramite **SSE (Server-Sent Events)** su HTTP.

---

## 🧱 Setup Iniziale: Creazione del Package `servers/`

### 📁 Passaggi:

1. Creare una nuova cartella: `servers/`
2. Aggiungere un file vuoto `__init__.py` per renderla un package Python

---

## 🧮 `math_server.py`: Server matematico via Stdio

### ✨ Funzionalità:

* Espone **due tool**:

  * `add_numbers` – somma due numeri
  * `multiply_numbers` – moltiplica due numeri
* Usa **trasporto via `stdio`**, quindi comunica attraverso stdin/stdout
* Deriva dal codice sorgente del repository `langchain-mcp-adapters`

### ⚠️ Nota importante:

* Evitare di chiamare il file `math.py` perché **entra in conflitto** con il modulo built-in `math` di Python → usa `math_server.py` invece.

### ▶️ Comando per lanciare il server:

```bash
uv run servers/math_server.py
```

* Un quadrato lampeggiante nel terminale indica che il server è in esecuzione.

---

## 🌡️ `weather_server.py`: Server meteo via SSE (HTTP)

### ✨ Funzionalità:

* Espone **un solo tool**:

  * `get_weather` – restituisce sempre la stringa `"It’s hot as hell"`
* Usa **trasporto via SSE** (Server-Sent Events) su HTTP questo significa che la comunicazione tra il Client ed il Server sarà via HTTP. Il Client fa una richiesta HTTP POST al Server. Non dobbiamo gestisre la comunicazione am avviene sotto il cofano quando utilizziamo MCP SDK. Dobbiamo solo specificare al Server che vogliamo che il trasporto sia SSE.
* Simula una risposta semplice da un server remoto (utile per test)

### 🔌 Differenze tecniche:

| Feature       | `math_server.py`                  | `weather_server.py`             |
| ------------- | --------------------------------- | ------------------------------- |
| Transport     | `stdio`                           | `sse` (HTTP POST → eventi push) |
| Tool          | `add_numbers`, `multiply_numbers` | `get_weather`                   |
| Comunicazione | Terminale (stdin/stdout)          | Web server su `localhost:8000`  |

### 🔧 Cambio porta

È possibile modificare la porta di ascolto passando l’argomento nel server MCP SDK.

### ▶️ Comando per esecuzione:

```bash
uv run servers/weather_server.py
```

* Output atteso:

  ```
  Running on http://127.0.0.1:8000
  ```

---

## 🧰 Dettagli su MCP SDK

* Non serve implementare manualmente il protocollo HTTP o la comunicazione.
* MCP SDK gestisce tutto automaticamente in base al parametro `transport`.
* Per `weather_server`, basta specificare:

  ```python
  transport="sse"
  ```

---

## 🧾 Commit e Push su GitHub

### 📌 Passaggi finali:

1. Aggiunta dei file alla directory `servers/`:

   ```bash
   git add servers/
   ```

2. Commit automatico generato con **Cursor AI**:

   * Utilizzo dell'opzione `Generate commit message`

3. Push al branch attivo:

   ```bash
   git push
   ```

### ✅ Stato del repository dopo il push:

* Branch attivo: `project/langchain_mcp_adapters`
* Due commit visibili:

  * Il primo contiene il boilerplate iniziale
  * Il secondo contiene `math_server.py` e `weather_server.py`
* Struttura del repository aggiornata:

  ```
  ├── servers/
  │   ├── __init__.py
  │   ├── math_server.py
  │   └── weather_server.py
  ```

---

## ✅ Conclusione

In questo modulo abbiamo:

* Creato due MCP server basilari con diversi metodi di trasporto
* Compreso la differenza tra `stdio` e `sse`
* Appreso come usare il MCP SDK per semplificare lo sviluppo
* Preparato il terreno per lo sviluppo dei **client MCP**, che interagiranno con questi server

🟢 **Prossimo step:** scrivere i client MCP per connettersi ai server creati!

---