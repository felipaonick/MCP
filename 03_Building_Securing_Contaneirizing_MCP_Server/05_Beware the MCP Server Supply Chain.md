# 🛡️ MCP & Sicurezza: Remote Code Execution e Supply Chain Attacks

## 🎯 Obiettivo del video

In questo episodio Eden mostra:

* Come un MCP server può essere sfruttato per eseguire **codice remoto malevolo** ☠️
* I **rischi di clonare MCP server pubblici** da GitHub
* Il concetto di **supply chain attack**
* Un esempio pratico di **esposizione di un tool malevolo**

---

## 🐍 1. Creazione di un file malevolo remoto (GitHub Gist)

### 🧱 Step:

1. Vai su [gist.github.com](https://gist.github.com)
2. Crea un nuovo **Gist pubblico** 📂
3. Incolla un disegno ASCII con il messaggio "you got hacked" 🖼️
4. Salvalo come `hacked.txt`

✅ Questo file sarà pubblicamente accessibile tramite URL.

---

## 🧰 2. Esposizione di un tool MCP chiamato `benign_tool`

🎯 Obiettivo: mostrare come **un tool apparentemente innocuo** può:

* Scaricare un file remoto (via `curl`)
* Eseguire codice potenzialmente pericoloso nel sistema locale 😨

### 🤖 Prompt scritto in Cursor:

> Implement a tool using Python MCP SDK that downloads the content of a public txt file via curl and returns it

📌 Il tool è generato con:

* Decoratore `@mcp.tool(...)`
* Uso di `subprocess` per eseguire il comando `curl`
* URL hardcoded nel codice

### 🔍 Funzionamento:

```python
@mcp.tool()
async def benign_tool() -> Dict[str, Any]:
    """
    Download content from a specified URL using curl.
    
    Returns:
        A dictionary containing the downloaded content and status
    """
    url = "https://gist.githubusercontent.com/felipaonick/2bc8cd87a9a8daf747b9f2288cf2b8fa/raw/c5b5ba36fa4b72203388a77a076a735f2c3ed6f1/hacked.txt"
    
    try:
        # Use curl to download the content
        process = await asyncio.create_subprocess_exec(
            "curl", "-s", url,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        
        # Get output
        stdout, stderr = await process.communicate()
        
        # Return results
        return {
            "content": stdout.decode() if stdout else "",
            "error": stderr.decode() if stderr else "",
            "success": process.returncode == 0
        }
    except Exception as e:
        return {
            "content": "",
            "error": f"Error downloading content: {str(e)}",
            "success": False
        }
```

---

## 💣 3. Esecuzione in Claude Desktop

1. Riavvia Cloud Desktop per ricaricare il nuovo tool
2. Inizia una nuova chat
3. Esegui: “**Run the benign tool**”
4. ✅ Viene richiesto il permesso per eseguire il tool
5. 🖼️ Il contenuto ASCII viene mostrato a schermo

---

## ⚠️ 4. Le *vere* implicazioni

💡 **Quello che abbiamo appena fatto**:

* Scaricato dinamicamente contenuto da una sorgente remota 🌐
* Iniettato **in tempo reale** in un sistema in esecuzione 🧠
* Eseguito del codice con permessi potenzialmente elevati 🔓

🎭 Anche se era solo un file `.txt`, **in uno scenario reale potrebbe essere**:

* Uno script che **ruba password** 🕵️‍♂️
* Una **reverse shell** per l’accesso remoto 🧨
* Un comando per **cancellare dati** o formattare il disco 💀

---

## 🧪 5. Remote Code Execution (RCE)

🧨 MCP server = **punto di ingresso critico**
➡️ Se usi un MCP server preso da GitHub senza verificarlo, stai **eseguendo codice di altri nella tua macchina**.

🎯 *"Clonare e avviare un MCP server da GitHub è letteralmente eseguire codice remoto di qualcun altro."*

---

## 🔄 6. Supply Chain Attacks

> Anche se un MCP server viene da **un fornitore affidabile**, esiste comunque un **rischio di attacco nella catena di dipendenze**.

🧩 Esempio:

* Cloni MCP da **Cloudflare** (o altro vendor)
* Usa una libreria open-source → che a sua volta è vulnerabile
* 🕳️ Attaccanti possono sfruttare vulnerabilità *a monte* (es. dipendenze compromesse)

---

## 🛡️ 7. Linee guida di sicurezza

### 🚫 Non fare:

* **Eseguire codice MCP preso da GitHub alla cieca**
* Affidarti solo alla "popolarità" o "star" del repo

### ✅ Fai sempre:

* **Leggi e verifica il codice prima di eseguirlo**
* Usa ambienti isolati (es. Docker, VM)
* Controlla **ogni URL hardcoded** o accesso esterno 🌍
* Audita le dipendenze con strumenti come `pip-audit`, `safety`, ecc.

---

## 📌 Conclusione

| Punto chiave                                | Descrizione                                                  |
| ------------------------------------------- | ------------------------------------------------------------ |
| 💻 MCP server esegue codice                 | I tool sono vere e proprie funzioni di sistema               |
| ☠️ Tool “innocui” possono essere pericolosi | Anche un `.txt` può mascherare uno script malevolo           |
| 🔗 Rischio supply chain                     | Anche vendor affidabili possono usare dipendenze vulnerabili |
| 🕵️ Verifica sempre il codice               | Mai fidarti ciecamente del codice open source                |

---

## 🚨 Takeaway

> **“MCP server è un'esecuzione remota mascherata. Può essere sicura… o può aprire una porta al tuo sistema.”**

🔒 *Sii paranoico con fiducia. È così che si sopravvive in cybersecurity.*

---

