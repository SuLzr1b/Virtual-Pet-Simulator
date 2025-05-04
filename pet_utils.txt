import os
import random

PET_FILE = "pet.txt"

def load_pet():
    if os.path.exists(PET_FILE):
        with open(PET_FILE, "r") as f:
            line = f.readline().strip()
            parts = line.split("|")
            nome, fome, felicidade, energia, higiene = parts[:5]
            disciplina = int(parts[5]) if len(parts) > 5 else 0
            truques = parts[6].split(",") if len(parts) > 6 and parts[6] else []
            inventario = parts[7].split(",") if len(parts) > 7 and parts[7] else []
            return {
                "nome": nome,
                "fome": int(fome),
                "felicidade": int(felicidade),
                "energia": int(energia),
                "higiene": int(higiene),
                "disciplina": disciplina,
                "truques": truques,
                "inventario": inventario
            }
    return None
    
def save_pet(pet):
    truques = ",".join(pet["truques"]) if pet["truques"] else ""
    with open(PET_FILE, "w") as f:
        f.write(f"{pet['nome']}|{pet['fome']}|{pet['felicidade']}|{pet['energia']}|{pet['higiene']}|{pet['disciplina']}|{truques}|{'inventario'}\n")

def create_pet(nome):
    return {
        "nome": nome,
        "fome": 50,
        "felicidade": 50,
        "energia": 50,
        "higiene": 50,
        "disciplina": 0,
        "truques": [],
        "inventario": []
    }

def update_status(pet):
    """CONFIGURAÇÃO PADRÃO -> COM O TEMPO AS COISAS VAO AUMENTANDO OU DIMINUINDO"""
    pet["fome"] = min(100, pet["fome"] + 5)  # fome aumenta
    pet["felicidade"] = max(0, pet["felicidade"] - 5)  # felicidade diminui
    pet["energia"] = max(0, pet["energia"] - 5)  # energia diminui
    pet["higiene"] = max(0, pet["higiene"] - 5)  # higiene diminui
    save_pet(pet)

def feed_pet(pet):
    """ALIMENTANDO, REDUZ FOME, AUMENTA FELICIDADE"""
    pet["fome"] = max(0, pet["fome"] - 20)  # fome diminui
    #pet["felicidade"] = min(100, pet["felicidade"] + 10)  # felicidade aumenta
    save_pet(pet)
    return f"{pet['nome']} adorou a comida!"

def play_pet(pet):
    """BRINCANDO, AUMENTA FOME, AUMENTA FELICIDADE, REDUZ ENERGIA, REDUZ HIGIENE"""
    if pet["energia"] > 10:
        pet["fome"] = min(100, pet["fome"] + 5)  # fome aumenta
        pet["felicidade"] = min(100, pet["felicidade"] + 15)  # felicidade aumenta
        pet["energia"] = max(0, pet["energia"] - 10)  # energia diminui
        pet["higiene"] = max(0, pet["higiene"] - 20)  # higiene diminui
        items = ["osso", "bola", "graveto", "submarino do ibere"]
        if random.random() < 0.3:
            item = random.choice(items)
            pet["inventario"].append(item)
            save_pet(pet)
            return f"{pet['nome']} se divertiu bastante! Encontrou um {item}!"
        save_pet(pet)
        return f"{pet['nome']} se divertiu bastante!"
    return f"{pet['nome']} está muito cansado para brincar."

def sleep_pet(pet):
    """DORMINDO, AUMENTA FOME, AUMENTA ENERGIA, REDUZ HIGIENE"""
    pet["fome"] = min(100, pet["fome"] + 10)  # fome aumenta
    pet["energia"] = min(100, pet["energia"] + 30)  # energia aumenta
    pet["higiene"] = max(0, pet["higiene"] - 20)  # higiene diminui
    save_pet(pet)
    return f"{pet['nome']} dormiu e está descansado!"

def shower_pet(pet):
    """BANHO, AUMENTA FELICIDADE, AUMENTA HIGIENE"""
    pet["felicidade"] = min(100, pet["felicidade"] + 10)  # felicidade aumenta
    pet["higiene"] = min(100, pet["higiene"] + 30)  # higiene aumenta
    save_pet(pet)
    return f"{pet['nome']} tomou banho e está cheiroso!"

def talk_pet(pet):
    """FAZ O PET FALAR UMA MENSAGEM ALEATÓRIA SEM ALTERAR STATUS"""
    messages = [
        "Tô de boa!",
        "Me dá um petisco?",
        "O que tá rolando?",
        "Tô na minha!",
        "Que dia legal!",
        "Adoro ficar contigo!"
    ]
    message = random.choice(messages)
    return f"{pet['nome']} diz: {message}"

def carinho_pet(pet):
    """CARINHO, AUMENTA FELICIDADE"""
    pet["felicidade"] = min(100, pet["felicidade"] + 20) # fekicidade aumenta
    save_pet(pet)
    return f"{pet['nome']} amou o carinho hihihi"

def trick_pet(pet):
    """ENSINA UM TRUQUE AO PET, AUMENTA FELICIDADE E DISCIPLINA"""
    possible_tricks = ["sentar", "rolar", "dar a pata", "fingir de morto"]
    available_tricks = [trick for trick in possible_tricks if trick not in pet["truques"]]
    if available_tricks:
        trick = random.choice(available_tricks)
        pet["truques"].append(trick)
        pet["felicidade"] = min(100, pet["felicidade"] + 10) # felicidade aumenta
        pet["disciplina"] = min(100, pet["disciplina"] + 20) # disciplica aumenta
        save_pet(pet)
        return f"{pet['nome']} aprendeu a {trick}!"
    return f"{pet['nome']} já sabe todos os truques!"

def petisco_pet(pet):
    """PETISCO, DIMINUI FOME, AUMENTA FELICIDADE"""
    pet["fome"] = max(0, pet['fome'] - 10) # fome diminui
    pet ["felicidade"] = min(100, pet['felicidade'] + 10) # felicidade aumenta
    save_pet(pet)
    return f"{pet['nome']} saboreou o petisco!"

def song_pet(pet):
    """CANTAR, NAO ALTERA STATUS"""
    songs = [
        "OH GAROTA EU QUERO VOCE SO PRA MIM",
        "TA FAZENDO TUDO QUE EU MANDO",
        "SAO 4 DA MANHA E EU TO NA ESTRADA",
        "BRINCO DE DIAMANTE YEAH",
        "TRALELO TRALALA PUM PUM PAM PAM"
    ]
    song = random.choice(songs)
    return f"{pet['nome']} está cantando: {song}"

def show_inventory(pet):
    """MOSTRA INVENTARIO SEM ALTERAR STATUS"""
    if pet['inventario']:
        return f"{pet['nome']} tem: {', '.join(pet['inventario'])}"
    return f"{pet['nome']} não tem nada no inventário."


def get_pet_message(pet):
    """RETORNA UMA MENSAGEM BASEADA NO ESTADO DO PET"""
    if pet["fome"] > 90:
        return f"{pet['nome']} está com muita fome!"
    elif pet["felicidade"] < 20:
        return f"{pet['nome']} está triste... acho que precisa brincar um pouco!"
    elif pet["energia"] < 20:
        return f"{pet['nome']} está exausto, precisa dormir!"
    elif pet["higiene"] < 10:
        return f"{pet['nome']} está sujo, precisa tomar um banho! D:"
    return f"{pet['nome']} está feliz e saudável!! :)"