import importlib

PET_FILE = "pet.txt"

def show_status(pet, funcoes):
    print("=======================================")
    print(f"\n=== Estado de {pet['nome']} ({pet['tipo']}) ===")
    print(f"Fome: {pet['fome']}")
    print(f"Felicidade: {pet['felicidade']}")
    print(f"Energia: {pet['energia']}")
    print(f"Higiene: {pet['higiene']}")
    print(f"Disciplina: {pet['disciplina']}")
    print(f"Truques: {', '.join(pet['truques']) if pet['truques'] else 'nenhum'}")
    print(f"Inventário: {', '.join(pet['inventario']) if pet['inventario'] else 'vazio'}")
    print(funcoes["get_pet_message"](pet))
    print("=======================================")

def main():
    pet = None
    try:
        pet = importlib.import_module("dog").load_pet()
        if pet is None:
            raise FileNotFoundError
    except (FileNotFoundError, AttributeError):
        print("Bem-vindo ao Virtual Pet!")
        nome = input("Digite o nome do seu pet: ")
        while True:
            print("Escolha o tipo do pet:")
            print("1. Cachorro")
            print("2. Gato")
            print("3. Dragão")
            tipo_escolha = input("Digite o número (1-3): ")
            if tipo_escolha == "1":
                tipo = "dog"
                modulo = importlib.import_module("dog")
                break
            elif tipo_escolha == "2":
                tipo = "cat"
                modulo = importlib.import_module("cat")
                break
            elif tipo_escolha == "3":
                tipo = "dragon"
                modulo = importlib.import_module("dragon")
                break
            print("Opção inválida, tente novamente.")
        pet = modulo.create_pet(nome, tipo)
        modulo.save_pet(pet)

    modulo = importlib.import_module(pet["tipo"])
    funcoes = {
        "feed": modulo.feed_dog if pet["tipo"] == "dog" else modulo.feed_cat if pet["tipo"] == "cat" else modulo.feed_dragon,
        "play": modulo.play_dog if pet["tipo"] == "dog" else modulo.play_cat if pet["tipo"] == "cat" else modulo.play_dragon,
        "sleep": modulo.sleep_dog if pet["tipo"] == "dog" else modulo.sleep_cat if pet["tipo"] == "cat" else modulo.sleep_dragon,
        "shower": modulo.shower_dog if pet["tipo"] == "dog" else modulo.shower_cat if pet["tipo"] == "cat" else modulo.shower_dragon,
        "talk": modulo.talk_dog if pet["tipo"] == "dog" else modulo.talk_cat if pet["tipo"] == "cat" else modulo.talk_dragon,
        "carinho": modulo.carinho_dog if pet["tipo"] == "dog" else modulo.carinho_cat if pet["tipo"] == "cat" else modulo.carinho_dragon,
        "trick": modulo.trick_dog if pet["tipo"] == "dog" else modulo.trick_cat if pet["tipo"] == "cat" else modulo.trick_dragon,
        "petisco": modulo.petisco_dog if pet["tipo"] == "dog" else modulo.petisco_cat if pet["tipo"] == "cat" else modulo.petisco_dragon,
        "song": modulo.song_dog if pet["tipo"] == "dog" else modulo.song_cat if pet["tipo"] == "cat" else modulo.song_dragon,
        "show_inventory": modulo.show_inventory_dog if pet["tipo"] == "dog" else modulo.show_inventory_cat if pet["tipo"] == "cat" else modulo.show_inventory_dragon,
        "get_pet_message": modulo.get_pet_message
    }

    print(f"\nCuide de {pet['nome']}, seu {pet['tipo']}! Use o menu para interagir.")

    while True:
        print("\n==== MENU ====")
        print("1. Alimentar")
        print("2. Brincar")
        print("3. Dormir")
        print("4. Dar banho")
        print("5. Falar")
        print("6. Fazer Carinho")
        print("7. Fazer Truque")
        print("8. Dar Petisco")
        print("9. Cantar")
        print("10. Mostrar Inventário")
        print("11. Ver status")
        print("12. Sair")
        escolha = input("Escolha uma opção (1-12): ")

        if escolha == "1":
            print(funcoes["feed"](pet))
            modulo.update_status(pet)
        elif escolha == "2":
            print(funcoes["play"](pet))
            modulo.update_status(pet)
        elif escolha == "3":
            print(funcoes["sleep"](pet))
            modulo.update_status(pet)
        elif escolha == "4":
            print(funcoes["shower"](pet))
            modulo.update_status(pet)
        elif escolha == "5":
            print(funcoes["talk"](pet))
        elif escolha == "6":
            print(funcoes["carinho"](pet))
            modulo.update_status(pet)
        elif escolha == "7":
            print(funcoes["trick"](pet))
            modulo.update_status(pet)
        elif escolha == "8":
            print(funcoes["petisco"](pet))
            modulo.update_status(pet)
        elif escolha == "9":
            print(funcoes["song"](pet))
        elif escolha == "10":
            print(funcoes["show_inventory"](pet))
        elif escolha == "11":
            show_status(pet, funcoes)
        elif escolha == "12":
            print(f"Tchau, {pet['nome']} vai sentir sua falta!")
            break
        else:
            print("Opção inválida, tente novamente.")
        show_status(pet, funcoes)

if __name__ == "__main__":
    main()
