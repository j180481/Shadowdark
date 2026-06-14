

class Character:
    def __init__(self):
        self.name = ""

        self.health_points = 0

        self.level = 0

        self.gold = 0

        self.armor_class = 0

        self.player_class = ""

        self.strength = 0
        self.dexterity = 0
        self.constitution = 0
        self.intelligence = 0
        self.wisdom = 0
        self.charisma = 0

        self.strength_modifier = 0
        self.dexterity_modifier = 0
        self.constitution_modifier = 0
        self.intelligence_modifier = 0
        self.wisdom_modifier = 0
        self.charisma_modifier = 0

        self.ancestry = ""
        self.alignment = ""
        self.background = ""

    def to_dict(self):
        """
        Convert the Character into a dictionary
        for saving into JSON.

        Args:
            self: function calls on itself to
            construct the dictionary representation
            of the character.

        Returns:
            Dictionary: character attributes
            converted to keys and values in
            a dictionary.
        """
        return {
            "name": self.name,
            "level": self.level,
            "player_class": self.player_class,
            "health_points": self.health_points,
            "armor_class": self.armor_class,
            "gold": self.gold,
            "strength": self.strength,
            "dexterity": self.dexterity,
            "constitution": self.constitution,
            "intelligence": self.intelligence,
            "wisdom": self.wisdom,
            "charisma": self.charisma,
            "strength_modifier": self.strength_modifier,
            "dexterity_modifier": self.dexterity_modifier,
            "constitution_modifier": self.constitution_modifier,
            "intelligence_modifier": self.intelligence_modifier,
            "wisdom_modifier": self.wisdom_modifier,
            "charisma_modifier": self.charisma_modifier,
            "ancestry": self.ancestry,
            "alignment": self.alignment,
            "background": self.background,
        }

    @staticmethod
    def from_dict(data):
        """
        Rebuild a Character from its
        dictionary representation.
        Args:
            data: <dictionary> function to
            build a Character object using
            dictionary.

        Returns:
            Character: Character object built
            from the dictionary.
        """
        character = Character()
        character.name = data["name"]
        character.level = data["level"]
        character.player_class = data["player_class"]
        character.health_points = data["health_points"]
        character.armor_class = data["armor_class"]
        character.gold = data["gold"]
        character.strength = data["strength"]
        character.dexterity = data["dexterity"]
        character.constitution = data["constitution"]
        character.intelligence = data["intelligence"]
        character.wisdom = data["wisdom"]
        character.charisma = data["charisma"]
        character.strength_modifier = data["strength_modifier"]
        character.dexterity_modifier = data["dexterity_modifier"]
        character.constitution_modifier = data["constitution_modifier"]
        character.intelligence_modifier = data["intelligence_modifier"]
        character.wisdom_modifier = data["wisdom_modifier"]
        character.charisma_modifier = data["charisma_modifier"]
        character.ancestry = data["ancestry"]
        character.alignment = data["alignment"]
        character.background = data["background"]
        return character
