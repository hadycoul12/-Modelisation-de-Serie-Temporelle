from fastapi import FastAPI, HTTPException, Query
from fastapi.responses import JSONResponse
from pymongo import MongoClient
import uvicorn

app = FastAPI(title="Movies API", description="API pour MongoDB Mflix", version="1.0")

MONGODB_URL = "mongodb+srv://hadycoul:8TLd9gSHlT17bzpc@cluster0.hulxfud.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(MONGODB_URL)
db = client["sample_mflix"]
collection = db["movies"]

def serialize(doc):
    doc["_id"] = str(doc["_id"])
    return doc

@app.get("/")
def hello():
    return {"message": "Bienvenue sur l'API MongoDB des films 🎬"}

@app.get("/movies/")
def get_movies():
    movies = list(collection.find().limit(10))
    return [serialize(m) for m in movies]

@app.get("/movies/count/")
def count_movies():
    count = collection.count_documents({})
    return {"total_movies": count}

@app.get("/movies/sort_by_genre/")
def get_movies_by_genre(genres_to_search: str):
    results = list(collection.find({"genres": genres_to_search}).limit(10))
    return [serialize(m) for m in results]

@app.get("/movies/sort_by_year/")
def get_movies_by_year(year: int = Query(...)):
    results = list(collection.find({"year": year}).limit(10))
    return [serialize(m) for m in results]

@app.get("/movies/sort_by_genre_and_year/")
def get_movies_by_genre_and_year(genres_to_search: str, year: int):
    query = {"genres": genres_to_search, "year": year}
    results = list(collection.find(query).limit(10))
    return [serialize(m) for m in results]

@app.get("/movies/directors/")
def get_unique_directors():
    directors = collection.distinct("directors")
    return {"directors": directors, "count": len(directors)}

@app.get("/movies/{movie_title}")
def get_movie_by_title(movie_title: str):
    movie = collection.find_one({"title": movie_title})
    if not movie:
        raise HTTPException(status_code=404, detail="Film non trouvé")
    return serialize(movie)

@app.get("/info")
def get_info():
    return {
        "project": "TP4 FastAPI + MongoDB",
        "description": "API pour interroger la base de films",
        "version": "1.0",
        "endpoints": [
            "/movies/",
            "/movies/count/",
            "/movies/sort_by_genre/",
            "/movies/sort_by_year/",
            "/movies/sort_by_genre_and_year/",
            "/movies/directors/",
            "/movies/{movie_title}",
            "/info",
            "/statistics"
        ]
    }

@app.get("/statistics")
def get_statistics():
    pipeline = [
        {"$match": {"runtime": {"$type": "int"}}},
        {"$group": {"_id": None, "average_runtime": {"$avg": "$runtime"}}}
    ]
    result = list(collection.aggregate(pipeline))
    if result:
        return {"average_runtime": round(result[0]["average_runtime"], 2)}
    return {"message": "Pas de données de durée disponibles"}
