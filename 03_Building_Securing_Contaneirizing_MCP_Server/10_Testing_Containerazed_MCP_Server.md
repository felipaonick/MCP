# 🧪 **Testing completo del MCP server in Docker con Cloud Desktop**

## 🎯 Obiettivo del video

* ✅ Verificare che il server MCP venga avviato da Docker tramite Claude Desktop
* 🪟 Aprire il terminale e leggere i **log dei container**
* 💬 Inviare comandi tramite Claude Desktop
* 🔒 Verificare l'**isolamento del container**
* 🧼 Eseguire un comando di eliminazione file
* ☁️ Fare **commit su GitHub** del `Dockerfile` finale

---

## 🚀 1. Riavvio e Verifica Iniziale

* 🧠 Riaprire **Claude Desktop**
* 🔍 Verifica che il tool `run_command` sia presente sotto il server `docker_shell`
* ✅ Controlla in **Settings > Developer** che i parametri Docker siano esattamente quelli del JSON

---

## 📜 2. Lettura Log dei Container

* Usa `docker ps` per vedere i container attivi
* Ne trova **due** → uno è "leftover" da tentativi precedenti
* Usa `docker logs --follow <container_id>` per vedere i log in tempo reale

### 📥 Primo log mostrato:

* Risposta alla richiesta `list_tools`
* Include:

  * Nome tool: `run_command`
  * Descrizione
  * Argomenti e tipi
  * Valore di ritorno

> 💬 Questo è il *handshake* iniziale tra MCP client e server.

---

## 🧪 3. Invocazione tool via Claude Desktop

### Prompt:

> "Write 'Hello MCP' in ASCII art and echo it via terminal, then save it in hello_mcp.txt file"

* ✨ ASCII art viene generata
* 🟢 MCP chiede autorizzazione per eseguire `run_command`
* ✅ Viene approvato → output ricevuto correttamente


```plaintext
_   _      _ _        __  __  ____ ____  
| | | | ___| | | ___  |  \/  |/ ___|  _ \ 
| |_| |/ _ \ | |/ _ \ | |\/| | |   | |_) |
|  _  |  __/ | | (_) || |  | | |___|  __/ 
|_| |_|\___|_|_|\___/ |_|  |_|\____|_|
```

🧭 Verifichiamo i log del **secondo container** e lì troviamo effettivamente:

* Comando ricevuto
* Output ASCII ricevuto via `stdout`
* `status_code = 0` (esecuzione OK)

---

## 🧪 4. Scrittura file e cat per verifica se è stato scritto e salvato il file

### Prompt successivo:

> "Write 'Cool' in ASCII art and echo it via terminal, then save it in cool.txt file"


```plaintext
██████╗ ██████╗  ██████╗ ██╗     
██╔════╝██╔═══██╗██╔═══██╗██║     
██║     ██║   ██║██║   ██║██║     
██║     ██║   ██║██║   ██║██║     
╚██████╗╚██████╔╝╚██████╔╝███████╗
 ╚═════╝ ╚═════╝  ╚═════╝ ╚══════╝
```

* 🔍 MCP mostra:

  * Input ricevuto
  * Comando eseguito
  * ASCII art nel `stdout`

---

## 🔒 5. Isolamento del file system

### Prompt:

> "List files in \~/Desktop"

* 🧱 Il container non ha montato il desktop locale, non ha tale cartella come volume nel suo interno.
* ⚠️ Risultato: `No such file or directory`
* Risponde con: `This is a Linux/Docker environment, not a Windows system, so the Windows path C:\Users\felip\Desktop doesn't exist here. The current working directory is /app and contains some Python project files.`

Dunque dalla risposta si vede che non ha accesso al file system reale, ma solo a quello del container (quello di `/app`).

✅ Output:

* ❌ Nessun accesso al `Desktop` del sistema reale → **sandbox funzionante**

---

## 🧨 6. Rimozione file con `rm`

### Prompt:

> "Remove hello_mcp.txt"

* ✅ MCP esegue `rm -f hello_mcp.txt`
* Claude verifica la rimozione
* 🧠 Verifichiamo manualmente entrando nel container con:

* Prima dell'eleminazione:

```bash
docker exec -it <container_id> sh
ls -la

total 80
drwxr-xr-x 1 root root  4096 Jun  4 15:54 .
drwxr-xr-x 1 root root  4096 Jun  4 15:36 ..
drwxr-xr-x 1 root root  4096 Jun  4 10:56 .venv
-rw-r--r-- 1 root root   619 Jun  4 15:54 hello_mcp.txt
-rwxr-xr-x 1 root root   181 Jun  3 09:24 pyproject.toml
-rwxr-xr-x 1 root root  2885 Jun  3 15:55 server.py
-rwxr-xr-x 1 root root 47247 Jun  3 09:24 uv.lock
```

* Dopo l'eleminazione:

```bash
ls -la


total 76
drwxr-xr-x 1 root root  4096 Jun  4 16:00 .
drwxr-xr-x 1 root root  4096 Jun  4 15:36 ..
drwxr-xr-x 1 root root  4096 Jun  4 10:56 .venv
-rwxr-xr-x 1 root root   181 Jun  3 09:24 pyproject.toml
-rwxr-xr-x 1 root root  2885 Jun  3 15:55 server.py
-rwxr-xr-x 1 root root 47247 Jun  3 09:24 uv.lock
```


## 🧑‍💻 7. Commit finale su GitHub

* Aggiunge `Dockerfile`
* Usa la funzionalità AI di **Cursor** per generare il messaggio di commit
* Esegue:

```bash
git add Dockerfile
git commit -m "Add Dockerfile for containerized MCP server"
git push
```

🔗 Codice disponibile su GitHub

---

## ✅ Conclusione e Risultati

| Verifica                                                                            | Esito |
| ----------------------------------------------------------------------------------- | ----- |
| ✔️ Docker eseguito via Cloud Desktop                                                | ✅     |
| 🔗 Comando Docker corretto (con `-i`, `--rm`, `--init`, `-e DOCKER_CONTAINER=true`) | ✅     |
| 📤 Comandi eseguiti via MCP tool `run_command`                                      | ✅     |
| 🧱 Nessun accesso al file system host (sandbox OK)                                  | ✅     |
| 🧼 Comandi `rm`, `cat`, `echo` funzionanti                                          | ✅     |
| ☁️ Dockerfile committato su GitHub                                                  | ✅     |

---

## 🧠 Takeaway finale

> **“Containerizzare il server MCP migliora l’isolamento, la sicurezza e la portabilità, senza sacrificare funzionalità.”**
> 🌐 È pronto per essere eseguito su qualsiasi macchina o in cloud.

---
