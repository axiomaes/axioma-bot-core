# Axioma Bot Core

Backend microservice for Axioma's multi-tenant AI agent engine.

## Features
- **FastAPI** REST API
- **LangGraph** based agent workflows
- **Multi-tenant** support via configuration
- **Integrations**: Chatwoot, Axioma Core, n8n
- **LLM Support**: OpenAI, Anthropic, Ollama

## Requirements
- Python 3.11+
- Docker (for deployment)

## Local Development

1.  **Clone the repository**
2.  **Create a virtual environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```
3.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
4.  **Configure Environment**:
    Create a `.env` file based on your requirements (see `app/config/settings.py`).
    ```env
    OPENAI_API_KEY=sk-...
    CHATWOOT_API_TOKEN=...
    CHATWOOT_BASE_URL=...
    ```
5.  **Run the service**:
    ```bash
    make run
    ```
    Service will be available at `http://localhost:8000`.

## Testing

Run tests using pytest:
```bash
make test
```

## Deployment (CapRover)

The project includes a `Dockerfile` optimized for CapRover.

1.  Create a new app in CapRover.
2.  Set the Container Port to `80`.
3.  Deploy using CaptainDuckDuck CLI or Git Webhook.
4.  Set Environment Variables in the App Config on CapRover dashboard.

## Dashboard UI

El proyecto incluye un dashboard en tiempo real para visualizar las ejecuciones de los flujos.

### Ejecución Local

1.  **Backend**: Asegúrate de que el backend esté corriendo (`make run`).
2.  **Frontend**: Navega a la carpeta `dashboard` e inicia la aplicación.
    ```bash
    cd dashboard
    npm install
    npm run dev
    ```
3.  Abre `http://localhost:5173` en tu navegador.

### Despliegue en CapRover

El dashboard tiene su propio `Dockerfile` en el directorio `dashboard/`. Para desplegarlo:
1.  Crea una nueva App en CapRover (ej. `axioma-bot-dashboard`).
2.  Despliega usando el Dockerfile de la carpeta `dashboard`.
3.  Configura la variable de entorno `VITE_API_URL` apuntando a tu backend (ej. `https://axioma-bot-core.tu-dominio.com`).

## Bitácora del Proyecto

2026-01-28 – Inicio del proyecto y estructura base
Se ha creado la estructura de carpetas del microservicio "axioma-bot-core" y se han generado los archivos de configuración iniciales (Dockerfile, Makefile, requirements.txt). Se implementó LangGraph como motor de agentes y se configuró el enrutamiento multi-tenant.

2026-01-28 – Configuración de proveedores y herramientas
Se añadieron las abstracciones para proveedores de LLM (OpenAI, Anthropic, Ollama) y los wrappers para herramientas externas (Chatwoot, Axioma Core, n8n). Se crearon los endpoints básicos de la API (webhook y healthcheck) y se definieron los esquemas de datos.

2026-01-28 – Implementación del Dashboard
Se desarrolló una interfaz gráfica con React y Vite para la visualización de ejecuciones en tiempo real. Se añadieron nuevos endpoints al backend para exponer datos de ejecuciones, clientes y workflows, además de habilitar CORS. El sistema ahora permite inspeccionar el trazo paso a paso de cada ejecución del agente.

<!-- Próximas entradas aquí -->
