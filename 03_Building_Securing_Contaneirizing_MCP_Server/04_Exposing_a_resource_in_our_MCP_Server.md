# 📄 Esposizione di una *Resource* nel MCP Server

## 🎯 Obiettivo del video

In questo episodio:

* 📥 Scarichiamo il contenuto del `README.md` del **MCP Python SDK**
* 💾 Lo salviamo localmente nel filesystem
* 🌐 Lo esponiamo come **risorsa accessibile da un client MCP**

---

## 🔽 1. Download del contenuto del Readme

🔗 Passaggi:

1. Vai su GitHub al repository dell’MCP Python SDK (`https://github.com/modelcontextprotocol/python-sdk`)
2. Apri il file `README.md`
3. Copia tutto il contenuto 📋

---

## 💻 2. Salvataggio locale del Readme

Nel terminale:

```bash
cd ~/Desktop
vim mcpreadme.md
# oppure usa un altro editor a tua scelta
```

📌 All’interno del file `mcpreadme.md`:

* Incolla il contenuto del README del repo GitHub
* Salva e chiudi il file 💾

---

## 🤖 3. Generazione automatica del codice con Cursor

📂 Apri `server.py` nel tuo progetto

🎯 Prompt scritto in Cursor:

> Implement a resource using the Python SDK that exposes the file `mcpreadme.md` from the desktop directory

🏷️ Hai taggato:

* 📘 La documentazione MCP
* 🐍 L’SDK Python MCP

🕒 Nota: questa richiesta richiede un po’ più tempo perché Cursor deve processare **molto contesto**

---

## 🧑‍💻 4. Analisi del codice generato

### 🆕 Coroutine: `mcpreadme()`

```python
@mcp.resource("file:///mcpreadme")
async def mcpreadme() -> str:
    """
    Expose mcpreadme.md from the user's Desktop directory
    
    Returns:
        The contents of mcpreadme.md as a string
    """
    desktop_path = Path.home() / "Desktop"
    readme_path = desktop_path / "mcpreadme.md"
    
    try:
        with open(readme_path, "r") as file:
            content = file.read()
        return content
    except Exception as e:
        return f"Error reading mcpreadme.md: {str(e)}"
```

### 🧩 Spiegazione:

* `@mcp.resource(...)`: indica che questa funzione fornisce **una risorsa statica**
* 🔁 Nessun argomento in input
* 📤 Output: stringa con il contenuto del file markdown
* 📌 Il path dev’essere **assoluto o relativo corretto**, altrimenti il server non troverà il file

🎯 Lo scopo è fornire ai client MCP un contenuto contestuale da allegare ai prompt, come documentazione o guida.

---

## 🔁 5. Riavvio del server MCP

🛠 Dopo aver aggiornato `server.py`, è necessario:

1. 🔄 Chiudere e riaprire Claude Desktop
2. In questo modo viene **ricaricata la configurazione aggiornata** con la nuova resource esposta

---

## 📂 6. Verifica in Claude Desktop

1. Clic sull’icona dei cavi 🧷
2. Scegli l’integrazione → `shell` MCP server
3. ✅ Ora vedi la nuova risorsa: `file.readme`
4. 🔍 Facendo doppio clic la puoi visualizzare: è esattamente il contenuto di `mcpreadme.md`
5. 🧠 Puoi **allegarla ai prompt** come contesto extra per ottenere risposte più informate

---

## ✅ Riepilogo delle azioni

| Azione                                               | Stato |
| ---------------------------------------------------- | ----- |
| Copiato README da GitHub                             | ✅     |
| Salvato localmente come `.md`                        | ✅     |
| Generato il codice della risorsa con Cursor          | ✅     |
| Decorato con `@mcp.resource(...)`                    | ✅     |
| Riavviato Cloud Desktop per riflettere i cambiamenti | ✅     |
| Testata la resource in Cloud                         | ✅     |

---

## 🔐 Nota di sicurezza

➡️ Anche se in questo caso abbiamo esposto un file *benigno* (README), il concetto di *resource exposure* va gestito con attenzione, soprattutto se il file contiene:

* 🔒 Informazioni sensibili
* 🔧 Configurazioni interne
* 🛡️ Token o credenziali

---

## 🧠 Conclusione

Hai imparato a:

* Integrare una **resource testuale** nel tuo MCP server
* Utilizzarla tramite Claude Desktop come **contesto utile** nei prompt
* Automatizzare tutto grazie a **Cursor**

---