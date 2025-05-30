# ☁️ Configurare Claude Desktop con MCP – Weather Server

---

## 🎯 Obiettivo

- Collegare un **MCP server locale** (Weather MCP) al client **Claude Desktop**
- Verificare il comportamento di Claude con/senza MCP
- Capire come funziona il sistema di configurazione tramite `claude-desktop-config.json`

---

## 🛠️ Configurazione del MCP in Claude Desktop

### 1. Apri le impostazioni di Claude:
- Vai su `Settings > Developer`
- Vedrai la sezione **MCP Servers**
- Se vuota, vuol dire che non è ancora stato configurato nulla

---

### 2. Modifica il file di configurazione

- Fai clic su **Edit Config**
- Apri il file `claude-desktop-config.json` (cartella `.claude`)
- Cerca la chiave `"mcpServers": []`
- Sostituiscila con il seguente JSON:

````json
{
  "mcpServers": {
    "waether": {
        "command": "node",
        "args": [
            "C:\\Users\\felip\\Desktop\\import-pc\\MCP\\mcp-servers\\quickstart-resources\\weather-server-typescript\\build\\index.js"
        ]
    }
  }
}
````

📌 Sostituisci `/percorso/assoluto/...` con il path **reale** del tuo file `index.js` compilato.

---

### 3. Riavvia Claude Desktop

- Chiudi Cloud Desktop
- Riaprilo

Se la configurazione è corretta:
- Comparirà un'**icona a forma di martello**
- Verranno mostrati i tools disponibili: `get_forecast` e `get_alerts`

---

## 🔁 Test: Verifica della Funzionalità

### ✅ Con MCP attivo:

Prompt:
> "What is the weather in San Francisco right now"

- Cloud ti chiederà se **autorizzi l’esecuzione** dello strumento MCP
- Se autorizzato:
  - Invoca `get_forecast(lat, lon)`
  - Invoca opzionalmente anche `get_alerts(region)`
- Mostra il meteo e gli eventuali avvisi

### ❌ Senza MCP (dopo averlo rimosso):

1. Elimina la configurazione da `claude-desktop-config.json`
2. Riavvia Claude Desktop
3. Riprova il prompt:
   - Otterrai una risposta generica, **senza accesso a dati in tempo reale**

---

## 🧪 Conclusione

✅ Hai imparato a:
- Integrare un MCP server in Claude
- Utilizzare tool MCP come `get_forecast`
- Gestire il file di configurazione `claude-desktop-config.json`
- Capire l’effetto di un MCP server attivo vs. non configurato

---

## 🔐 Sicurezza

Anche in Claude Desktop, un MCP server locale è codice remoto che gira sulla tua macchina.  
Verifica sempre le fonti prima di configurare MCP da repository esterni.

---
