import click
from src.create_character import construct_character
from src.character_manager import (add_character, list_characters,
                                   delete_character, get_character)
from rich.console import Console
from rich.table import Table
from src.storage_service import save_text


def valid_name_input(name):
    """
        Makes sure input for name is valid
    """
    name = name.strip()
    if len(name) == 0:
        return 0
    else:
        return True


def valid_id_input(name):
    """
    Makes sure id number for searches are valid
    """
    name = name.strip()
    if len(name) == 0:
        return False
    try:
        int(name)
    except ValueError:
        return False
    return True


def print_character(character):
    """
    Used for printing the character table to terminal
    """
    table = Table(title=f"{character.name} — Level {character.level}")
    table.add_column("Field", justify="right", style="cyan", no_wrap=True)
    table.add_column("Value", style="white")
    table.add_column("Modifier", justify="center", style="green")

    table.add_row("Ancestry", character.ancestry["name"], "")
    if character.player_class is None:
        table.add_row("Class", "—", "")
    else:
        table.add_row("Class", character.player_class, "")
    table.add_row("Alignment", character.alignment, "")
    table.add_row("Background", character.background, "")
    table.add_row("HP", str(character.health_points), "")
    table.add_row("AC", str(character.armor_class), "")
    table.add_row("Gold", str(character.gold), "")

    table.add_section()

    stats = [
        ("Strength", character.strength, character.strength_modifier),
        ("Dexterity", character.dexterity, character.dexterity_modifier),
        ("Constitution", character.constitution,
         character.constitution_modifier),
        ("Intelligence", character.intelligence,
         character.intelligence_modifier),
        ("Wisdom", character.wisdom, character.wisdom_modifier),
        ("Charisma", character.charisma, character.charisma_modifier),
    ]
    for stat_name, score, mod in stats:
        if mod >= 0:
            modifier = f"+{mod}"
        else:
            modifier = str(mod)
        table.add_row(stat_name, str(score), modifier)

    console = Console()
    console.print(table)


@click.group()
def cli():
    """Main click group which houses all Click.Commands"""
    pass


@cli.command()
@click.option('--name', prompt='Your name')
@click.option('--classed', is_flag=True, default=False)
def create(name, classed):
    """Create a new Shadowdark Character.
     Add --classed to generate with a class"""
    if valid_name_input(name) == 0:
        click.echo("Invalid. Cannot be empty space.")
        return

    if classed:
        character = construct_character(name, classed)

    else:
        character = construct_character(name, classed)

    print_character(character)

    response = click.prompt("Do yo want to save this character? Y/N")
    response = response.strip()
    response = response.upper()
    if response == "Y":
        save_character = character.to_dict()
        response = add_character(save_character)
        save_text(character, response)
        click.echo(f"{character.name} character sheet was saved to txt!")
        click.echo(f"{character.name} saved with ID {response}")


@cli.command()
def view():
    """View a list of saved characters"""
    list_characters()


@cli.command()
@click.option('--number', prompt='Id')
def delete(number):
    """delete character using id number"""
    if not valid_id_input(number):
        click.echo("Id must be a number")
        return

    response = delete_character(number)
    if response:
        click.echo(f"Character with ID {number} deleted")
    else:
        click.echo("Character doesn't exist")


@cli.command()
@click.option('--number', prompt='Id')
def show(number):
    """show character using id number"""
    if not valid_id_input(number):
        click.echo("Id must be a number")
    character = get_character(number)
    if character is None:
        click.echo("Character Id does not exist in save file")
        return

    print_character(character)


@cli.command()
@click.option('--number', prompt='Id')
def txt(number):
    """print a character sheet using id number"""
    if not valid_id_input(number):
        click.echo("Id must be a number")
    character = get_character(number)
    if character is None:
        click.echo("Character not in file")
    else:
        save_text(character, number)
        click.echo("Character sheet printed")


if __name__ == "__main__":
    cli()
    # main()
