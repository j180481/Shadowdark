import json
import os

DATA_FILE = "characters.json"


def save_text(character, new_id):
    """Write a character's sheet to a .txt file named after the character."""
    ancestry_name = character.ancestry["name"]
    ancestry_talent = character.ancestry["talent"]

    with open(f"{character.name}{new_id}.txt", "w") as file:
        file.write(f"Name: {character.name}\n")
        file.write(f"Level: {character.level}\n")
        file.write(f"Class: {character.player_class or '—'}\n")
        file.write(f"Ancestry: {ancestry_name}\n")
        file.write(f"Alignment: {character.alignment}\n")
        file.write(f"Background: {character.background}\n")
        file.write(f"HP: {character.health_points},"
                   f" AC: {character.armor_class}\n")
        file.write(f"STR: {character.strength}"
                   f" ({character.strength_modifier})\n")
        file.write(f"DEX: {character.dexterity}"
                   f" ({character.dexterity_modifier})\n")
        file.write(f"CON: {character.constitution}"
                   f" ({character.constitution_modifier})\n")
        file.write(f"INT: {character.intelligence}"
                   f" ({character.intelligence_modifier})\n")
        file.write(f"WIS: {character.wisdom}"
                   f" ({character.wisdom_modifier})\n")
        file.write(f"CHA: {character.charisma}"
                   f" ({character.charisma_modifier})\n")
        file.write(f"Ancestry Talent: {ancestry_talent}\n")
        file.write(f"Gold: {character.gold}\n")


def load_characters():
    """Load the character store from disk, or return an empty one."""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    return {"next_id": 1, "characters": {}}


def save_characters(characters):
    """Write the character store to disk."""
    with open(DATA_FILE, "w") as file:
        json.dump(characters, file, indent=2)
