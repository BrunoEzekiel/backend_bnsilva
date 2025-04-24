from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Configura CORS para seu frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # URL exata do seu front
    allow_methods=["*"],  # Métodos HTTP permitidos
    allow_credentials=True,
    allow_headers=["*"]
)

# Rota de teste
@app.get("/api")
def home():
    return {"message": "Backend rodando!"}

# Rota para integrar com o frontend
@app.get("/api/hello")
def hello(name: str = "Bruno"):
    return {"message": f"Olá, {name}! Sou o backend Python."}

@app.get("/api/hello2")
def hello2(name: str = None):
    if name:
        return {"message": f"oi, {name}! voce vai aprender."}
    