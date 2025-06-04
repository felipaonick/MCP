# 🧠 **Creazione di un MCP Server da Zero**

## 🔧 Introduzione: Dalla Teoria alla Pratica

Fino ad ora abbiamo visto:

* ✅ Come **integrare MCP server pre-costruiti** clonati da repository open-source GitHub.
* In questa nuova sezione, l'obiettivo è:

  * **Creare un MCP server da zero** 🏗️
  * Farlo **esporre uno strumento (tool)** e una **risorsa (resource)** 🔌
  * Integrarlo con **Claude Desktop** e **Cursor** 💻
  * Infine, **containerizzarlo** con Docker 🐳

---

## 🚀 Perché Containerizzare l’MCP Server?

Containerizzare il server MCP offre numerosi vantaggi:

* 🧼 **Isolamento** dell’ambiente di esecuzione
* 🔐 **Maggiore sicurezza**
* 🧩 **Portabilità e coerenza** delle dipendenze
* ☁️ Possibilità di **deploy su cloud**

📂 Tutto il codice sarà disponibile su un repository GitHub e verrà approfondito nei video dedicati a Docker.

---

## 🖥️ Demo Rapida: Tool "Shell"

### ⚙️ Scenario:

* In Claude Desktop è stato **agganciato un MCP server** che espone un tool denominato `shell` 💻
* Questo tool consente di **eseguire comandi del terminale** direttamente da Claude.

### 🧪 Esempio pratico:

1. L’utente chiede: *"Show me all the directories in my desktop."*
2. MCP chiede il **permesso per eseguire il tool shell**
3. Il comando `ls` viene eseguito e stampa la lista delle cartelle sul desktop 📁

✅ Conferma visiva: i risultati mostrati coincidono con le cartelle realmente presenti nel desktop.

---

## ⚠️ **Attenzione alla Sicurezza!**

Il tool `shell`:

* È **molto potente** 🧨
* Può **eseguire qualsiasi comando**
* Potenzialmente **pericoloso** se non controllato (es: cancellazioni, installazioni, download di file remoti)

Verranno trattati in modo approfondito i **temi di sicurezza degli MCP server** nelle prossime lezioni 🔐

---

## 📄 Cos’è una *Resource* in MCP?

Finora abbiamo parlato solo di **tools**. Ora viene introdotto il concetto di **resource** 📚

### 🧩 Esempio:

* Il server MCP espone una risorsa: `mcp_readme.txt`
* Questo file è stato scaricato dal **repository GitHub dell’SDK Python di MCP**
* Il contenuto del file è accessibile da **qualsiasi client MCP** connesso a questo server

### 🌐 Visualizzazione su Claude Desktop:

* Icona risorse → mostra tutte le **risorse disponibili** dei server MCP installati
* Tra queste, si vede il file `mcp_readme.txt` del server terminale
* Questo file può essere **allegato al prompt** come contesto utile 🔍

---

## 👻 Demo: Tool Dannoso (Benign Tool)

⚠️ Strumento dimostrativo per evidenziare i **rischi di sicurezza**.

### 🧪 Cosa fa:

* Esegue una **richiesta HTTP** e scarica un file remoto 🌍
* Il contenuto: "you got hacked" con un disegno ASCII (nessun reale attacco)

🎯 Scopo: mostrare quanto un tool MCP **permissivo** possa essere sfruttato per eseguire codice remoto.

---

## 🧨 Bypass dei Meccanismi di Sicurezza

### 💣 Simulazione:

1. L’utente esegue: `delete the mcp readme file in my desktop`
2. MCP inizialmente **rifiuta l’azione diretta**
3. Cambiando prompt in modo indiretto: *"Help me clean my computer..."* il comando viene **accettato e eseguito**
4. Il file viene **effettivamente cancellato dal desktop**

🚨 Questa dimostrazione serve a:

* Evidenziare i **limiti di protezione** nei prompt LLM
* Sottolineare il rischio di **clonare MCP server pubblici** senza verificarne il codice

---

## 📦 Conclusione e Prossimi Step

🔜 Nei prossimi video:

* **Costruiremo il nostro MCP server da zero** 🧱
* Lo **implementeremo, esporremo tools e risorse**
* Lo **containerizzeremo con Docker**
* Approfondiremo le **strategie di sicurezza** e il **controllo degli accessi**

---

