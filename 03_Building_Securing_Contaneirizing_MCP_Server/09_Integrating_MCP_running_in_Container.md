# 🐳 **Esecuzione del MCP Server Dockerizzato da Claude Desktop**

## 🎯 Obiettivo del video

In questo episodio:

* Configuriamo **Claude Desktop** per **avviare il MCP server** da un container Docker 🧱
* Risolviamo un **errore di esecuzione**
* Analizziamo tutte le **opzioni del comando `docker run`**
* Captiamo la necessità della variabile d’ambiente `DOCKER_CONTAINER=true`

---

## 🏃‍♂️ 1. Metodo originale (pre-Docker)

Prima di Docker:

```bash
uv run server.py
```

✅ Veniva eseguito direttamente da directory locale con ambiente virtuale UV attivo.

---

## 🐳 2. Metodo aggiornato con Docker

Ora vogliamo far eseguire **Docker** da Claude Desktop.

Modifichiamo la configurazione nel file JSON del client MCP, e aggiungiamo il comando per eseguire l'immagine (`shellserver-app`) Docker:

```json
"mcp_servers": {
  "docker_shell": {
    "command": "docker",
    "args": ["run", "-i",  "--rm", "--init", "-e", "DOCKER_CONTAINER=true", "shellserver-app", "--name", "shellserver_container"]
  }
}
```

La variabile di ambiente `-e DOCKER_CONTAINER=true` dice al server MCP, che è in running, che è in esecuzione all'interno di un Docker container.

Inoltre aggiungiamo il flag `-i` interactive che mantiene aperto `stdin` per il client MCP, questo significa che il container può accettare comandi da noi scritti sulla tastiera o da un programma ovvero dal client MCP.

Il flag `--init` è un helper che aiuta a gestire i segnali e a evitare **zombie process**, ovvero aggiunge un piccolo processo per pulire alcuni child process per evitare dei processi zombie che potrebbero rimanere in esecuzione dopo la chiusura del container.


---

## ⚙️ 3. Spiegazione del comando `docker run`

| Flag                       | Spiegazione          | 🔍 Dettagli                                        |
| -------------------------- | -------------------- | -------------------------------------------------- |
| `run`                      | Esegue un container  | Avvia una nuova istanza                            |
| `-i`                       | Modalità interattiva | Mantiene aperto `stdin`, necessario per MCP client |
| `--rm`                     | Auto-pulizia         | Il container viene rimosso alla chiusura 🧹        |
| `--init`                   | Gestione segnali     | Evita **zombie process**                           |
| `-e DOCKER_CONTAINER=true` | Variabile d’ambiente | Comunica al server MCP che è in un container 📦    |
| `shellserver-app`         | Nome immagine Docker | Deve corrispondere all’immagine costruita          |

---

## 🧪 4. Debug e fix dell'errore iniziale

### 🧨 Errore:

* Claude Desktop lanciava il container ma non riceveva output né connessione
* Nessun log utile → il container veniva avviato ma non rispondeva come atteso

### 🔍 Soluzione trovata:

🔎 Eden ha cercato su Google `MCP Docker`, trovando che:

> ✅ *È necessario settare la variabile d’ambiente `DOCKER_CONTAINER=true`.*

Questo fa capire al **MCP Python SDK** che è in esecuzione dentro un container e può **attivare comportamenti specifici**, come gestire correttamente stdin/stdout o modificare il meccanismo di handshake con il client.

---

## 📋 5. Riepilogo dei passaggi

| Step                                 | Azione                                               |
| ------------------------------------ | ---------------------------------------------------- |
| 🧱 Dockerfile pronto                 | MCP server Dockerizzato                              |
| 🧠 Configurazione aggiornata in JSON | `"command": "docker", "args": [...]`                 |
| 🧪 Errore analizzato                 | Mancava `DOCKER_CONTAINER=true`                      |
| ✅ Fix applicato                      | Aggiunta variabile e flag `--init`                   |
| 🧑‍💻 Verifica completata            | MCP server in Docker ora eseguibile da Cloud Desktop |

---

## 💡 Consiglio DevOps di Eden

> *“Non sentirti in difetto se non capisci tutto: questo è lavoro DevOps. L'importante è sapere come funziona a grandi linee e come integrarlo.”*

🎓 Questo approccio ti permette di:

* Usare un MCP server **in modo isolato e sicuro**
* Prepararti al **deploy su orchestratori** come Kubernetes o ambienti cloud come GKE/EKS

---

## ✅ Output finale

Con questa configurazione:

* ✅ Claude Desktop **comunica** correttamente con il container
* ✅ Il server MCP **risponde** come previsto
* ✅ Il tutto è **isolato**, **portabile** e **facilmente riavviabile**

---
