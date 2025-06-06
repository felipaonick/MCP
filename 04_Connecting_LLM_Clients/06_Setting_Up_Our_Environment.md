## 🧱 Setup Progetto MCP LangChain Adapters con UV e Cursor IDE

### 🎯 Obiettivo del video

Preparare uno scheletro di progetto in Python per lavorare con MCP e LangChain:

* Usando il package [`langchain-mcp-adapters`](https://github.com/langchain-ai/langchain/tree/main/libs/mcp-adapters)
* Configurando l’ambiente virtuale con [`uv`](https://github.com/astral-sh/uv)
* Inizializzando un progetto Git in un nuovo branch
* Creando un file `.env` per la gestione sicura delle API key
* Installando le dipendenze base per interagire con LLMs

---

## 📁 1. Creazione del Progetto

### ✅ Clonare il repository MCP Crash Course

```bash
git clone <url-del-repo>  # URL disponibile tra le risorse video
cd mcp-crash-course
```

### ✅ Creare un nuovo branch *orphan* (senza cronologia preesistente)

```bash
git checkout --orphan project/langchain-mcp-adapters
```

### ✅ Pulire tutti i file esistenti

```bash
git rm -rf .
```

---

## 🧪 2. Inizializzare progetto con `uv`

```bash
uv init
```

Questo comando crea i file base:

* `pyproject.toml`
* `main.py`
* `README.md`

---

## 🌐 3. Creazione e attivazione virtual environment

```bash
uv venv
source .venv/bin/activate  # oppure .venv/Scripts/activate su Windows
```

---

## 📦 4. Installazione dipendenze

### Dipendenze principali

```bash
uv add langchain-mcp-adapters langgraph langchain-openai
```

> 🔁 `langchain-mcp-adapters` installa anche automaticamente il pacchetto `mcp`.

### Aggiunta `python-dotenv` per gestione variabili ambiente

```bash
uv add python-dotenv
```

---

## 🔐 5. Configurazione variabili ambiente `.env`

Creare un file `.env` nella root del progetto con:

```env
OPENAI_API_KEY=sk-...
LANGCHAIN_API_KEY=...
LANGCHAIN_PROJECT=MCP-Test
LANGCHAIN_ENDPOINT=https://api.smith.langchain.com
LANGCHAIN_TRACING_V2=true
```

> ✅ È possibile usare anche altri LLM che supportano **function calling**, come:
>
> * Anthropic Claude (es. *Sonnet*)
> * Google Gemini
> * DeepSeek

---

## 📁 6. Aggiungere `.gitignore` per proteggere `.env`

Creare un file `.gitignore`:

```
.env
```

> Questo evita di committare accidentalmente le API key.

---

## 🧪 7. Esecuzione di test su `main.py`

### Versione base:

```python
print("Hello from MCP!")
```

### Versione asincrona:

```python
import asyncio

async def main():
    print("Hello from MCP async!")

if __name__ == "__main__":
    asyncio.run(main())
```

Esegui con:

```bash
uv run main.py
```

---

## 🌱 8. Caricamento variabili con `dotenv`

Aggiorna `main.py` per caricare e verificare `.env`:

```python
import os
from dotenv import load_dotenv

load_dotenv()

print(os.environ.get("OPENAI_API_KEY"))
```

> Assicurati di importare anche `os`.

---

## 💾 9. Commit iniziale su GitHub

### Aggiungere tutti i file

```bash
git add .
```

### Commit (con AI assistita da Cursor)

```bash
git commit -m "Initial setup with MCP + LangChain adapters"
```

### Push al branch remoto

```bash
git push -u origin project/linkchain-mcp-adapters
```

Ora i file saranno visibili online:

* `main.py`
* `.gitignore`
* `.env` (ignorato)
* `pyproject.toml`
* `uv.lock`

---

## ✅ Riepilogo dei componenti installati

| Componente               | Descrizione                                |
| ------------------------ | ------------------------------------------ |
| `langchain-mcp-adapters` | Adattatore MCP ↔️ LangChain                |
| `langgraph`              | Libreria di orchestrazione (LangChain DAG) |
| `langchain-openai`       | Provider LLM                               |
| `python-dotenv`          | Gestione file `.env`                       |
| `uv`                     | Tool moderno per gestione pacchetti Python |

---

## 🔜 Prossimi Passi

Nel prossimo video:

* Si implementerà un **MCP client** che si connette a un **MCP server**
* Si integrerà con **LangChain Agents** per invocare strumenti da MCP
* Si aggiungerà tracing con **LangSmith** per monitorare gli step dell’agente

---
