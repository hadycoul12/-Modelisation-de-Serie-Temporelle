import requests

base_url = "http://localhost:4000"

def afficher_menu():
    print("\n🤖 Bienvenue dans le chatbot API Movies !")
    print("1 - Dire Hello (/)")
    print("2 - Lister 10 premiers films (/movies/)")
    print("3 - Compter les films (/movies/count/)")
    print("4 - Chercher par genre (/movies/sort_by_genre/)")
    print("5 - Chercher par année (/movies/sort_by_year/)")
    print("6 - Chercher par genre + année (/movies/sort_by_genre_and_year/)")
    print("7 - Lister les réalisateurs (/movies/directors/)")
    print("8 - Détails d’un film (/movies/{title})")
    print("9 - Infos API (/info)")
    print("10 - Statistiques (/statistics)")
    print("0 - Quitter")

def get_json(endpoint, params=None):
    try:
        response = requests.get(f"{base_url}{endpoint}", params=params)
        if response.status_code == 200:
            return response.json()
        else:
            print("❌ Erreur:", response.status_code, response.text)
    except Exception as e:
        print("🚨 Exception :", e)

def chatbot():
    while True:
        afficher_menu()
        choix = input("Votre choix : ")

        if choix == "0":
            print("👋 Au revoir !")
            break

        elif choix == "1":
            print(get_json("/"))

        elif choix == "2":
            data = get_json("/movies/")
            for movie in data:
                print("-", movie.get("title"))

        elif choix == "3":
            print(get_json("/movies/count/"))

        elif choix == "4":
            genre = input("Genre ? : ")
            data = get_json("/movies/sort_by_genre/", {"genres_to_search": genre})
            for movie in data:
                print("-", movie.get("title"))

        elif choix == "5":
            year = input("Année ? : ")
            data = get_json("/movies/sort_by_year/", {"year": year})
            for movie in data:
                print("-", movie.get("title"))

        elif choix == "6":
            genre = input("Genre ? : ")
            year = input("Année ? : ")
            data = get_json("/movies/sort_by_genre_and_year/", {"genres_to_search": genre, "year": year})
            for movie in data:
                print("-", movie.get("title"))

        elif choix == "7":
            data = get_json("/movies/directors/")
            print("🎬 Réalisateurs :", data["count"])
            for d in data["directors"][:10]:
                print("-", d)

        elif choix == "8":
            title = input("Titre du film : ")
            data = get_json(f"/movies/{title}")
            if data:
                print("🎬", data.get("title"))
                print("📅", data.get("year"))
                print("🎞️", data.get("genres"))
                print("🎬", data.get("directors"))

        elif choix == "9":
            print(get_json("/info"))

        elif choix == "10":
            print(get_json("/statistics"))

        else:
            print("⚠️ Choix invalide.")

if __name__ == "__main__":
    chatbot()
