
# ⚙️ Configurare un MCP Server – Esempio: Weather Server

---

## 🎯 Obiettivo

Imparare a:
- Configurare un **MCP server pre-esistente**
- Collegarlo a **Claude** e **Cursor**
- Comprendere la struttura base di un MCP server
- Gestire problemi comuni di configurazione e dipendenze

---

## 🗂️ Organizzazione iniziale

1. Crea una directory: `MCP-servers`
   - Scopo: contenere tutti i server MCP locali
2. Clonare un **MCP server esistente**
   - Esempio usato: `weather MCP server` dal repo **Model Context Protocol – Quickstart**

---

## 🧭 Local vs Remote Server

| Tipo        | Descrizione                                        |
|-------------|----------------------------------------------------|
| **Locale**  | Eseguito sulla tua macchina                        |
| **Remoto**  | Eseguito nel cloud, gestito da terze parti         |

> In questo esempio lavoriamo con **server locali**

---

## 🌦️ Il Weather MCP Server

- Linguaggio: **TypeScript (Node.js)**
- Funzionalità offerte:
  - `get_forecast(lat, lon)`
  - `get_alerts(lat, lon)`

---

## 🔧 Requisiti iniziali

Assicurarsi di avere installato:
- Node.js
- npm

Verifica con:
```bash
node -v
npm -v
```

---

## 🛠️ Passaggi di configurazione

1. Clona il repo Quickstart:
   ```bash
   git clone https://github.com/.../model-context-protocol/quickstart
   ```

2. Naviga nella cartella:
   ```bash
   cd quickstart-resources/weather-server/typescript
   ```

Qui abbiamo un file 'package.json' con la lista di tutte le dipendenze.

Seguendo la docuemntazione ed il quickstart del repository scegliamo di integrare il MCP Server usando 'Node' dunque sarà costruito usando 'NodeJS'.

Dunque la prima cosa che vogliamo fare è assicurarcci che abbiamo Node ed npm installati.

```bash
node --version
npm --version
```

3. Rimuovi `package-lock.json` in caso di errore con `npm install`:
   - Il lock file potrebbe causare **incompatibilità con la tua versione di Node**

4. Installa le dipendenze:
   ```bash
   npm install
   ```

Se andiamo in 'src/index.ts' vediamo l'implementazione del pre-built MCP server che ci darà le previsioni del tempo.

5. Compila il server:
   ```bash
   npm run build
   ```

   - Output: directory `build/` con file `index.js`

---

## ⚠️ Problema comune: errore con `npm install`

**Errore**: dipendenze in conflitto  
**Soluzione**:  
```bash
rm package-lock.json
npm install
```

---

## 🔒 Nota di sicurezza

- ⚠️ **Non fidarti ciecamente di ogni server MCP open-source**
- Potrebbero contenere codice malevolo
- Rischio: **attacchi alla supply chain**
- Verifica sempre i server prima di eseguirli localmente

---

## 🧩 Integrazione con Claude e Cursor

Per far funzionare il server MCP:
- Serve **solo indicare/dire al client (Cursor o Claude) come si avvia tale MCP server**


> Una volta fatto, il client MCP sarà in grado di:
> - Rilevare gli strumenti disponibili (`get_forecast`, `get_alerts`)
> - Utilizzarli come se fossero parte dell'agente

---

## ✅ Conclusione

Hai ora configurato il tuo primo **MCP server locale**:
- Organizzato il codice
- Risolto problemi di dipendenza
- Collegato con successo agli agenti AI
