# ☁️ Esecuzione e Verifica MCP in Cursor – Weather Server

## 🎯 Obiettivo

Verificare che Cursor possa:
- Riconoscere un server MCP locale
- Comunicare correttamente con esso
- Eseguire i tool `get_forecast` e `get_alerts` in modo automatico

---

## 🔄 Comportamento SENZA MCP

- Prompt: _"What is the weather in San Francisco right now?"_
- Risultato: Cursor **non è in grado di rispondere** (nessun accesso a fonti in tempo reale)

---

## 🧰 Aggiunta del MCP Server

1. Vai su `Cursor > Settings > MCP`
2. Crea o modifica il file: `~/.cursor/mcp.json` in windows `C:\Users\felip\.cursor\mcp.json`
    - Tale file conterrà la configurazione che i Cursor Clients useranno per comunicare con MCP server.
    - Qui diremo a Cursor come eseguire i MCP servers, se essi saranno da eseguire localmente, come nel nostro esempio, e se utilzzano la comunicazione Stdio (standard input e output) oppure SSE (server side events).

3. Se andiamo nella documentazione ufficiale di MCP (https://modelcontextprotocol.io/quickstart/server) nella parte **Testing your server with Claude for Desktop** vediamo un payload molto simile, un JSON nested:
```json
{
    "mcpServers": {
        "weather": {
            "command": "node",
            "args": [
                "C:\\PATH\\TO\\PARENT\\FOLDER\\weather\\build\\index.js"
            ]
        }
    }
}
```

Questo esempio notiamo che c'è la chiave **weather** che ha come valore un dizionario con **command**, il quale esegue l'MCP server, e la chiave **arguments** gli argomenti per il comando.

Nel nostro caso eseguiamo il comando **node** con il file compilato **index.js** nella build directory. 

4. Inserisci la configurazione seguente nel nostro mcp.json:

````json
{
    "mcpServers": {
        "weather": {
            "command": "node",
            "args": [
                "C:\\Users\\felip\\\\Desktop\\da importare sul tuo pc\\MCP\\mcp-servers\\quickstart-resources\\weather-server-typescript\\build\\index.js"
            ]
        }
    }
}
````

📌 Assicurati che:
- Il percorso al file `index.js` sia **corretto**
- Il server sia già stato **compilato** con `npm run build`

---

## ✅ Verifica della Connessione

Una volta inserita la configurazione:
- Cursor segnalerà che il server è **valido**
- Mostrerà i tool MCP registrati:
  - `get_forecast`
  - `get_alerts`

Se appare l'errore `client closed`, la causa è **percorso errato**.

---

## 🚀 Test di Esecuzione

1. Apri un agent Cursor
2. Prompt: _"What is the weather in San Francisco right now?"_
3. Osserva:
   - Cursor **deduce latitudine e longitudine**
   - Chiama `get_forecast(lat, lon)`
   - Successivamente chiama anche `get_alerts(region)`

📥 Il risultato mostra:
- La **previsione meteo**
- Eventuali **allerta attive** nella regione

---

## 🔄 Riepilogo Azioni

✅ Abbiamo:
- Clonato e compilato un MCP server (weather)
- Creato il file `mcp.json` con percorso corretto
- Collegato Cursor a tale server
- Verificato l’esecuzione automatica dei tool da parte dell’agente

---

## 🔐 Sicurezza

Ricorda: anche in fase di test, un MCP server è **esecuzione di codice remoto**.  
Verifica sempre la provenienza e il contenuto prima dell’uso in ambienti reali.

