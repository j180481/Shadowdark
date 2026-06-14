# Shadowdark Character Generator

A command line character generator for the Shadowdark RPG, written in Python.
It rolls a character's stats, ancestry, background, alignment, and (optionally)
class, saves characters to a persistent store, and displays them as formatted
tables in the terminal.

## Features

- Generate a random level-0 character, or a level-1 character with a class
  (--classed).
- Stats rolled as 3d6 with ability modifiers clamped to Shadowdark's -4 to +4
  range.
- Armour class and HP calculated automatically (HP uses the class hit die plus
  Constitution modifier for classed characters).
- Save characters to a JSON store and reload, view, or delete them later.
- View a single character sheet or the full list of saved characters as Rich
  tables.
- Export any saved character back out to a .txt sheet.

## Requirements

- Python (developed on 3.11).
- Dependencies: (click, rich).

## Setup

Clone the repository and move into the project folder:

```bash
git clone <your-repo-url>
cd Shadowdark-Character-Generator
```

Create/activate a virtual environment.

**Git Bash:**

```bash
python -m venv .venv
source .venv/Scripts/activate
```


Install dependencies:

```bash
pip install -r requirements.txt

pip install -r requirements-dev.txt
```

## Usage

Run the app through main.py. Use --help on any command to see its options:

```bash
python main.py --help
python main.py create --help
```
![Help screenshot](images/command_help.png)


### Commands

**Create a character**

Generate a new character. You'll be prompted for a name if you don't pass one,
then shown the character sheet and asked whether to save it.

```bash
python main.py create
python main.py create --name "Garrosh"
```
![create screenshot](images/python_create_0.png)

![create pt2 screenshot](images/create_0_name.png)

Add --classed to generate a level 1 character with a randomly assigned class
(Fighter, Priest, Thief, or Wizard):

```bash
python main.py create --name "Garrosh" --classed
```
![garrosh classed screenshot](images/garrosh_classed.png)

**View saved characters**

List every saved character in a table, with their IDs:

```bash
python main.py view
```
![View screenshot](images/view.png)

**Show a character sheet**

Display a single saved character's full sheet by ID:

```bash
python main.py show --number 1
```

![show screenshot](images/show.png)

**Export a character to a text file**

Write a saved character's sheet out to a `.txt` file:

```bash
python main.py txt --number 1
```
![txt output](images/txt_output.png)

**Delete a character**

Remove a saved character by ID:

```bash
python main.py delete --number 1
```

![delete output](images/delete_output.png)

## Project structure

Shadowdark-Character-Generator/
- main.py
- src/
  - character.py
  - create_character.py
  - character_manager.py
  - dice.py
  - storage_service.py
- tests/
  - requirements.txt
  - requirements-dev.txt


## Running the tests

With the dev dependencies installed and the virtual environment active, run the unittest 
from the project root:

```bash
python run -m unittest discover
```

## Acknowledgements
- This is based on an original script by jason-napier
- Baron de Ropp contributed previous code revisions.

## License & Attribution
This is an independent project published under the Shadowdark RPG
Third-Party License and is not affiliated with The Arcane Library, LLC.
Shadowdark RPG © 2023 The Arcane Library, LLC.