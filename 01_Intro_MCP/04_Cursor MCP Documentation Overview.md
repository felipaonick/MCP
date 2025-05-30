# 🧪 Configurare Cursor con un MCP Server – Standard Input/Output Transport

---

## 🎯 Obiettivo

Configurare il client **Cursor** per usare il nostro MCP server (es. il Weather MCP Server) utilizzando il **trasporto standard input/output**.

---

## 📚 Contesto

- MCP sta diventando uno **standard**.
- Cursor supporta **diversi trasporti** MCP:
  1. **Standard Input/Output (stdin/stdout)** – quello usato in questo esempio
    - In sostanza il server MCP è in esecuzione sulla nostra macchina locale.
    - Scriverà gli interi input ed output nello standard input e output. 
    - Il client che è hostato su Cursor leggerà tutto dal server.
    - Per tale motivo dobbiamo dire a Cursor come eseguire il server MCP localmente, questo sarà un shell command su come eseguire il nostro server localmente.
  2. **Server-Side Events (SSE)** – sarà trattato più avanti

---

## ⚙️ Come si configura?

Abbiamo già clonato e compilato il nostro NodeJS Server. 

Ora vediamo come fare la stessa cosa ma con il Python Server.

Il concetto è identico sia per NodeJS che per Python dato che nella configurazione (file .json) diciamo semplicemente a Cursor come eseguire il nostro MCP server.

Vediamo che c'è un file 'payload.json' con una lista di servers, dobbiamo dare al server un nome (server-name) in cui si scrive il comando per runnare/eseguire il server (nel nostro esempio il comando è "npx"). Dobbiamo inoltre fornire il 'path' del nostro server compilato, nel nostro caso dobbiamo dare il path del nostro file 'index.js' che abbiamo già compilato. Se abbiamo delle variabili di ambiente come API Keys ecc. dobbiamo metterle nel chiave "env".

---

## 📂 Dove si configura?

Cursor permette due tipi di configurazione MCP:

| Tipo            | Percorso                                     | Valido per        |
|-----------------|----------------------------------------------|-------------------|
| **Globale**     | `~/.cursor/mcp.json` nella home directory                         | Tutti i progetti: Ogni volta che apriamo Cursor avremo la configurazione dei server MCP funzionante. Questo rende i server MCP disponibile in tutto il nostro Cursor workspace |
| **Per progetto**| `.cursor/mcp.json` nella root del progetto   | Solo quel progetto: consente di definire MCP servers che sono solamente disponibili per questo specifico progetto. |

---

## 🧾 Esempio di configurazione `mcp.json`

```json
// This example demonstrated an MCP server using the stdio format
// Cursor automatically runs this process for you
// This uses a Node.js server, ran with `npx`
{
  "mcpServers": {
    "server-name": {
      "command": "npx",
      "args": ["-y", "mcp-server"],
      "env": {
        "API_KEY": "value"
      }
    }
  }
}
```

- `name`: nome leggibile per il server
- `command`: come eseguire il server MCP (Node o Python)
- `env`: variabili ambiente opzionali (es. chiavi API, variabili d'ambiente)

---

## 🧠 Funzionamento

Una volta che abbiamo configurato un MCP server che espone i tools (nel nostro esempio è il weather tool) all'Agente Cursor, allora l'agente Cursor sarà in grado di eseguire tale tool se lo reputa rilevante.

Un MCP server che scarichiamo ed eseguiamo localmente è RCE che è una vulnerabilità di Remote Code Execution dato che è un codice che non abbiamo scritto noi e che è in esecuzione sulla nostra macchina.

Dunque in caso avessimo degli attori malitenzionati che avvelenano un MCP Server potrebbero causare dei problemi.

La scelta progettuale che ha fatto Cursor riguardo al tool approval è:

- Cursor di default non va ad eseguire il tool quando lo reputa appropriato ma ci da' un prompt con un messaggio "se vogliamo approvare la chiamata al tool o meno".
- In suddetto messaggio possiamo anche vedere quale tool viene chiamato e con quali argomenti. Questo è importante per quanto riguarda la sicurezza.

Ricapitolando:
- Cursor **lancia il comando specificato**
- Legge e scrive attraverso lo **stdin/stdout**
- Gli strumenti MCP esposti (es. `get_forecast`, `get_alerts`) vengono **registrati nel sistema**
- Quando l’agente lo ritiene utile, può decidere di usare il tool (con approvazione dell’utente)

---

## 🔐 Sicurezza: Prompt di approvazione

- Di default, Cursor **chiede approvazione** ogni volta che un tool MCP viene chiamato
- Mostra:
  - Il nome dello strumento (tool)
  - Gli argomenti passati
- Questo protegge da **Remote Code Execution (RCE)** tramite server MCP malevoli

---

## 😎 Modalità YOLO

> Solo per sviluppatori "vibe coder" 

- Disattiva il prompt di approvazione
- Cursor **esegue automaticamente** tutti i tool MCP
- 🔥 Utile in ambienti di test / personale
- 🚫 **Sconsigliato in contesti aziendali o di produzione**

---

## 🧪 Riepilogo

✅ Hai configurato Cursor per:
- Usare il tuo MCP server via stdin/stdout
- Eseguire tool registrati
- Personalizzare il comportamento (approvazione vs YOLO mode)


## Fonti:

[Configuring MCP servers](https://docs.cursor.com/context/model-context-protocol)