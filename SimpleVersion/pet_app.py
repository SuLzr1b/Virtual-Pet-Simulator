from pet_utils import load_pet, create_pet, save_pet, feed_pet, play_pet, sleep_pet, shower_pet, talk_pet, carinho_pet, update_status, trick_pet, petisco_pet, song_pet, show_inventory, get_pet_message

def show_status(pet):
    print("=======================================")
    print(f"\n=== Estado de {pet['nome']} ===")
    print(f"Fome: {pet['fome']}")
    print(f"Felicidade: {pet['felicidade']}")
    print(f"Energia: {pet['energia']}")
    print(f"Higiene: {pet['higiene']}")
    print(f"Disciplina: {pet['disciplina']}")
    print(f"Truques: {', '.join(pet['truques']) if pet['truques'] else 'nenhum'}")
    print(f"Inventario: {', '.join(pet['inventario']) if pet['inventario'] else 'vazio'}")
    print(get_pet_message(pet)) 
    print("=======================================")

def main():
    pet = load_pet()
    if pet is None:
        nome = input("Bem-vindo ao Virtual Pet! Digite o nome do seu pet: ")
        pet = create_pet(nome)
        save_pet(pet)

    print(f"\nCuide de {pet['nome']}!\nUse o menu para interagir.")

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
        print("10. Mostrar Inventario")
        print("11. Ver status")
        print("12. Sair")
        escolha = input("Escolha uma opção (1-12): ")

        if escolha == "1":
            print(feed_pet(pet))
            update_status(pet)
        elif escolha == "2":
            print(play_pet(pet))
            update_status(pet)
        elif escolha == "3":
            print(sleep_pet(pet))
            update_status(pet)
        elif escolha == "4":
            print(shower_pet(pet))
            update_status(pet)
        elif escolha == "5":
            print(talk_pet(pet))
        elif escolha == "6":
            print(carinho_pet(pet))
            update_status(pet)
        elif escolha == "7":
            print(trick_pet(pet))
            update_status(pet)
        elif escolha == "8":
            print(petisco_pet(pet))
            update_status(pet)
        elif escolha == "9":
            print(song_pet(pet))
        elif escolha == "10":
            print(show_inventory(pet))

        elif escolha == "11":
            show_status(pet)
        elif escolha == "12": 
            print(f"Tchau, {pet['nome']} vai sentir sua falta!")
            break
        else:
            print("Opção inválida, tente novamente.")
        show_status(pet)

if __name__ == "__main__":
    main()