from fastapi import FastAPI

app = FastAPI(
    title="WhatsApp Business Platform API",
    version="0.1.0",
)


@app.get("/")
def root():
    return {
        "message": "WhatsApp Business Platform API is running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }
