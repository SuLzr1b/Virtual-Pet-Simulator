import os
import random

PET_FILE = "pet.txt"

def load_pet():
    if os.path.exists(PET_FILE):
        with open(PET_FILE, "r") as f:
            line = f.readline().strip()
            parts = line.split("|")
            if len(parts) >= 8:
                return {
                    "nome": parts[0],
                    "tipo": parts[1],
                    "fome": int(parts[2]),
                    "felicidade": int(parts[3]),
                    "energia": int(parts[4]),
                    "higiene": int(parts[5]),
                    "disciplina": int(parts[6]),
                    "truques": parts[7].split(",") if parts[7] else [],
                    "inventario": parts[8].split(",") if len(parts) > 8 and parts[8] else []
                }
    return None
    
def save_pet(pet):
    truques = ",".join(pet["truques"]) if pet["truques"] else ""
    inventario = ",".join(pet["inventario"]) if pet["inventario"] else ""
    with open(PET_FILE, "w") as f:
        f.write(f"{pet['nome']}|{pet['tipo']}|{pet['fome']}|{pet['felicidade']}|{pet['energia']}|{pet['higiene']}|{pet['disciplina']}|{truques}|{inventario}\n")

def create_pet(nome, tipo="dragon"):
    return {
        "nome": nome,
        "tipo": tipo,
        "fome": 50,
        "felicidade": 50,
        "energia": 50,
        "higiene": 50,
        "disciplina": 0,
        "truques": [],
        "inventario": []
    }

def update_status(pet):
    pet["fome"] = min(100, pet["fome"] + 5)
    pet["felicidade"] = max(0, pet["felicidade"] - 5)
    pet["energia"] = max(0, pet["energia"] - 5)
    pet["higiene"] = max(0, pet["higiene"] - 5)
    save_pet(pet)

def feed_dragon(pet):
    pet["fome"] = max(0, pet["fome"] - 20)
    pet["felicidade"] = min(100, pet["felicidade"] + 10)
    pet["fome"] = min(100, pet["fome"] + 10)  # Dragões comem muito
    save_pet(pet)
    return f"{pet['nome']} devorou um banquete de carne!"

def play_dragon(pet):
    if pet["energia"] > 10:
        pet["fome"] = min(100, pet["fome"] + 5)
        pet["felicidade"] = min(100, pet["felicidade"] + 20)  # Dragões adoram ação
        pet["energia"] = max(0, pet["energia"] - 10)
        pet["higiene"] = max(0, pet["higiene"] - 20)
        items = ["joia", "tocha", "escama", "submarino do ibere"]
        if random.random() < 0.3:
            item = random.choice(items)
            pet["inventario"].append(item)
            save_pet(pet)
            return f"{pet['nome']} voou e cuspiu fogo! Encontrou um {item}!"
        save_pet(pet)
        return f"{pet['nome']} voou e cuspiu fogo!"
    return f"{pet['nome']} está muito cansado para brincar."

def sleep_dragon(pet):
    pet["fome"] = min(100, pet["fome"] + 10)
    pet["energia"] = min(100, pet["energia"] + 30)
    pet["higiene"] = max(0, pet["higiene"] - 20)
    save_pet(pet)
    return f"{pet['nome']} dormiu na caverna!"

def shower_dragon(pet):
    pet["felicidade"] = min(100, pet["felicidade"] + 10)
    pet["higiene"] = min(100, pet["higiene"] + 30)
    save_pet(pet)
    return f"{pet['nome']} brilhou suas escamas!"

def talk_dragon(pet):
    messages = ["Rugido!", "Fogo, fogo!", "Sou o rei dos céus!"]
    message = random.choice(messages)
    return f"{pet['nome']} ruge: {message}"

def carinho_dragon(pet):
    pet["felicidade"] = min(100, pet["felicidade"] + 20)
    save_pet(pet)
    return f"{pet['nome']} gostou do carinho nas escamas!"

def trick_dragon(pet):
    possible_tricks = ["cuspir fogo", "voar em círculos", "rosnar alto", "esconder tesouro"]
    available_tricks = [trick for trick in possible_tricks if trick not in pet["truques"]]
    if available_tricks:
        trick = random.choice(available_tricks)
        pet["truques"].append(trick)
        pet["felicidade"] = min(100, pet["felicidade"] + 10)
        pet["disciplina"] = min(100, pet["disciplina"] + 20)
        save_pet(pet)
        return f"{pet['nome']} aprendeu a {trick}!"
    return f"{pet['nome']} já sabe todos os truques!"

def petisco_dragon(pet):
    pet["fome"] = max(0, pet["fome"] - 10)
    pet["felicidade"] = min(100, pet["felicidade"] + 10)
    save_pet(pet)
    return f"{pet['nome']} devorou um petisco flamejante!"

def song_dragon(pet):
    songs = [
        "RUGIDO, EU SOU O MAIOR",
        "VOO ALTO, QUEIMO TUDO",
        "NAS NUVENS, SOU O REI",
        "FOGO E GLORIA, VEM COMIGO",
        "RAR RAR, DOMINO O CÉU"
    ]
    song = random.choice(songs)
    return f"{pet['nome']} está rugindo: {song}"

def show_inventory_dragon(pet):
    if pet["inventario"]:
        return f"{pet['nome']} tem: {', '.join(pet['inventario'])}"
    return f"{pet['nome']} não tem nada no inventário."

def get_pet_message(pet):
    if pet["fome"] > 90:
        return f"{pet['nome']} está com muita fome!"
    elif pet["felicidade"] < 20:
        return f"{pet['nome']} está triste... precisa voar!"
    elif pet["energia"] < 20:
        return f"{pet['nome']} está exausto, precisa dormir!"
    elif pet["higiene"] < 10:
        return f"{pet['nome']} está sujo, precisa polir as escamas!"
    return f"{pet['nome']} está feliz e saudável!"
