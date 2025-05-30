# Introduzione al Model Context Protocol (MCP) 🌐

## Cos'è l'MCP? 🤖

Il **Model Context Protocol (MCP)** ha lo scopo di **standardizzare** il modo in cui le applicazioni forniscono **contesto** ai **LLM (Large Language Models)**. Questo contesto può essere molto semplice o complesso e può comprendere:

* **Contesto aggiuntivo al prompt**: Includere informazioni extra nel prompt che aiuti l'LLM a generare risposte migliori.
* **Quale strumento invocare**: Specificare quale strumento l'LLM deve utilizzare per ottenere la risposta.
* **Il prompt stesso**: In alcuni casi, il contesto può essere proprio il prompt da inviare all'LLM.

L'obiettivo è creare una **comunicazione standard** tra **diversi strumenti** e **LLM**.

![alt](images/mcp_architecture.png)

---

## Esempio Pratico di Utilizzo di MCP 🍽️

Un esempio interessante di utilizzo dell'MCP è il **server MCP** scritto da Eric Dickerson per **Cursor**. Questo server consente all'applicazione di AI (in questo caso, **Cursor**) di ordinare cibo, tramite il collegamento con il suo **Uber Eats** account.

### Flusso del Processo:

1. **Prompt iniziale**: L'utente scrive "I want FIKA, where can I get Kane Cain" (un tipo di dolce, in questo caso "Fika").
2. **MCP Server**: Il server MCP è connesso all'account Uber Eats di **Cursor** e può accedere al menu.
3. **Filtraggio dei Risultati**: Il server filtra i risultati, cerca il piatto richiesto e prepara l'ordine.
4. **Ordinazione**: Il sistema chiede all'utente se desidera ordinare il piatto e, in caso di conferma, invoca lo strumento di **ordine cibo** tramite Uber Eats.

Questo esempio dimostra la potenza dell'MCP, che consente di **integrare applicazioni AI** con strumenti esterni senza scrivere troppo codice.

---

## Architettura Generale di MCP 🏗️

### 1. **MCP Host (Applicazioni AI)** 🖥️

Un **MCP Host** è l'applicazione che supporta il protocollo MCP, come **Claude Desktop**, **Windsurf**, **Cursor**, o altre applicazioni AI specializzate che supportano il protocollo MCP. Attenzione, non si è parlato del modello Claude-sonnet-3.7 ma di **Claude Desktop** dato che è essa l'applicazione AI che utilizza sotto il cofano i modelli di Anthropic. Possiamo creare anche le nostre applicazioni AI (MCP Hosts) purchè seguano il protocollo e lo implementino. Gli **MCP Hosts** (le applicazioni AI non i modelli LLM) sono quelli che riceveranno l'accesso ai dati esterni, ai tool o ai prompt.

### 2. **MCP Server (Fornitori di Dati)** 🌍

Il **MCP Server** è il componente che espone risorse, strumenti (tools) e prompts tramite il protocollo MCP. I server sono i **gateway** che offrono l'accesso (tramite API o protocolli di comunicazione come http) a funzionalità come il recupero di dati esterni, l'esecuzione di azioni (tools) o la generazione di risposte basate su input.

Per esporre queste funzionalità necessitano avere dei **metodi** e certe **funzioni**, ad esempio **list_prompts**, **get_prompt**, **list_tools**, **call_tool**, ecc.

### 3. **Comunicazione tra Client e Server** 💬

Una volta che abbiamo implementato un MCP Server, esso può essere chiamato/collegato da qualsiasi MCP Client che **supporti il protocollo**. 
Questo significa che possiamo scrivere le nostre funzionalità una volta sola ed esporle per poi collegarle a molti MCP Clients.

Il client MCP, che si trova all'interno del MCP host, interagisce con il server MCP tramite il **protocollo MCP**. È importante notare che:

* Ogni **MCP Client** può comunicare solo con **un singolo MCP server** alla volta (1 to 1 Connection tra MCP Client e MCP Server).
* Se un **MCP Host** (ad es. Claude Desktop) desidera connettersi a più server, sarà necessario **moltiplicare gli MCP Client** all'interno dell'host.

---

## Vantaggi dell'Utilizzo di MCP 💡

### 1. **Integrazioni e Strumenti** 🔌

MCP consente di **collegare facilmente** applicazioni AI a **fonti di dati esterne** e **strumenti**, come ad esempio:

* API per il recupero di dati
* Strumenti di calcolo o ricerca
* Connettori per database esterni

### 2. **Indipendenza dal Fornitore dell'LLM** 💼

Un grande vantaggio dell'MCP è che non siamo legati a un singolo **fornitore di LLM** o **sviluppatore di applicazioni AI**. Possiamo scrivere strumenti e **tool** indipendenti dal fornitore e **migrare facilmente** tra diversi **vendor LLM**.

### 3. **Capacità di Plug-and-Play** 🔄

L'MCP offre una **capacità di plug-and-play** simile a una **porta USB**, permettendo di **collegare facilmente** strumenti o funzionalità esterne a un'applicazione AI, come nel caso dell'integrazione di **Uber Eats** in **Cursor**.

---

## Confronto tra MCP e LangChain 🔗

### 1. **LangChain** 🔗

**LangChain** è un framework open-source che consente di integrare LLM con strumenti esterni e fonti di dati. Si focalizza sulla costruzione di **catene di strumenti** (chains) e interazioni tra LLM.

### 2. **MCP vs LangChain** ⚖️

Sebbene **MCP** e **LangChain** risolvano problemi simili, ognuno lo fa in modo diverso:

* **MCP** si concentra sulla **standardizzazione** del contesto tra strumenti e LLM, consentendo una facile integrazione tra **diversi applicativi AI**.
* **LangChain** è più orientato alla **creazione dinamica di flussi** di lavoro, gestendo diversi modelli e strumenti in una singola applicazione AI.

In un futuro video, esploreremo **come si combinano** e **cosa ciascun framework porta in più**.

---

## Componenti Principali di MCP 🧩

### 1. **MCP Host** 🖥️

Le applicazioni AI che utilizzano MCP, come **Claude Desktop**, **Cursor**, o altre specializzazioni, che traggono vantaggio dalle funzionalità esterne, come API, database, e strumenti aggiuntivi.

### 2. **MCP Server** 🌐

Il **server MCP** è l'entità che espone gli strumenti, le risorse e i prompt tramite il protocollo MCP. Permette a qualsiasi applicazione di interagire con questi strumenti.

---

## Conclusioni 🎯

MCP offre un modo **standardizzato** per arricchire le applicazioni AI con strumenti esterni e dati, creando un sistema **plug-and-play** che permette di:

* **Integrare facilmente** fonti di dati e strumenti.
* Essere **indipendenti dal fornitore** di LLM o dalle applicazioni AI.
* Semplificare la comunicazione tra diversi **componenti AI** grazie al protocollo standard.

In futuro, esploreremo ulteriormente la **creazione di server MCP** e come integrarli con i client per una comunicazione fluida tra le applicazioni AI. 🚀

---
