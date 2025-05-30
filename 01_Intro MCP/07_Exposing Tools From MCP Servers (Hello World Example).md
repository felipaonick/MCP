# 🌦️ Creare un MCP Server in Python – Weather MCP (Part 1)

---

## 🎯 Obiettivo

- Comprendere come **scrivere un MCP server da zero**
- Imparare a **esporre tools e risorse** tramite la libreria `fastmcp`
- Analizzare il caso d’uso di un **weather server** scritto in Python

---

## 🔍 Cosa può esporre un MCP Server

1. **Resources**: aggiungono contesto ai LLM (es. file, PDF, API, documenti)  
2. **Functions (Tools)**: chiamate che eseguono codice (approvabili manualmente o automaticamente)  
3. **Prompts**: template di prompt dinamici con variabili

---

## 🛠️ Prerequisiti

- Python ≥ 3.10 installato  
- MCP SDK Python (`fastmcp`)  
- Libreria `httpx` per richieste HTTP

---

## 📁 Setup del progetto

1. **Crea la directory**:
   ```bash
   # Create a new directory for our project
   uv init weather
   cd weather
   ```

2. **Attiva un ambiente virtuale**:
   ```bash
   # Create virtual environment and activate it
   uv venv
   .venv\Scripts\activate
   ```

3. **Installa le dipendenze**:
   ```bash
   uv add mcp[cli] httpx
   ```

4. **Crea il file principale**:
   ```bash
   # Create our server file   
   new-item weather.py
   ```

---

## 📦 File `pyproject.toml`

Contiene:
- Nome progetto
- Dipendenze
- Entry point (`weather.py`)
- Funzione `main()` da eseguire

---

## 🔧 Architettura del server

```python
from mcp.server.fastmcp import FastMCP
import httpx
```

### 1. **Inizializzazione del server**
```python
mcp = FastMCP("weather")
```

### 2. **Costanti**
```python
# API completamente free
NWS_API_BASE = "https://api.weather.gov"
# la richiesta che viene da weather-app
USER_AGENT = "weather-app/1.0"
```


Ora abbiamo solamente inizializzato il MCP Server. Vogliamo aggiungerli le capacità di fare richieste per ottenere il meteo e vogliamo etichettare questa funzionalità di ottenere il meteo come **tool** che forniremo poi all'LLM.

---

# Creazione di un Server MCP con Funzionalità di Previsioni Meteorologiche 🌦️ (Part 2)

## Introduzione 💡

In questa sezione, esploreremo come costruire un **server MCP** (Model Context Protocol) per esporre funzionalità relative al servizio meteo, in particolare per ottenere **previsioni meteorologiche** e **allarmi meteo** da un'API di servizio esterno (National Weather Service - NWS). Creeremo due strumenti (tools) che possono essere utilizzati da un **client MCP** per ottenere previsioni e allarmi meteo.

---

## Funzioni di Supporto 🔧

### 1. **Funzione `make_aws_request` 🌐**

Questa funzione è un **coroutine** (funzione asincrona) che riceve un URL e fa una richiesta HTTP usando un **client HTTP asincrono** per comunicare con l'API del National Weather Service. Il suo scopo è recuperare i dati dal servizio meteo.

* **Funzionalità**: Esegue una richiesta HTTP all'API del National Weather Service (NWS).
* **Risultato**: Restituisce una risposta che contiene i dati meteo richiesti.

```python
async def make_nws_request(url: str) -> dict[str, Any] | None:
    """Make a request to the NWS API with proper error handling."""
    headers = {
        "User-Agent": USER_AGENT,
        "Accept": "application/geo+json"
    }
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url, headers=headers, timeout=30.0)
            response.raise_for_status()
            return response.json()
        except Exception:
            return None
```

### 2. **Funzione `format_alert` 📃**

La funzione `format_alert` si occupa di formattare i dati ricevuti dal servizio meteo in un formato più leggibile per l'utente o per l'elaborazione successiva da parte del modello.

* **Input**: Un dizionario contenente le informazioni ricevute dal NWS (ad esempio, un allarme meteo).
* **Output**: Una stringa formattata che include eventi, gravità, descrizione e istruzioni.

```python
def format_alert(feature: dict) -> str:
    """Format an alert feature into a readable string."""
    props = feature["properties"]
    return f"""
Event: {props.get('event', 'Unknown')}
Area: {props.get('areaDesc', 'Unknown')}
Severity: {props.get('severity', 'Unknown')}
Description: {props.get('description', 'No description available')}
Instructions: {props.get('instruction', 'No specific instructions provided')}
"""
```

---

## Esposizione degli Strumenti (Tools) tramite MCP 🔧

### 1. **Strumento `get_forecast` 🌤️**

Questo strumento espone la funzionalità di ottenere una **previsione meteo** per una specifica **latitudine e longitudine**.

#### Funzionamento:

* **Decoratore**: Utilizza il decoratore `@mpc.tool()` fornito da MCP che abbiamo inizializzato (mcp).
* **Descrizione**: Fornisce una descrizione dettagliata della funzionalità, come "Ottieni previsioni meteo per una posizione".
* **Argomenti**: Richiede **latitudine** e **longitudine**.
* **Implementazione**: Fa una richiesta HTTP per ottenere i dati meteo e restituisce informazioni come temperatura, vento, previsione e periodo di validità.

#### Dettaglio Importante:

* La descrizione di questa funzione è cruciale per far sì che il **client MCP** sappia se questa funzione può essere invocata o meno. Una descrizione precisa aiuta l'LM (Language Model) a capire meglio quando chiamare questa funzione.

```python
@mcp.tool()
async def get_forecast(latitude: float, longitude: float) -> str:
    """Get weather forecast for a location.

    Args:
        latitude: Latitude of the location
        longitude: Longitude of the location
    """
    # First get the forecast grid endpoint
    points_url = f"{NWS_API_BASE}/points/{latitude},{longitude}"
    points_data = await make_nws_request(points_url)

    if not points_data:
        return "Unable to fetch forecast data for this location."

    # Get the forecast URL from the points response
    forecast_url = points_data["properties"]["forecast"]
    forecast_data = await make_nws_request(forecast_url)

    if not forecast_data:
        return "Unable to fetch detailed forecast."

    # Format the periods into a readable forecast
    periods = forecast_data["properties"]["periods"]
    forecasts = []
    for period in periods[:5]:  # Only show next 5 periods
        forecast = f"""
{period['name']}:
Temperature: {period['temperature']}°{period['temperatureUnit']}
Wind: {period['windSpeed']} {period['windDirection']}
Forecast: {period['detailedForecast']}
"""
        forecasts.append(forecast)

    return "\n---\n".join(forecasts)
```

### 2. **Strumento `get_alerts` ⚠️**

Questo strumento espone la funzionalità di ottenere **allarmi meteo** per una determinata area geografica degli Stati Uniti (ad esempio, New York, California, ecc.).

#### Funzionamento:

* **Decoratore**: Come per `get_forecast`, si usa il decoratore `@mcp.tool()`.
* **Descrizione**: Descrive come ottenere allarmi meteo per uno stato specifico degli USA.
* **Implementazione**: Fa una richiesta API per ottenere gli allarmi e li formatta in una stringa leggibile.

```python
@mcp.tool()
async def get_alerts(state: str) -> str:
    """Get weather alerts for a US state.

    Args:
        state: Two-letter US state code (e.g. CA, NY)
    """
    url = f"{NWS_API_BASE}/alerts/active/area/{state}"
    data = await make_nws_request(url)

    if not data or "features" not in data:
        return "Unable to fetch alerts or no alerts found."

    if not data["features"]:
        return "No active alerts for this state."

    alerts = [format_alert(feature) for feature in data["features"]]
    return "\n---\n".join(alerts)
```

---

## Esecuzione del Server MCP 🖥️

### 1. **Creazione del Server MCP** 🏠

Il server MCP è creato utilizzando l'oggetto `MCPServer` con le due funzioni decorate come strumenti (tools):

* **Strumenti Esposti**: `get_forecast` e `get_alerts`.
* **Decoratori**: Le funzioni vengono decorate con `@tool` per essere esposte al client MCP.

### 2. **Esecuzione del Server** 🏃‍♂️

Una volta che il server è configurato, si esegue con:

* **MCP Run**: Viene utilizzato il comando `mcp.run()` per avviare il server.
* **Trasporto**: La comunicazione tra il client e il server avviene tramite **stdin** (standard input/output), questo significa che l'intera comunicazione tra il client ed il Server MCP avviene via standard input/output channel.

```python
if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport='stdio')
```

#### Passaggi per l'Esecuzione:

1. **Installa tutte le dipendenze** necessarie nel tuo ambiente di sviluppo.
2. **Esegui lo script** `weather.py`, che avvierà il server con le funzionalità (tools) esposte. In questo caso abbiamno un server che espone 2 tools.

---

## Come Connettersi al Server MCP 📡

### 1. **Connessione del Client al server MCP** 🌐

Il Server MCP si esegue localmente. Per collegare un client MCP (come Claude Desktop) al server MCP, è necessario configurare il client per sapere come eseguire il server. Il file di configurazione del client deve includere il nome del server (ad esempio, "weather") e il comando per eseguire il server, ad esempio:

```json
{
    "mcpServers": {
        "weather": {
            "command": "uv",
            "args": [
                "--directory",
                "/ABSOLUTE/PATH/TO/PARENT/FOLDER/weather",
                "run",
                "weather.py"
            ]
        }
    }
}
```

Questo JSON dice: 
- Abbiamo un MCP Server che si chiama "weather" e quindi si forniscono anche i comandi e argomenti per eseguirlo

### 2. **Configurazione per Cloud e Hosting** ☁️

Se desideri ospitare il server su un **cloud** (ad esempio AWS), devi configurare correttamente il server. In alternativa, puoi anche eseguire il server localmente, come visto in precedenza.

---

## Conclusioni 🎯

In questa sezione, abbiamo esplorato come costruire un semplice server MCP che espone **funzionalità meteo** tramite API:

* **Strumenti Esposti**: Abbiamo esposto strumenti per ottenere previsioni meteo e allarmi meteo.
* **Decoratori MCP**: Abbiamo utilizzato il decoratore `@tool` per esporre le funzioni come strumenti al client MCP.
* **Esecuzione del Server**: Abbiamo visto come eseguire il server e configurare il client per connettersi ad esso.

Questa è una base solida per creare applicazioni che espongono funzionalità tramite il protocollo **MCP**, utile per l'integrazione con altri sistemi. 🚀



