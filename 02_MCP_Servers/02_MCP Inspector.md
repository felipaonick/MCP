# Introduzione a MCP Inspector 🛠️

## Cos'è MCP Inspector? 🕵️‍♂️

**MCP Inspector** è uno strumento open-source sviluppato dal team di **Anthropic**, creatore del **Model Context Protocol (MCP)**. Questo strumento è essenziale per **troubleshooting**, **debugging** e **tracing** nelle applicazioni che utilizzano **MCP servers**. Permette di vedere cosa succede effettivamente all'interno del server MCP, rendendo la vita molto più facile per gli sviluppatori.

[MCP Inspector](https://modelcontextprotocol.io/docs/tools/inspector#py-pi-package)

### Funzionalità Principali 🌟

* **Testing e Debugging**: Consente di interagire con il server MCP, eseguire test e risolvere problemi senza la necessità di installazioni complesse.
* **Interazione Senza Installazione**: Può essere eseguito localmente tramite **npm**, il che lo rende molto comodo durante lo sviluppo.

---

## Caratteristiche di MCP Inspector 🔍

### 1. **Panoramica delle Risorse** 📂

La sezione delle **risorse** ti consente di visualizzare tutte le risorse disponibili nel server MCP, mostrando **metadata** e permettendo **l'ispezione del contenuto**:

* Puoi vedere quali risorse sono esposte e **interagire con esse** per ottenere i dettagli.

### 2. **Gestione dei Prompt** 📝

La sezione dei **prompt** mostra:

* **Template dei prompt**: Visualizza i modelli di prompt utilizzati dal server.
* **Argomenti dei prompt**: Mostra i parametri che i prompt richiedono.
* **Testing Personalizzato**: Permette di testare i template dei prompt con **input personalizzati**, utile per verificare come risponde il server a vari scenari.

### 3. **Tab degli Strumenti (Tools)** 🛠️

Il tab degli **strumenti** elenca:

* Tutti gli strumenti disponibili nel server, inclusi i relativi **schemi**.
* La possibilità di **testare gli strumenti** con **input personalizzati**, consentendo di eseguire le funzioni del server direttamente nell'interfaccia.

### 4. **Pannello di Notifiche** 📢

Il **pannello di notifiche** visualizza:

* **Log e notifiche** dal server MCP, fornendo un modo per monitorare le attività e individuare eventuali problemi.

---

## Come Funziona MCP Inspector 🚀

### 1. **Connessione a un Server** 🌍

MCP Inspector ti permette di connetterti a un server MCP in esecuzione, sia tramite il protocollo **SSH** che tramite il protocollo **stdio**. Una volta connesso:

* Puoi esplorare gli strumenti esposti dal server e **testarli** direttamente.

### 2. **Esempio di Connessione a un Server** 🔌

Nel video, l'autore si connette a un **server MCP in esecuzione localmente** tramite **SSH**:

* Il server espone due strumenti:

  1. **List Document Sources**: Visualizza tutte le fonti di documentazione disponibili.
  2. **Fetch Docs**: Permette di recuperare documenti specifici tramite input dinamico.

---

## Esempio di Utilizzo di MCP Inspector 🎬

### 1. **Visualizzazione degli Strumenti** 🛠️

Una volta connessi, puoi visualizzare gli strumenti disponibili nel server MCP. Ad esempio:

* Lo strumento **List Document Sources** ti permette di ottenere un elenco delle fonti di documentazione.
* Puoi testare lo strumento **Fetch Docs**, dove puoi fornire un **input dinamico** (ad esempio, una richiesta di documentazione) e vedere il risultato direttamente nell'interfaccia di MCP Inspector.

### 2. **Testare gli Strumenti** 🧪

* Utilizzando il **Playground** di MCP Inspector, puoi testare come gli strumenti rispondono a diversi input.
* È particolarmente utile per verificare che il server MCP stia funzionando correttamente e che gli strumenti espongano i dati giusti.

---

## Conclusione 🎯

**MCP Inspector** è uno strumento potente e pratico per lo sviluppo e il debugging di **MCP servers**. Consente di:

* **Esplorare e testare** strumenti e risorse esposte dal server MCP.
* **Monitorare** le notifiche e i log per risolvere rapidamente i problemi.
* **Esegui test personalizzati** su strumenti e prompt per verificare il comportamento del server.

Grazie a **MCP Inspector**, il processo di sviluppo di server MCP diventa molto più fluido e intuitivo, rendendolo uno strumento essenziale per ogni sviluppatore che lavora con il **Model Context Protocol**. 🚀

