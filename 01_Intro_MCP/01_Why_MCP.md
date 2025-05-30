# 🧩 MCP – Model Context Protocol: Cos'è, Perché Serve e Come Funziona

---

## 🚀 Cos’è l’MCP?

L’**MCP (Model Context Protocol)** è un **protocollo standard** per permettere l’interoperabilità tra agenti AI e strumenti/servizi.  
In parole semplici, è un modo per far **comunicare agenti diversi** con strumenti esterni in maniera **modulare**, **riutilizzabile** e **senza dover riscrivere codice ogni volta**.

---

## ❓ Perché abbiamo bisogno dell’MCP?

### 🌐 Il problema senza MCP:
- Immagina di avere un **agente AI** (es. Cursor) capace di:
  - Mandare messaggi su **Slack**
  - Inviare email via **Gmail**
  - Fare query su un **database**
- Per ogni funzione dobbiamo:
  - Scrivere codice personalizzato
  - Usare API (es. Slack, Gmail)
  - Proteggere certe operazioni (es. evitare `delete` su Gmail)
- E se un'altra persona, con un'altro strumento che usa gli LLMs, volesse usare le stesse funzioni? (ad es. con WindSurf o Copilot)
  - Dovremmo **scrivere da zero** ogni integrazione manualmente
  - Ogni tool → nuova integrazione → moltiplicazione del codice da mantenere


![alt text](images/senza_mcp.png)

---

## 💡 La soluzione: aggiungere uno strato di astrazione

> “In informatica, ogni problema può essere risolto aggiungendo un layer di astrazione.”

### ✅ Entra in gioco MCP:
- Invece di scrivere integrazioni diverse per ogni tool:
  - ✅ Si crea **una sola integrazione MCP** per il nostro agente
  - ✅ Tutti gli altri strumenti compatibili con MCP possono **collegarsi automaticamente**
- Questo significa:
  - L’agente compatibile con Cursor → funziona anche con WindSurf, Luvabull, Bolt, Copilot…
  - Nessun nuovo codice richiesto
  - **Scrivi una volta, usi ovunque**

![alt text](images/con_mcp.png)

---

## 🔁 Un ecosistema in crescita

- Oggi ci sono **tantissimi MCP server** già attivi
- Strumenti AI come **Cursor**, **Claude** e altri **usano già MCP**
- Sta diventando uno **standard di fatto** come i protocolli nei social media o nel web
- Più persone lo adottano → più valore genera per tutti (effetto network/flywheel)

---

## 🎯 Obiettivo del corso

- Renderti **proficiente nell’uso e nella creazione di MCP server**
- Capire **come funziona internamente** il protocollo
- Imparare a **creare agenti AI compatibili con MCP**
- Permetterti di **scalare l’interoperabilità** delle tue applicazioni AI senza moltiplicare il codice

---

## ⏭️ Prossimo step

- Nella prossima lezione: **"Cos’è tecnicamente l’MCP"**  
  Vedremo:
  - Come appare
  - Come si implementa
  - Qual è la struttura del protocollo
