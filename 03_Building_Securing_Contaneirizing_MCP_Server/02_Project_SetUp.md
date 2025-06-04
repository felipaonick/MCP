# 🚀 Setup Iniziale del Progetto MCP Server

## 🧱 Obiettivo del Video

👉 Prima di iniziare a **scrivere il codice** del nostro MCP server, dobbiamo:

* Preparare il progetto 📁
* Installare le dipendenze 🔧
* Attivare Cursor ⚙️
* Indicizzare la documentazione MCP 📚
* Configurare regole personalizzate per Cursor 🧠

---

## 📦 Tool utilizzati

* 🐍 **UV**: package manager e tool per creare ambienti virtuali
* 🧠 **Cursor**: AI assistant per scrivere codice in modo smart
* 📚 **MCP Python SDK**: libreria ufficiale per creare MCP server
* 🛠️ Altri alternativi: puoi usare anche `poetry`, `pipenv`, o `virtualenv` al posto di `uv`!

---

## 🛠️ Step-by-step: Configurazione del Progetto

### 📂 1. Navigare nella cartella dei MCP Server

```bash
cd MCP-servers
```

### 🧪 2. Creazione del progetto UV

```bash
uv init shell-server
```

🔹 Crea una cartella `shell-server` con:

* `pyproject.toml` 🧾
* `main.py` (che poi verrà rimosso)
* `README.md`

### 🧪 3. Creazione e attivazione dell’ambiente virtuale

```bash
uv venv
source .venv/bin/activate  # oppure usa il comando proposto da UV
```

✅ Una volta attivato, nella shell vedrai il nome dell’ambiente virtuale attivo (`shell-server`).

---

### 📦 4. Installazione delle dipendenze

📌 Installiamo il **pacchetto ufficiale CLI del MCP**:

```bash
uv add mcp[cli] # oppure usa `pip install mcp[cli]` se preferisci pip con venv
```

👉 Questo aggiorna automaticamente il `pyproject.toml` e installa la libreria.

---

### 🧹 5. Pulizia e preparazione del file di partenza

* ✂️ Elimina `main.py` (non necessario)
* ✏️ Crea `server.py`: sarà il punto d’ingresso dell’MVP server

---

## 🧠 Cursor: Il Tuo AI Pair Programmer

Siamo nel 2025 e non dobbiamo spendere tutto il tempo a scrivere codice per creare MCP Servers da zero! 

Andremo a fare il Vibe-Coding con Cursor, il nostro AI pair programmer che ci aiuterà a scrivere codice in modo smart e veloce.

Quindi, vedimao come possiamo Applicare il Vibe-Coding con Cursor per creare il nostro MCP Server.

### 🧑‍💻 Attivazione di Cursor nella directory

1. Apri Cursor nel progetto
2. Assicurati che sia visibile tutta la struttura `shellserver`

---

## 📚 Indicizzazione della Documentazione

### 📘 1. Indicizzare la documentazione ufficiale MCP

* Vai su **Settings > Features**
* Aggiungi URL: `https://modelcontextprotocol.io`
* 📥 Cursor scaricherà e indicizzerà tutte le pagine e sottopagine
* Possiamo quindi utilizzare questa documentazione quando facciamo il Vibe-Coding con Cursor
* 🧩 Questo aiuta Cursor a capire il contesto del progetto e a suggerire codice rilevante

🪪 Nome suggerito: `MCP`

📖 Verifica cliccando sull’icona del libro: vedrai le sezioni come `server`, `client`, ecc.

---

### 🐍 2. Indicizzare l’MCP Python SDK (GitHub)

* Aggiungi il repo GitHub del Python SDK: `https://github.com/modelcontextprotocol/python-sdk`
* Include `README.md` e altre parti utili del codice
* 🪪 Nome suggerito: `MCP Python SDK`

💡 Questo aiuterà Cursor a scrivere codice con conoscenza contestuale della libreria.

```markdown
    Un **Python SDK** (Software Development Kit) è **un insieme di strumenti, librerie, esempi di codice e documentazione** che ti permette di **interagire facilmente con una piattaforma, un servizio o un protocollo direttamente da Python**.

    ---

    ## 🧩 Cosa contiene di solito un SDK Python:

    | Componente          | Descrizione                                                         |
    | ------------------- | ------------------------------------------------------------------- |
    | 📦 Librerie         | Moduli Python già pronti da importare (`import nome_sdk`)           |
    | 📘 Documentazione   | Spiegazioni su come usare le funzioni e le classi disponibili       |
    | 🧪 Esempi di codice | File `.py` che mostrano come usare l'SDK in casi reali              |
    | 🛠️ Script CLI      | A volte include comandi da terminale per facilitare setup o testing |

    ---

    ## 🧠 A cosa serve?

    Un Python SDK ti **semplifica la vita** perché ti **nasconde le complessità** tecniche (es. chiamate API, gestione delle richieste, parsing delle risposte) e ti **fornisce funzioni già pronte**.

    ### 🔧 Esempio pratico

    Se stai lavorando con il **Model Context Protocol (MCP)**, invece di fare tutto "a mano", potresti usare:

    ```python
    from mcp_sdk import MCPClient

    client = MCPClient()
    client.connect()
    ```

    Senza SDK dovresti:

    * scrivere a mano le richieste HTTP
    * costruire i payload
    * gestire gli errori delle API
    * leggere la documentazione raw del protocollo
```
---

## 🎭 Creazione di *Cursor Rules* personalizzate

Cursor ci aiuterà a scrivere il codice per la creazione del nostro MCP server, ma per farlo al meglio dobbiamo dargli delle **regole personalizzate**.

### 🧠 Obiettivo: Dare a Cursor una "persona" da **esperto Python e FastAPI**

📁 Crea directory `.cursor/rules/`

📄 Crea file: `python.mdc`

🔍 Vai su [Cursor Directory](https://cursor.directory/rules) e cerca regole come:

* "Python expert"
* "FastAPI expert"
* "Scalable API developer"

📋 Copia e incolla il contenuto nel file `.mdc`

🧷 Imposta il tipo di regola su `always` (verrà usata in ogni richiesta Cursor nel progetto)

---

## ✅ Riepilogo delle Azioni Compiute

| Azione                           | Descrizione                           |
| -------------------------------- | ------------------------------------- |
| 🛠️ Progetto creato              | `uv init shell-server`                |
| 🐍 Virtualenv attivato           | `uv venv` + activate                  |
| 📦 Dipendenze installate         | `uv add mcp[cli]`                      |
| 📁 Struttura del progetto pulita | `main.py` rimosso, `server.py` creato |
| 🧠 Cursor configurato            | Avviato su progetto                   |
| 📚 Doc indicizzata               | Sito MCP + GitHub SDK                 |
| 🎭 Persona Python                | `python.mdc` con regole custom        |

---

## 🧩 Prossimo Step

🎯 Iniziare la **scrittura dell’MCP server** con l’aiuto di Cursor... o meglio, farlo scrivere direttamente a lui! 😎

---