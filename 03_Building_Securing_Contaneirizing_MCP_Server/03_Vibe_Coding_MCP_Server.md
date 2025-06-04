# 🚀 **Implementazione di un MCP Server da Zero**

## 🎯 Obiettivo del video

* Creare un **MCP server** da zero con Python
* Esporre un **tool chiamato `terminal`** capace di eseguire comandi della shell 💻
* Usare **Cursor** per generare codice automaticamente
* Eseguire e **debuggare** il server
* **Configurarlo** in Claude Desktop per testarlo e usarlo

---

## 📁 Setup iniziale del progetto

1. ✅ `server.py` è il file principale (inizialmente vuoto)

2. ✨ Apertura di **Cursor**:

   * Su Mac: `Cmd + I`
   * Su Windows: `Ctrl + I`

3. ✍️ Prompt usato con Cursor:

   ```plaintext
   I want you to implement me a simple MCP server from @MCP. Use the Python SDK @MCP Python SDK and the server should expose one tool which is called terminal tool which will allow the user to run terminal commands, make it simple.
   ```

   * Sono stati taggati i link alla documentazione MCP e SDK Python

4. 💡 Cursor:

   * Ha generato **server.py**
   * Ha creato e aggiornato anche un `README.md` ✅

---

## 📦 Analisi del codice generato

### 📚 Importazioni principali:

```python
from mcp.server.fastmcp import FastMCP
import subprocess
import asyncio
from typing import Dict, Optional, Any, List
```

* `FastMCP`: oggetto del server MCP
* `subprocess` + `asyncio`: per eseguire comandi shell in maniera non bloccante
* `typing`: per type hint del dizionario di output

---

### 🛠️ Implementazione del Tool `run_command`

```python
@mcp.tool(description="Run a terminal command and return output, stderr, and return code")
async def run_command(command: str) -> Dict:
```

📌 Il tool:

* Riceve una stringa `command`
* Esegue il comando in shell
* Ritorna un dizionario:

  * `stdout`: output del comando
  * `stderr`: eventuali errori
  * `returncode`: codice di uscita

🧠 Il cuore:

Esegue il comando che abbiamo fornito tramite `subprocess` e `asyncio` per non bloccare il server.

`subprocess.PIPE` dice al sottoprocesso del terminale di creare una nuova pipe che sarà usata per la comunicazione con il processo genitore.

```python
process = await asyncio.create_subprocess_shell(
    command,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE
)
stdout, stderr = await process.communicate()
```

📤 Output formattato:

```python
return {
    "stdout": stdout.decode(),
    "stderr": stderr.decode(),
    "returncode": process.returncode
}
```

🛡️ Inclusa anche gestione delle eccezioni nel caso il comando fallisca.

---

## 🐞 Debug: Errore iniziale e Fix

### ❌ Errore:

```python
await mcp.serve()
```

* 🔴 `serve` **non esiste**

### ✅ Fix:

```python
mcp.run("stdio")
```

* Il server viene avviato e comunica tramite `stdin/stdout` (richiesto da Claude Desktop)

---

## ⚙️ Integrazione e Configurazione in **Claude Desktop**

### 🧭 Percorso:

1. Vai su `Settings > Developer > Edit Config`
2. Aggiungi la definizione del server MCP:

```json
"mcp_servers": {
  "shell": {
      "command": "C:/Users/felip/.local/bin/uv.exe",
      "args": ["--directory", "C:/Users/felip/Desktop/import-pc/MCP/03_Building_Securing_Contaneirizing_MCP_Server/shellserver", "run", "server.py"],
      
    }
}
```

> 📌 **Errore comune**: inserire il blocco `"shell"` **fuori** da `"mcp_servers"` ❌
> 🔧 Soluzione: assicurarsi che `"shell"` sia **interno** al dizionario `"mcp_servers"` ✅

---

## 🔁 Reload e verifica

1. Riavvia Cloud Desktop
2. ✔️ Verifica che il nuovo **tool `run_command`** sia visibile
3. L’etichetta e descrizione del tool corrispondono a quelle definite nella funzione Python

---

## 🧪 Test del server MCP integrato

### Prompt usato:

> "Can you please list me the directories in my desktop?"

* 🟢 Il tool `run_command` viene attivato
* Claude Desktop genera il comando: `ls -la ~/Desktop`
* MCP lo esegue e restituisce `stdout`
* Claude Desktop mostra l’output in linguaggio naturale

### 🔍 Verifica visiva:

* I nomi delle cartelle mostrate da Claude Desktop coincidono con quelli nel vero `~/Desktop`

---

## ✅ Conclusioni

| Azione                                         | Stato |
| ---------------------------------------------- | ----- |
| MCP server implementato con tool `terminal`    | ✅     |
| Cursor utilizzato per generare codice Python   | ✅     |
| Debug e correzione `serve` → `run("stdio")` | ✅     |
| Configurazione Cloud Desktop corretta          | ✅     |
| Test funzionale con output reale del terminale | ✅     |

---

## 🧠 Considerazioni finali

* 🧨 Gli strumenti MCP possono eseguire comandi **potenzialmente pericolosi** se mal configurati
* ✍️ Le **descrizioni nei tools** sono fondamentali per farli usare correttamente dai client
* 🧪 Gli errori di configurazione (es. JSON mal strutturato) sono **comuni ma facili da risolvere**
* 🤖 Cursor è utile ma può **hallucinare metodi inesistenti**: è bene **verificare sempre il codice generato**

---