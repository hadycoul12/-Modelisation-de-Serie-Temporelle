# TP4 - FastAPI + MongoDB (sample_mflix)

## Installation

```bash
pip install -r requirements.txt
```

## Lancer l'API

```bash
uvicorn main:app --reload --port 4000
```

## Lancer le chatbot

```bash
python chatbot.py
```

## Tester dans le navigateur

- http://localhost:4000
- http://localhost:4000/docs

## Configuration

L'URL de connexion MongoDB Atlas n'est jamais écrite dans le code : définissez-la dans votre environnement avant de lancer l'API.

```bash
# macOS ou Linux
export MONGODB_URL="mongodb+srv://<utilisateur>:<mot_de_passe>@<cluster>.mongodb.net/?retryWrites=true&w=majority"

# Windows (PowerShell)
$env:MONGODB_URL = "mongodb+srv://<utilisateur>:<mot_de_passe>@<cluster>.mongodb.net/?retryWrites=true&w=majority"
```
