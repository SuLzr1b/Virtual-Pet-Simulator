# Virtual Pet Simulator

Welcome to **Virtual Pet Simulator**, a fun and interactive command-line game written in Python! In this game, you can adopt a virtual pet—choose between a dog, cat, or dragon—and take care of its needs, teach it tricks, collect items, and even make it sing. Each pet type has unique behaviors and responses, making every interaction special. Whether you're feeding your dog a bone, playing with your cat's yarn, or watching your dragon breathe fire, this simulator offers a delightful virtual pet experience.

This project was created for educational purposes, showcasing Python programming concepts like modular design, file handling, and dynamic function mapping. It's perfect for beginners learning Python or anyone who loves virtual pets!

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [How to Play](#how-to-play)
- [Project Structure](#project-structure)
- [License](#license)

## Features
- **Pet Customization**: Choose your pet's name and type (dog, cat, or dragon) when starting the game.
- **Unique Pet Behaviors**:
  - **Dog**: Loves chasing balls, learns tricks like "sit," and collects items like bones.
  - **Cat**: Enjoys yarn, learns tricks like "jump," and collects items like feathers.
  - **Dragon**: Flies and breathes fire, learns tricks like "spit fire," and collects items like jewels.
- **Interactive Actions**:
  - Feed your pet to reduce hunger.
  - Play to increase happiness (with a 30% chance to find items for the inventory).
  - Put your pet to sleep to restore energy.
  - Give a bath to improve hygiene.
  - Talk to hear unique pet sounds (e.g., "Woof!" for dogs, "Miau!" for cats).
  - Give affection to boost happiness.
  - Teach tricks to increase discipline and happiness.
  - Offer a treat to reduce hunger and increase happiness.
  - Make your pet sing fun songs.
  - Check the inventory to see collected items.
  - View the pet's status (hunger, happiness, energy, hygiene, discipline, tricks, inventory).
- **Persistent State**: Pet data (name, type, stats, tricks, inventory) is saved to `pet.txt` and loaded automatically.
- **Dynamic Gameplay**: Each pet type has tailored messages and effects (e.g., cats lose less hygiene when playing, dragons gain more happiness).

## Installation
To run the Virtual Pet Simulator, you need Python installed. No external libraries are required!

1. **Prerequisites**:
   - Python 3.8 or higher (available at [python.org](https://www.python.org/downloads/)).
   - A terminal or command prompt.

2. **Clone the Repository**:
   ```bash
   git clone https://github.com/<your-username>/virtual-pet-simulator.git
   cd virtual-pet-simulator
   ```

3. **Verify Files**:
   Ensure the following files are in the project directory:
   - `pet_app.py`
   - `dog.py`
   - `cat.py`
   - `dragon.py`

4. **Optional: Remove Old Save**:
   If you have a `pet.txt` file from a previous run, delete it to start fresh:
   ```bash
   rm pet.txt  # Linux/Mac
   del pet.txt  # Windows
   ```

## How to Play
1. **Run the Game**:
   In the project directory, run:
   ```bash
   python pet_app.py
   ```

2. **Create Your Pet**:
   - Enter your pet's name (e.g., "name_pet").
   - Choose a pet type:
     - `1` for Dog
     - `2` for Cat
     - `3` for Dragon

3. **Use the Menu**:
   Interact with your pet using the menu (1-12):
   - `1. Feed`: Reduce hunger (e.g., "name_pet abanou o rabo com a ração!").
   - `2. Play`: Increase happiness, may find items (e.g., "name_pet correu atrás da bola! Encontrou um osso!").
   - `3. Sleep`: Restore energy.
   - `4. Bath`: Improve hygiene.
   - `5. Talk`: Hear your pet's unique sounds.
   - `6. Affection`: Boost happiness.
   - `7. Trick`: Teach a new trick (e.g., "name_pet aprendeu a sentar!").
   - `8. Treat`: Give a treat to reduce hunger.
   - `9. Sing`: Make your pet sing a fun song.
   - `10. Show Inventory`: View collected items.
   - `11. Status`: Check all pet stats.
   - `12. Exit`: Save and quit.

4. **Game Mechanics**:
   - Pet stats (hunger, happiness, energy, hygiene) change over time and with actions.
   - Hunger increases, while happiness, energy, and hygiene decrease unless you act.
   - Discipline improves by teaching tricks.
   - Items are collected randomly when playing (30% chance).
   - The pet's state is saved to `pet.txt` after most actions.

## Project Structure
- **`pet_app.py`**: Main game logic, handles user input, menu, and dynamic loading of pet type modules.
- **`dog.py`**: Functions for dog-specific behaviors (e.g., `feed_dog`, `talk_dog`).
- **`cat.py`**: Functions for cat-specific behaviors (e.g., `feed_cat`, `talk_cat`).
- **`dragon.py`**: Functions for dragon-specific behaviors (e.g., `feed_dragon`, `talk_dragon`).
- **`pet.txt`**: Auto-generated file that stores the pet's state (e.g., `name_pet|dog|50|50|50|50|0|sentar|osso`).

Each pet type module (`dog.py`, `cat.py`, `dragon.py`) contains functions like `create_pet`, `save_pet`, `load_pet`, and action-specific functions (e.g., `play_dog`, `trick_cat`). The `pet_app.py` dynamically imports the correct module based on the pet's type.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---
Created by [SuLzr1b] as part of a cybersecurity learning journey.
