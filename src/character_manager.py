from src.storage_service import save_characters, load_characters
from rich.console import Console
from rich.table import Table
from src.character import Character


def add_character(character_data):
    """
    Add character to storage

    Args:
         character_data: dictionary of
         character data to store in the
         json storage file.
    Returns:
        new_id: <int> number of the next
        id to be assigned when adding
        a character. This is used
        in the JSON storage file.
    """
    store = load_characters()
    new_id = store["next_id"]
    store["characters"][str(new_id)] = character_data
    store["next_id"] = new_id + 1
    save_characters(store)
    return new_id


def delete_character(character_id):
    """
    Delete a character from the storage by ID.
    Loads the character storage file.
    Delete character from dictionary.
    Resave new characters save file.

    Args:
        character_id (int): The ID of the character to delete.

    Returns:
        bool: True if the character existed and was deleted,
              False if no character had that ID.
    """
    store = load_characters()
    key = str(character_id)

    if key not in store["characters"]:
        return False

    del store["characters"][key]
    save_characters(store)
    return True


def get_character(character_id):
    """
        Gets a character from the storage file.
        This is used for "show" character based
        on character id input by user.

        Args:
            character_id (int): The ID of the character
            to retrieve a Character object built
            from the storage file.

        Returns:
            Character: character object built
            from the dictionary found in the storage.
    """
    store = load_characters()
    key = str(character_id)
    if key not in store['characters']:
        return None
    else:
        character_dict = store["characters"][key]
        return Character.from_dict(character_dict)


def list_characters():
    """
        Loads and opens characters save file.
        Builds a table with character representations
        and their id number.

        Args:
            No arguments passed.

        Returns:
            No return.
            It Console.Prints the Table(character list) of
            characters.
    """
    store = load_characters()

    table = Table(title="Characters")
    table.add_column("ID", justify="right", style="cyan", no_wrap=True)
    table.add_column("Name", style="magenta")
    table.add_column("Level", style="yellow")
    table.add_column("Class", style="green")

    for character_id, character_data in store["characters"].items():
        table.add_row(
            character_id,
            character_data["name"],
            str(character_data["level"]),
            character_data["player_class"] or "—",
        )

    console = Console()
    console.print(table)
