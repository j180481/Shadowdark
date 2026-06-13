from storage_service import save_characters, load_characters
from rich.console import Console
from rich.table import Table
from character import Character


def add_character(character_data):
    store = load_characters()
    new_id = store["next_id"]
    store["characters"][str(new_id)] = character_data
    store["next_id"] = new_id + 1
    save_characters(store)
    return new_id


def delete_character(character_id):
    """Delete a character from the store by ID.

    Args:
        character_id (int): The ID of the character to delete.

    Returns:
        bool: True if the character existed and was deleted,
              False if no character had that ID.

    Side Effects:
        Saves the updated store to disk via save_characters.
    """
    store = load_characters()
    key = str(character_id)

    if key not in store["characters"]:
        return False

    del store["characters"][key]
    save_characters(store)
    return True


def get_character(character_id):
    store = load_characters()
    key = str(character_id)
    if key not in store['characters']:
        return None
    else:
        character_dict = store["characters"][key]
        return Character.from_dict(character_dict)


def list_characters():
    """Display all saved characters in a summary table."""
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
