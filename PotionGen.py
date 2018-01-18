#!/usr/bin/env python3

# PotionGen.py
# Francis Windram
# 16/01/18
# Version 0.0.1
#
# Python 3.4.1
#
# Generates a random potion
#

import random
import sys
import argparse

# Source lists (could split out to separate area)
titles_l = ["Potion", "Elixir", "Draught", "Vial", "Philter", "Tonic", "Brew", "Ichor", "Juice", "Concoction"]
effects_l = [
    ("Healing", "It instantly regenerates some health when drank"), ("Vigor", "Gives temporary health when drank"),
    ("Vitality", "It slowly regenerates health over a period of some hours"),
    ("Might", "It gives a bonus to attack rolls after drinking"),
    ("Courage", "Gives immunity to fear and some temporary inspiration"),
    ("Giant Strength", "It gives the user much more strength"),
    ("Flame Resistance", "It gives resistance to fire damage"),
    ("Cold Resistance", "It gives resistance to cold damage"),
    ("Necro Resistance", "Gives resistance to necrotic damage"),
    ("Radiant Resistance", "Gives resistance to radiant damage"),
    ("Stoneskin", "Gives resistance to martial damage"),
    ("Acid Resistance", "Gives resistance to acid"),
    ("Lightning Resistance", "Gives resistance to lightning damage"),
    ("Succubus Charm", "Makes the drinker irresistible to nearby people"),
    ("Shielding", "Gives the user a magical shield of energy"),
    ("Flame Breath", "Gives the user fire breath for a short time"),
    ("Growth", "Makes the user double in size"),
    ("Shrinking", "Makes the user halve in size"),
    ("Comprehension", "Lets the user understand all languages"),
    ("Fertility", "Makes the user infatuated with those of the opposite gender (if possible)."),
    ("Intimidation", "Gives the user a huge booming voice that terrifies those around"),
    ("Luck", "It gives the user a temporary boost to luck"),
    ("Mana", "Gives the user more magical power to cast with"),
    ("Arcane", "Gives the user more powerful spells"),
    ("Animal Form", "Makes the user turn into a random animal"),
    ("Dreams", "Makes the user get lost in a hallucinatory dream world of their perfect dream"),
    ("Nightmares", "Makes the user get lost in a hallucinatory dream world of their worst nightmares"),
    ("Stamina", "Gives the user more stamina and constitution"),
    ("Fleet Foot", "Makes the user have more speed"),
    ("Knowledge", "Increases the users intelligence temporarily"),
    ("The Bard", "Increases the users temporarily"),
    ("Disguise", "Changes the users form to a disguised form of any race and appearance"),
    ("Feast", "Removes all hunger and thirst from the target"),
    ("Youth", "Makes the user grow younger"),
    ("Age", "Makes the user grow older"),
    ("Furnace", "Makes the user radiate with a damaging aura"),
    ("Eagle Sight", "Gives the user strong vision and a bonus to perception"),
    ("Health", "Cures all diseases and illnesses"),
    ("Invulnerability", "Freezes the user in stasis that makes them immune to damage but they cannot move or act"),
    ("Riddle-me-Gone", "Gives the user the cure to a single riddle"),
    ("Horrifying Appearance", "Makes the user look more ugly for a time"),
    ("Beautiful Appearance", "Makes the user appear more attractive for a time"),
    ("Swordsmanship", "Makes the user more effective and versatile with a blade"),
    ("Bowmanship", "Makes the user more effective with a bow or ranged weapon"),
    ("Nymph Breath", "Gives water breathing"),
    ("Midas", "Makes the user turn things to gold"),
    ("Berserker", "Makes the user rage with great strength"),
    ("Utter Hatred", "Makes the user have bonuses against a particular type of enemy"),
    ("Oracle", "Lets the user divine the future"),
    ("Demonic Leech", "Heals a portion of all damage the user deals"),
    ("Fey Nature", "Lets the user become one with animals and nature around them"),
    ("Tracelessness", "Makes the user very hard to follow"),
    ("Gracefulness", "Makes the user have a better acrobatics skill"),
    ("Goblin Climb", "Gives the user a bonus to climbing"),
    ("Dead Ringer", "Makes the user appear completely dead to all magic"),
    ("One Leafed Clover", "Gives the user worst luck"),
    ("Possession", "Lets the user gain control of a nearby creature, their body comatose while they do"),
    ("Owls Wake", "Makes the user need no sleep for a time"),
    ("Hawks Flight", "Lets the user fly"),
    ("Peace", "Makes the user very calm and unable to harm others"),
    ("Rejuvenation", "Heals a single scar or bad injury on the user such as a missing arm"),
    ("Sphinxes Truth", "Makes the user tell the truth"),
    ("Serpent Tongue", "Makes the user only able to lie"),
    ("Navigation", "Makes the user unable to get lost and find where they need"),
    ("Hook Horror", "The users hands become sharp, weaponised blades"),
    ("Schaudenfreude", "Makes the enemies take damage as they deal it to the user"),
    ("Invisibility", "Makes the user invisible"),
    ("Wild Magic", "Causes a wild magic event"),
    ("Fame", "Makes the user more famous"),
    ("Goats Trek", "Makes the user immune to the toils of long travels and bad weather"),
    ("Gargoyle Toughness", "Increases the users constitution"),
    ("Atomic Clock", "Lets the user know the exact time and date"),
    ("Transmutation", "Lets the user have the ability to change an object's properties"),
    ("Iron Skin", "Turns the users skin to metal giving them many resistances"),
    ("Sex Change", "Changes the user's gender"),
    ("Race Change", "Changes the user's race"),
    ("Musical Breath", "Makes the user say everything in song, and fey music follows them in the air"),
    ("Utter Understanding", "Makes the user know very intimately about one exact thing"),
    ("Split Form", "The user turns into two or three tiny versions of themselves and controls them all"),
    ("Flavour", "Makes anything and everything taste amazing"),
    ("Glimmer", "Makes the user and its gear instantly clean and as good-looking as possible"),
    ("Love", "Makes the user and someone else fall in love"),
    ("Poison", "Poisons the user, weakening them"),
    ("Rebirth", "Resurrects the user if they die soon after drinking"),
    ("Elemental Form", "Turns the user to an elemental form relevant to their personality"),
    ("True Form", "Turns the user into a familiar like creature similar to their personality"),
    ("Gods Touch", "Gives the user a holy connection to their god or fiendish deity"),
    ("Antidepression", "Does what it says on the tin"),
    ("Ghostly Form", "Makes the user intangible and able to phase through objects"),
    ("Artisans Skill", "Gives the user skill in a particular art temporarily"),
    ("Godly Form", "Improves all stats"),
    ("Bless Weapon", "Makes the user's weapons do more damage"),
    ("Euphoria", "Makes the user feel amazing and trip out"),
    ("Bodyguard", "Creates a spectral bodyguard for a short time who obeys orders"),
    ("Babelfish", "Lets the user speak any language but not understand it"),
    ("Preservation", "Stops whatever its poured on from rotting or degrading"),
    ("Fear", "Makes the user terrified"),
    ("Night Vision", "Gives the ability to see in the dark"),
    ("Tracking", "Lets the user track an enemy"),
    ("Cure-all", "Cures any status effects")
]
strengths_lookup = ["na", "min", "reg", "maj", "perm"]
# strengths_lookup_old = ["None", "Minor", "Regular", "Major", "Permanent"]
strengths_l = [(2, 1), (2, 0), (2, 3), (1, 3), (1, 1), (3, 3), (3, 1), (0, 3), (3, 0), (4, 0)]
sideeffects_l = [
    "nothing bad at all", "the user to sleep", "rapid hair growth all over the body", "bleeding from the eyes",
    "vivid hallucinations", "flashbacks of your own eventual demise", "the skin to crack and appear distorted",
    "spots to grow on the skin", "diarrhoea", "vomiting", "blurred vision", "blindness", "deafness", "mutism",
    "health loss via rapid bleeding", "a sudden horrific accent", "the irresistible urge to dance",
    "audible demonic screams", "loss of balance", "everything to taste like dirt for some time", "excessive drooling",
    "loss of intelligence", "loss of strength", "loss of speed", "loss of charisma", "genuine happiness", "hunger",
    "thirst", "trouble breathing", "sudden moustache to appear", "poisoning", "petrification", "stunning",
    "immobilisation", "increased libido", "fidgeting", "itchiness", "rashes", "bears to appear",
    "magical dirt to appear all around the consumer", "horrifying stench", "baldness", "swelling",
    "loss of a random item", "curses", "damage", "weakness to a magical damage type", "weakness to physical damage",
    "feelings of guilt", "feelings of anxiety", "feelings of shame", "sneezing", "uncontrollable crying",
    "an irresistible urge to sing heroic music", "urge to hug", "kleptomania", "burping", "loss of smell", "insomnia",
    "paranoia", "bad luck", "nasty imps to appear", "bees", "fear of something", "temporary madness", "relaxation",
    "distinct appreciation of colours and sound", "an intense psychoactive trip", "painful lust", "light headedness",
    "increased confidence", "recklessness", "rage", "sadness", "dizziness", "pain", "slight possession",
    "an allergic reaction to your favourite food", "a strong belief that you’re someone else", "severe debt",
    "grumpiness", "muscle spasms", "a bloated feeling", "a mild cold", "a fever", "you to become strangely light",
    "weakness", "the urge to fight", "the need to make friends", "nausea", "mood swings", "addiction",
    "a need for alcohol", "drunkenness", "coughing", "uncontrollable babbling", "slight aches",
    "a bad taste for some time", "giddiness", "laughter", "uncontrollable complaining"
]
container_l = [
    "a conical, smooth glass bottle", "a square glass bottle", "a not-quite-watertight leather waterskin",
    "a stone flask", "a metal thermos", "a glass syringe", "a small medical vial", "a small shot sized bottle",
    "a large metal bottle", "a capped horn", "an ornate, very decorated glass bottle",
    "a geometric diamond shaped bottle", "a translucent long wine bottle", "a translucent beer bottle",
    "a leather pouch", "an inhaler-like spray bottle", "a coloured bottle", "a bone flask", "a small metal vial",
    "a large bottle which can be swigged from several times"
]
colour_l = [
    "Clear", "Blue", "Green", "Red", "Pale Green", "Pink", "Light Blue", "White", "Black", "Dark Grey", "Light grey",
    "Yellow", "Orange", "Gold", "Orange", "Bronze", "Metallic", "Purple", "Brown", "Dark Red"
]
appearance_l = [
    "flecks of colour", "swirls of colour", "fizzing bubbles", "bubbles suspended in it",
    "some kind of bone floating in it", "leaves and flowers in it", "two separating liquids", "a bright glow",
    "a soft glow", "stripes of colour", "a certain translucency", "a butty murkiness", "blood within it",
    "dirt floating in it", "chunks of metal in it", "some type of gore from a slain creature", "steam coming from it",
    "a face in the liquid", "constantly moving and shifting liquid", "a constant heat"
]
texture_l = [
    "Thick and sludgy", "Thin and watery", "Airy and bubbly", "Slimy", "Almost solid", "Oily", "Chunky", "Gritty",
    "Milky", "Almost gaseous"
]
taste_l = [
    "nothing at all", "sulphur", "fresh air", "baking cookies", "flowers", "rotting meat", "egg", "rotten eggs",
    "fresh bread", "blood", "home", "vomit", "garlic", "fruit", "chocolate", "beer", "smoke", "wood", "death", "orc",
    "wet dog", "wet goblin", "perfume", "cheap perfume", "musk", "garbage", "sand", "the forest", "nuts", "acid",
    "spice", "mint", "chemicals", "dirt", "something bad, masked to taste better", "alcohol", "sugar",
    "a damp cave", "something strange", "something indescribable but nice", "something indescribable but horrid",
    "rain", "medicine", "bacon", "coffee", "cut grass", "vanilla", "the sea", "roast meat", "festive foods",
    "lavender", "lilac and gooseberries", "a fresh baby", "a new cart", "citrus", "leather", "metal", "a forge",
    "fresh cake", "paint", "wine", "polish", "cheese", "fish", "compost", "the sewers", "apples", "holy oils",
    "massage oil", "a brothel", "old fruit", "roses", "something that stirs memories", "gingerbread", "cinnamon",
    "candy", "fumes", "bark", "chicken", "beef", "human flesh", "gunpowder", "a storm", "success", "gold", "mayonnaise",
    "barbecue", "salt", "pepper", "aromatic spices", "fruit punch", "water", "fresh water", "stagnant water", "mud",
    "a colour", "music", "the end of the world", "the worst thing you could hope for",
    "the best thing you could hope for"
]
label_l = [
    "Its name and title in bold letters", "Its description in ornate elvish",
    "Its description in elvish with a relevant mythic story", "Its description in Dwarven", "Dwarven runes",
    "Its description in gnomish", "Gnomish diagrams for its use",
    "The words USE ONLY IN EMERGENCIES scrawled in large shaky letters",
    "A mass produced label claiming the company has no fault for any side effects",
    "A mass produced label saying it’s a new flavour",
    "Very tiny print describing how the potion was made in great detail, around 1000 words",
    "Its name in Bold words in Giant", "a scrawled off name", "Has faded beyond reading", "Doesn’t seem to have one",
    "Its description and a random fact", "Its description and a small compliment to make your day better",
    "Its description and a joke", "Its description in infernal", "Its description in some ancient language",
    "All in some kind of symbols", "All in some kind of raised symbols for the blind to read",
    "Its description in elemental languages", "Its name and flavour", "Its name with a warning about side effects",
    "Its name and its recommended buying price", "Bloody prints all over it", "Name engraved into the container",
    "Its name glowing with minor magic", "A cartoonish mascot", "A warning of an ancient curse",
    "Its name and description in invisible ink", "Its description in Draconic",
    "Several different names and descriptions plastered over each other",
    "A name of a completely different potion to what it does", "A title describing the exact opposite",
    "A money back guarantee", "A coupon for a free potion", "A living face looking around",
    "Its name and recipe for other alchemists", "A heartfelt love letter for someone",
    "A heartfelt hate letter for someone", "A persons name. The potion wont work unless asked by its name to do so",
    "A strange prophecy", "A small doodle", "A note saying DO NOT DRINK",
    "A passive-aggressive note about other people drinking potions that don’t belong to them",
    "Brightly glowing letters", "That plays a very quiet sing song till the bottle is empty",
    "Ornate and beautiful designs", "Very practical designs", "Holy symbols", "Unholy symbols",
    "Fey symbols and sylvan writing", "A riddle, the lid not opening unless the riddle is solved",
    "Saying its designed for babies", "Saying that it shouldn’t be drank by anyone under 18",
    "A note saying its illegal contraband being confiscated",
    "A note saying the alchemist thinks it is its greatest work",
    "A note saying the alchemist is sorry for ever creating it",
    "A note saying that it never should have been made and copious blood stains over the bottle",
    "It says you’re being watched. When the person checks it instead says Just Kidding",
    "Its description in Druidic", "Its description in Orcish", "Its description in Goblin",
    "Its description in Halfling", "Its description in Celestial", "Its description in Undercommon",
    "Its description in Deep Speech", "Its description in strange arcane symbols", "A map of where the potion was made",
    "A small puzzle for kids", "A list of ingredients in their chemical forms",
    "A list of possible side effects as long as the bottle is", "A red X", "A sad face", "An angry face",
    "A happy face", "A healing symbol", "A cheesy pun potion name", "Growing with vines", "Growing with flowers",
    "Growing with crystals", "Growing with rock", "Shamanistic symbols and shavings", "No words just a single colour",
    "Water damage but a just legible label", "A label as if it was some kind of present",
    "A label showing how many calories it is", "A warning about potion abuse and to only take in moderation",
    "A label with warnings and side effects all scribbled out", "That only shows the side effects",
    "A mysterious number", "A code name", "A few unrelated letters", "The name of one of the party members",
    "The name of the bad guy", "Crawling with bugs", "Covered in something unspeakable",
    "Covered in glitter. It gets everywhere"
]


class Potion:
    """ Container class for potions """
    def __init__(self):
        self.seed = []
        self.strengthvals = ()
        self.title = []
        self.effect_name = ""
        self.effect = ""
        self.effect_strength = ""
        self.sideeffect = ""
        self.sideeffect_strength = ""
        self.container = ""
        self.colour = ""
        self.appearance = ""
        self.texture = ""
        self.taste = ""
        self.smell = ""
        self.label = ""

    def __repr__(self):
        return "\n".join(" = ".join((k, str(v))) for k, v in sorted(vars(self).items()))

    def __str__(self):
        descripstr = ""
        descripstr += "{} of {} ({}/{})\n".format(self.title,
                                                  self.effect_name,
                                                  self.effect_strength,
                                                  self.sideeffect_strength)

        if self.strengthvals[0]:
            descripstr += "{}. ".format(self.effect)
        if self.strengthvals[1]:
            descripstr += "Causes {}. ".format(self.sideeffect)
        descripstr += "\nComes in {}.\n{} with {}. {}.".format(self.container,
                                                               self.colour,
                                                               self.appearance,
                                                               self.texture)
        descripstr += "\nSmells of {} and tastes of {}.\nLabel: {}".format(self.smell, self.taste, self.label)
        return descripstr


def potiongen():
    workingpotion = Potion()
    seed_list = []

    # This has a lot of boilerplate, but refactoring is just complicated enough that I don't want to do it.

    # Determine title
    seed_curr = random.randrange(len(titles_l))
    workingpotion.title = titles_l[seed_curr]
    seed_list.append(seed_curr)

    # Determine effect
    seed_curr = random.randrange(len(effects_l))
    workingpotion.effect_name = effects_l[seed_curr][0]
    workingpotion.effect = effects_l[seed_curr][1]
    seed_list.append(seed_curr)

    # Determine strengths
    seed_curr = random.randrange(len(strengths_l))
    workingpotion.strengthvals = strengths_l[seed_curr]
    workingpotion.effect_strength = strengths_lookup[strengths_l[seed_curr][0]]
    workingpotion.sideeffect_strength = strengths_lookup[strengths_l[seed_curr][1]]
    seed_list.append(seed_curr)

    # Determine sideeffect
    seed_curr = random.randrange(len(sideeffects_l))
    workingpotion.sideeffect = sideeffects_l[seed_curr]
    seed_list.append(seed_curr)

    # Determine container
    seed_curr = random.randrange(len(container_l))
    workingpotion.container = container_l[seed_curr]
    seed_list.append(seed_curr)

    # Determine colour
    seed_curr = random.randrange(len(colour_l))
    workingpotion.colour = colour_l[seed_curr]
    seed_list.append(seed_curr)

    # Determine appearance
    seed_curr = random.randrange(len(appearance_l))
    workingpotion.appearance = appearance_l[seed_curr]
    seed_list.append(seed_curr)

    # Determine texture
    seed_curr = random.randrange(len(texture_l))
    workingpotion.texture = texture_l[seed_curr]
    seed_list.append(seed_curr)

    # Determine taste
    seed_curr = random.randrange(len(taste_l))
    workingpotion.taste = taste_l[seed_curr]
    seed_list.append(seed_curr)

    # Determine smell
    seed_curr = random.randrange(len(taste_l))
    workingpotion.smell = taste_l[seed_curr]
    seed_list.append(seed_curr)

    # Determine label
    seed_curr = random.randrange(len(label_l))
    workingpotion.label = label_l[seed_curr]
    seed_list.append(seed_curr)

    workingpotion.seed = seed_list
    return workingpotion


def main(argv):
    pass


if __name__ == '__main__':
    status = 0
    # Set up arguments
    parser = argparse.ArgumentParser(description='''Generate random potions for DnD 5e.''')
    parser.add_argument("n", type=int, nargs="?", default=1)   # Add optional argument
    args = parser.parse_args()

    # Run potion generation
    main(args)

    # Exit
    sys.exit(status)
