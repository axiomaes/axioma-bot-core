from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config.settings import get_settings
from app.api import webhook_controller, healthcheck, dashboard
from app.utils.logger import setup_logger

settings = get_settings()
logger = setup_logger(__name__)

app = FastAPI(title=settings.APP_NAME)

# CORS Configuration
origins = [
    "http://localhost:3000",
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(webhook_controller.router)
app.include_router(healthcheck.router)
app.include_router(dashboard.router)

@app.on_event("startup")
async def startup_event():
    logger.info("Starting up Axioma Bot Core...")

@app.get("/")
async def root():
    return {"message": "Axioma Bot Core is running"}
