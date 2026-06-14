import json
import os

DATA_FILE = "characters.json"


def save_text(character, new_id):
    """Write a character's sheet to a .txt file named after the character.

    Args:
        character: Character object created in create_character,
            used to retrieve values.
        new_id: int, the character's storage ID. Used in the file
            name so multiple characters with the same name don't
            overwrite each other's sheets.

    Returns:
        None. Creates a text file on disk.
    """
    with open(f"{character.name}{new_id}.txt", "w") as file:
        file.write(f"Name: {character.name}\n")
        file.write(f"Level: {character.level}\n")
        # player_class can be a string or None; write the
        # class name or "—" if the attribute is None
        file.write(f"Class: {character.player_class or '—'}\n")
        file.write(f"Ancestry: {character.ancestry}\n")
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
        file.write(f"Gold: {character.gold}\n")


def load_characters():
    """
    Load the character storage file,
     or return an empty one.

    Args:
        No arguments necessary.

    Returns:
        Returns dictionary of saved characters
        or empty one if it doesn't exist.
    """
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    # "next_id" is how we calculate what the
    # id number for the next character we
    # save will be
    return {"next_id": 1, "characters": {}}


def save_characters(characters):
    """
    Write the dictionary of characters
    to storage.
    Args:
        characters: dictionary of saved characters.

    Returns:
        Does not return anything.
        It saves the character storage to system.
    """
    with open(DATA_FILE, "w") as file:
        json.dump(characters, file, indent=2)
