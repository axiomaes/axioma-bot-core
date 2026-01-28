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

## Bitácora del Proyecto

2026-01-28 – Inicio del proyecto y estructura base
Se ha creado la estructura de carpetas del microservicio "axioma-bot-core" y se han generado los archivos de configuración iniciales (Dockerfile, Makefile, requirements.txt). Se implementó LangGraph como motor de agentes y se configuró el enrutamiento multi-tenant.

2026-01-28 – Configuración de proveedores y herramientas
Se añadieron las abstracciones para proveedores de LLM (OpenAI, Anthropic, Ollama) y los wrappers para herramientas externas (Chatwoot, Axioma Core, n8n). Se crearon los endpoints básicos de la API (webhook y healthcheck) y se definieron los esquemas de datos.

<!-- Próximas entradas aquí -->
