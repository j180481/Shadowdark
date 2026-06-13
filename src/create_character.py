import random
from dice import dice_roller
from character import Character
import math

D6 = 6

STATS_COUNT = 3

GOLD_COUNT = 2

HIT_DICE = {'Fighter': 8, 'Priest': 6, 'Thief': 4, 'Wizard': 4}

Background = ['Urchin', 'Wanted', 'Cult Initiate',
              "Thieves' Guild", 'Banished', 'Orphaned',
              "Wizard's Apprentice", 'Jeweler', 'Herbalist',
              'Barbarian', 'Mercenary', 'Sailor',
              'Acolyte', 'Soldier', 'Ranger', 'Scout',
              'Minstrel', 'Scholar', 'Noble', 'Chirurgeon']

Alignment = ['Lawful', 'Neutral', 'Chaotic']


Classes = ['Fighter', 'Priest', 'Thief', 'Wizard']


Ancestry = [
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
    return max(-4, min(4, math.floor((stat - 10) / 2)))


def get_class(classes):
    return random.choice(classes)


def get_background(backgrounds):
    return random.choice(backgrounds)


def get_alignment(alignments):
    return random.choice(alignments)


def get_ancestry(ancestries):
    return random.choice(ancestries)


def get_stat():
    return dice_roller(D6, STATS_COUNT)


def get_hp(constitution_mod, player_class=None):
    """Return starting HP.

    Level 0 (no class): just the CON modifier, floored at 1.
    Level 1 (classed): one hit-die roll + CON modifier, floored at 1.
    """
    if player_class is None:
        return max(1, constitution_mod)
    hit_die = HIT_DICE[player_class]
    return max(1, dice_roller(hit_die, 1) + constitution_mod)


def get_gold():
    return dice_roller(D6, GOLD_COUNT)


def construct_character(name, classed=True):
    new_character = Character()
    new_character.name = name
    if classed:
        new_character.level = 1
        new_character.player_class = get_class(Classes)
    else:
        new_character.level = 0
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

    new_character.ancestry = get_ancestry(Ancestry)
    new_character.alignment = get_alignment(Alignment)
    new_character.background = get_background(Background)

    return new_character
