from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Configura CORS para seu frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://bnsilva.vercel.app"],  # URL exata do seu front
    allow_methods=["GET", "POST"],
    allow_headers=["*"]
)

@app.get("/api/status")
def status():
    return {"status": "online", "framework": "FastAPI"}

@app.get("/api/echo/{message}")
def echo(message: str):
    return {"original": message, "processed": message.upper()}gla