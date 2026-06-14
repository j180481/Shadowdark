import random
from src.dice import dice_roller
from src.character import Character
import math

D6 = 6

STATS_COUNT = 3

GOLD_COUNT = 2

HIT_DICE = {'Fighter': 8, 'Priest': 6, 'Thief': 4, 'Wizard': 4}

BACKGROUND = ['Urchin', 'Wanted', 'Cult Initiate',
              "Thieves' Guild", 'Banished', 'Orphaned',
              "Wizard's Apprentice", 'Jeweler', 'Herbalist',
              'Barbarian', 'Mercenary', 'Sailor',
              'Acolyte', 'Soldier', 'Ranger', 'Scout',
              'Minstrel', 'Scholar', 'Noble', 'Chirurgeon']

ALIGNMENT = ['Lawful', 'Neutral', 'Chaotic']


CLASSES = ['Fighter', 'Priest', 'Thief', 'Wizard']


ANCESTRY = [
    {'name': 'Dwarf',
     'talent': 'Stout. Start with +2 HP (Included).'
               'Roll your hit point gains with advantage.'},
    {'name': 'Elf',
     'talent': 'Farsight. You get a +1 bonus to attack rolls with '
               'ranged weapons or a +1 bonus to spellcasting checks.'},
    {'name': 'Half-Orc',
     'talent': 'Mighty. You have a +1 bonus'
               ' to attack and damage rolls with melee weapons.'},
    {'name': 'Halfling',
     'talent': 'Stealthy. Once per day, '
               'you can become invisible for 3 rounds.'},
    {'name': 'Goblin',
     'talent': 'Keen Senses. You cannot be surprised.'},
    {'name': 'Human',
     'talent': 'Ambitious. You gain one additional'
               ' talent roll at 1st level.'}
]


def get_stat_mod(stat):
    """
    Used to calculate the stat modified (strength, dexterity...)

    Context: Original version is fine. On account this has been
    modularized for further expansion, also with the dice itself
    being further modularized, things like extra rolling for
    human ancestry could slightly break the stat mods pushing
    it to -5 or +5. This just nails it down.

    Args:
        stat (int): The ability score.

    Returns:
        int: The modifier, between -4 and +4.
    """
    return max(-4, min(4, math.floor((stat - 10) / 2)))


def get_class(classes):
    """
        Used to randomly return a class name
        for character creation:
        - fighter
        - priest
        - thief
        - wizard
        The classes list is passed as an arg
        then by using random choice returning
        that class as string

        Args:
            classes (list): list of classes.

        Returns:
            string: random class name.
    """
    return random.choice(classes)


def get_background(backgrounds):
    """
        Used to randomly return a background name
        for character creation:
        The backgrounds list is passed as an arg
        then by using random choice returning
        that background as string

        Args:
            backgrounds (list): list of backgrounds.

        Returns:
            string: random background name.
    """
    return random.choice(backgrounds)


def get_alignment(alignments):
    """
    Used to randomly return a background name
    for character creation:
    The backgrounds list is passed as an arg
    then by using random choice returning
    that background as string

    Args:
        alignments (list): list of alignments.

    Returns:
        string: random alignments name
    """
    return random.choice(alignments)


def get_ancestry(ancestries):
    """
        Used to randomly return an ancestry
        name and talent
        for character creation:
        The ancestries list is passed as an arg
        then by using random choice returning
        that dictionary ancestry

        Args:
            ancestries (list): list of ancestries.

        Returns:
            dictionary: random ancestry dictionary.
        """
    return random.choice(ancestries)


def get_stat():
    """
        Used to randomly "roll" character stats.

        Args:
            Does not take arguments.

        Returns:
            int: sum of random int between 1 and D6 (6)
            rolled STATS_COUNT amount of times.
    """
    return dice_roller(D6, STATS_COUNT)


def get_hp(constitution_mod, player_class=None):
    """
        Return starting HP.
        Level 0 (no class): just the CON modifier,
         floored at 1.
        Level 1 (classed): one hit-die (of that class)
        roll + CON modifier, floored at 1.

        Args:
            constitution_mod: int of modifier
             for constitution.
            player_class: boolean. Whether the
            character being created is classed
            or not.

        Returns:
            int: final health points based on class
            status and hit die roll based on this

    """
    if player_class is None:
        return max(1, constitution_mod)
    hit_die = HIT_DICE[player_class]
    return max(1, dice_roller(hit_die, 1) + constitution_mod)


def get_gold():
    """
        Used to randomly "roll" character
        starting gold.

        Args:
            Does not take arguments.

        Returns:
            int: sum of random int between 1 and D6 (6)
            rolled GOLD_COUNT amount of times.
    """
    return dice_roller(D6, GOLD_COUNT)


def construct_character(name, classed=True):
    """
        Takes the name input by user and creates a new character.

        Args:
            name: <string> name input by user.
            classed: <boolean> whether character
            should be classed or not.

        Returns:
            Character: returns a built character in
            Character class object.
    """
    new_character = Character()
    new_character.name = name
    if classed:
        # if classed true
        # set character level 1
        new_character.level = 1
        # if classed true
        # call get_class, set player class
        new_character.player_class = get_class(CLASSES)
    else:
        # if classed=false
        # set character level to 0
        new_character.level = 0
        # if classed=false
        # Character attribute player_class set to None
        new_character.player_class = None

    new_character.gold = get_gold() * 5
    new_character.strength = get_stat()
    new_character.dexterity = get_stat()
    new_character.constitution = get_stat()
    new_character.intelligence = get_stat()
    new_character.wisdom = get_stat()
    new_character.charisma = get_stat()

    new_character.strength_modifier =\
        get_stat_mod(new_character.strength)
    new_character.dexterity_modifier =\
        get_stat_mod(new_character.dexterity)
    new_character.constitution_modifier =\
        get_stat_mod(new_character.constitution)
    new_character.intelligence_modifier =\
        get_stat_mod(new_character.intelligence)
    new_character.wisdom_modifier =\
        get_stat_mod(new_character.wisdom)
    new_character.charisma_modifier =\
        get_stat_mod(new_character.charisma)

    new_character.health_points =\
        get_hp(new_character.constitution_modifier, new_character.player_class)

    new_character.armor_class = 10 + new_character.dexterity_modifier

    new_character.ancestry = get_ancestry(ANCESTRY)
    new_character.alignment = get_alignment(ALIGNMENT)
    new_character.background = get_background(BACKGROUND)

    return new_character
