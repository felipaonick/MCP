# 🌐 MCP Demo – Come funziona in pratica il Model Context Protocol

---

## 🎯 Obiettivo della demo

Mostrare in modo pratico **cosa si ottiene usando MCP**, e **come un tool sviluppato una sola volta** può essere usato da agenti diversi (es. Claude, Cursor) **senza ulteriori integrazioni**.

---

## 🛠️ Caso d’uso: Ottenere il meteo attuale

### ✳️ Step 1 – Prima dell’MCP
- Agente AI: **Claude**
- Nessun MCP configurato
- Prompt: _"What's the weather in San Francisco?"_
- Risposta del LLM: **"Non ho accesso a dati meteo in tempo reale"**

---

### ⚙️ Step 2 – Aggiunta dell’MCP Server
- MCP Server implementa una funzione `get_forecast(lat, lon)`
- Cloud rileva le coordinate di San Francisco
- Chiama `get_forecast` sul server MCP
- Il server restituisce la previsione meteo → Claude la processa e risponde

> 🔒 Prima dell'esecuzione, l’utente è **invitato a dare il consenso** (per motivi di sicurezza)  
> (Esempio: evitare l'esecuzione di codice potenzialmente pericoloso)

---

## 🔁 Riutilizzo con altri agenti: Cursor

- Lo **stesso MCP server** (per il meteo) viene collegato a Cursor
- MCP è già abilitato in modalità **YOLO** (non chiede conferma per ogni tool eseguito)
- Prompt: _"What’s the weather in San Francisco right now?"_
- Cursor:
  - Chiama `get_forecast` sul server MCP
  - In più decide autonomamente di chiamare anche `get_alerts`
  - Compone la risposta finale con **previsione meteo + allerta attiva**

> 🧠 **Magia apparente**, ma è tutto reso possibile dalla struttura modulare di MCP

---

## 🧩 Cosa vediamo nei settings

Sia in Claude che in Cursor:
- È possibile **vedere i server MCP configurati**
- È visibile l'elenco degli strumenti disponibili (`get_forecast`, `get_alerts`)
- Viene anche mostrato il **comando per avviare il server**, che in questo caso è in Node.js

---

## ✅ Conclusioni

- Con MCP possiamo **aggiungere nuove capacità** ai nostri agenti AI **senza modificare il loro codice**.
- Basta **implementare un MCP server compatibile**.
- Una volta fatto, tutti gli agenti MCP-ready possono usarlo: **integrazione 1 volta sola**.
- Funzionalità modulari, riutilizzabili, scalabili.
- Cursor e Claude sono solo esempi: MCP è supportato anche da altri (es. WindSurf, Luvabull, ecc.).
