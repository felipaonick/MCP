# Creazione di un Server MCP con TypeScript per il Servizio Meteo 🌦️

## Introduzione 💡

IN maniera del tutto simile a quanto abbiamo già fatto con Python, in questa sezione, esploreremo i passaggi necessari per costruire un **server MCP** (Model Context Protocol) utilizzando **TypeScript**. Il server esporrà due strumenti: uno per ottenere **previsioni meteo** e uno per ottenere **allarmi meteo** per una specifica area geografica.

---

## Passaggi di Installazione 🛠️

### 1. **Installazione di Node.js e npm** 🌐

Per prima cosa, assicurati di avere **Node.js** e **npm** installati nel tuo sistema.

```bash
node --version
npm --version
```

### 2. **Creazione di un Nuovo Progetto** 📂

Crea una nuova cartella chiamata **weather** e inizializzala come un nuovo progetto:

```bash
# Create a new directory for our project
md weather
cd weather

# Initialize a new npm project
npm init -y
```

### 3. **Installazione delle Dipendenze** 📦

Installa le seguenti dipendenze:

* **NCP SDK** per l'interazione con l'API di MCP.
* **TypeScript** per lo sviluppo del server.

```bash
# Install dependencies
npm install @modelcontextprotocol/sdk zod
npm install -D @types/node typescript

# Create our files
md src
new-item src\index.ts
```

### 4. **Update package.json e Configurazione del Progetto TypeScript** 🔧

Aggiorniamo il package.json aggiungendo il type: "module" e lo script di costruzione, in questo modo gli diciamo come costruire la nostra applicazione
per costruilra con TypeScipt:

```json
{
  "type": "module",
  "bin": {
    "weather": "./build/index.js"
  },
  "scripts": {
    "build": "tsc && chmod 755 build/index.js"
  },
  "files": [
    "build"
  ],
}
```

Configura **TypeScript** creando il file `tsconfig.json`:

```json
{
  "compilerOptions": {
    "target": "ES2022",
    "module": "Node16",
    "moduleResolution": "Node16",
    "outDir": "./build",
    "rootDir": "./src",
    "strict": true,
    "esModuleInterop": true,
    "skipLibCheck": true,
    "forceConsistentCasingInFileNames": true
  },
  "include": ["src/**/*"],
  "exclude": ["node_modules"]
}
```

---

## Creazione del Server MCP 🌍

### 1. **File del Server (`index.ts`)** 📝

Crea il file **`index.ts`** nella cartella **`src`**:

```bash
touch src/index.ts
```

### 2. **Importiamo i packages ed impostiamo le istanze** 🌐


```typescript
import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
import { StdioServerTransport } from "@modelcontextprotocol/sdk/server/stdio.js";
import { z } from "zod";

const NWS_API_BASE = "https://api.weather.gov";
const USER_AGENT = "weather-app/1.0";

// Create server instance
const server = new McpServer({
  name: "weather",
  version: "1.0.0",
  capabilities: {
    resources: {},
    tools: {},
  },
});
```
---

## Funzioni di Supporto 🔧

### 1. **Funzione `makeNWSRequest`** 🌐

Questa funzione è responsabile di fare una richiesta HTTP asincrona al servizio meteo:

```typescript
// Helper function for making NWS API requests
async function makeNWSRequest<T>(url: string): Promise<T | null> {
  const headers = {
    "User-Agent": USER_AGENT,
    Accept: "application/geo+json",
  };

  try {
    const response = await fetch(url, { headers });
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    return (await response.json()) as T;
  } catch (error) {
    console.error("Error making NWS request:", error);
    return null;
  }
}

interface AlertFeature {
  properties: {
    event?: string;
    areaDesc?: string;
    severity?: string;
    status?: string;
    headline?: string;
  };
}
```

### 2. **Formato di Allarme** ⚠️

La funzione `formatAlert` prende un oggetto di allarme e lo formatta in una stringa leggibile:

```typescript
// Format alert data
function formatAlert(feature: AlertFeature): string {
  const props = feature.properties;
  return [
    `Event: ${props.event || "Unknown"}`,
    `Area: ${props.areaDesc || "Unknown"}`,
    `Severity: ${props.severity || "Unknown"}`,
    `Status: ${props.status || "Unknown"}`,
    `Headline: ${props.headline || "No headline"}`,
    "---",
  ].join("\n");
}

interface ForecastPeriod {
  name?: string;
  temperature?: number;
  temperatureUnit?: string;
  windSpeed?: string;
  windDirection?: string;
  shortForecast?: string;
}

interface AlertsResponse {
  features: AlertFeature[];
}

interface PointsResponse {
  properties: {
    forecast?: string;
  };
}

interface ForecastResponse {
  properties: {
    periods: ForecastPeriod[];
  };
}
```

---

## Esposizione degli Strumenti tramite MCP 🔧

### 1. **Strumento `getAlerts` ⚠️**

Espone la funzionalità di ottenere **allarmi meteo** per uno stato degli USA. La funzione utilizza il decoratore `@tool` per renderla accessibile tramite il client MCP:

```typescript
server.tool(
  "get-alerts",
  "Get weather alerts for a state",
  {
    state: z.string().length(2).describe("Two-letter state code (e.g. CA, NY)"),
  },
  async ({ state }) => {
    const stateCode = state.toUpperCase();
    const alertsUrl = `${NWS_API_BASE}/alerts?area=${stateCode}`;
    const alertsData = await makeNWSRequest<AlertsResponse>(alertsUrl);

    if (!alertsData) {
      return {
        content: [
          {
            type: "text",
            text: "Failed to retrieve alerts data",
          },
        ],
      };
    }

    const features = alertsData.features || [];
    if (features.length === 0) {
      return {
        content: [
          {
            type: "text",
            text: `No active alerts for ${stateCode}`,
          },
        ],
      };
    }

    const formattedAlerts = features.map(formatAlert);
    const alertsText = `Active alerts for ${stateCode}:\n\n${formattedAlerts.join("\n")}`;

    return {
      content: [
        {
          type: "text",
          text: alertsText,
        },
      ],
    };
  },
);
```

### 2. **Strumento `getForecast` 🌤️**

Espone la funzionalità di ottenere una **previsione meteo** per una specifica **latitudine** e **longitudine**:

```typescript
server.tool(
  "get-forecast",
  "Get weather forecast for a location",
  {
    latitude: z.number().min(-90).max(90).describe("Latitude of the location"),
    longitude: z.number().min(-180).max(180).describe("Longitude of the location"),
  },
  async ({ latitude, longitude }) => {
    // Get grid point data
    const pointsUrl = `${NWS_API_BASE}/points/${latitude.toFixed(4)},${longitude.toFixed(4)}`;
    const pointsData = await makeNWSRequest<PointsResponse>(pointsUrl);

    if (!pointsData) {
      return {
        content: [
          {
            type: "text",
            text: `Failed to retrieve grid point data for coordinates: ${latitude}, ${longitude}. This location may not be supported by the NWS API (only US locations are supported).`,
          },
        ],
      };
    }

    const forecastUrl = pointsData.properties?.forecast;
    if (!forecastUrl) {
      return {
        content: [
          {
            type: "text",
            text: "Failed to get forecast URL from grid point data",
          },
        ],
      };
    }

    // Get forecast data
    const forecastData = await makeNWSRequest<ForecastResponse>(forecastUrl);
    if (!forecastData) {
      return {
        content: [
          {
            type: "text",
            text: "Failed to retrieve forecast data",
          },
        ],
      };
    }

    const periods = forecastData.properties?.periods || [];
    if (periods.length === 0) {
      return {
        content: [
          {
            type: "text",
            text: "No forecast periods available",
          },
        ],
      };
    }

    // Format forecast periods
    const formattedForecast = periods.map((period: ForecastPeriod) =>
      [
        `${period.name || "Unknown"}:`,
        `Temperature: ${period.temperature || "Unknown"}°${period.temperatureUnit || "F"}`,
        `Wind: ${period.windSpeed || "Unknown"} ${period.windDirection || ""}`,
        `${period.shortForecast || "No forecast available"}`,
        "---",
      ].join("\n"),
    );

    const forecastText = `Forecast for ${latitude}, ${longitude}:\n\n${formattedForecast.join("\n")}`;

    return {
      content: [
        {
          type: "text",
          text: forecastText,
        },
      ],
    };
  },
);
```

---

## Esecuzione del Server MCP 🏃‍♂️

### 1. **Funzione Main per Avviare il Server** 🚀

Crea una funzione principale che utilizza il trasporto standard di input/output (`stdio`):

```typescript
async function main() {
  const transport = new StdioServerTransport();
  await server.connect(transport);
  console.error("Weather MCP Server running on stdio");
}

main().catch((error) => {
  console.error("Fatal error in main():", error);
  process.exit(1);
});
```

---

## Come Eseguire il Server ⚙️

### 1. **Comando di Esecuzione** 🖥️

Per avviare il server, esegui il seguente comando:

```bash
npx tsc
node dist/index.js
```

Questo compila il progetto TypeScript e avvia il server.

---

## Integrazione con un Client MCP 📡

### 1. **Configurazione del Client** 🌍

Per connettersi al server MCP, configura il client con le informazioni appropriate (come il nome del server e il comando di esecuzione). Questo consente al client di interagire con il server per ottenere le previsioni e gli allarmi meteo.


### 2. **Esecuzione del Server nel Cloud** ☁️

Se desideri eseguire il server nel cloud (es. su **AWS**), dovrai configurare l'ambiente di hosting, come spiegato in precedenza, e avviare il server da lì.

---

## Conclusione 🎯

In questa sezione, abbiamo creato un **server MCP** utilizzando **TypeScript** che espone due strumenti:

* **`get_forecast`**: Ottieni le previsioni meteo per una posizione specifica.
* **`get_alerts`**: Ottieni gli allarmi meteo per uno stato.

Abbiamo visto come configurare il server, esporre gli strumenti e connetterlo a un **client MCP** per interagire con esso. 🚀


