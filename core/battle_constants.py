# 20 is ×2.0 TYPE_MUL_SUPER_EFFECTIVE
# 10 is ×1.0 TYPE_MUL_NORMAL
# 05 is ×0.5 TYPE_MUL_NOT_EFFECTIVE
# 00 is ×0.0 TYPE_MUL_NO_EFFECT


G_TYPE_EFFECTIVENESS = {
    ("TYPE_NORMAL", "TYPE_ROCK"): 0.5,
    ("TYPE_NORMAL", "TYPE_STEEL"): 0.5,
    ("TYPE_FIRE", "TYPE_FIRE"): 0.5,
    ("TYPE_FIRE", "TYPE_WATER"): 0.5,
    ("TYPE_FIRE", "TYPE_GRASS"): 2.0,
    ("TYPE_FIRE", "TYPE_ICE"): 2.0,
    ("TYPE_FIRE", "TYPE_BUG"): 2.0,
    ("TYPE_FIRE", "TYPE_ROCK"): 0.5,
    ("TYPE_FIRE", "TYPE_DRAGON"): 0.5,
    ("TYPE_FIRE", "TYPE_STEEL"): 2.0,
    ("TYPE_WATER", "TYPE_FIRE"): 2.0,
    ("TYPE_WATER", "TYPE_WATER"): 0.5,
    ("TYPE_WATER", "TYPE_GRASS"): 0.5,
    ("TYPE_WATER", "TYPE_GROUND"): 2.0,
    ("TYPE_WATER", "TYPE_ROCK"): 2.0,
    ("TYPE_WATER", "TYPE_DRAGON"): 0.5,
    ("TYPE_ELECTRIC", "TYPE_WATER"): 2.0,
    ("TYPE_ELECTRIC", "TYPE_ELECTRIC"): 0.5,
    ("TYPE_ELECTRIC", "TYPE_GRASS"): 0.5,
    ("TYPE_ELECTRIC", "TYPE_GROUND"): 0.0,
    ("TYPE_ELECTRIC", "TYPE_FLYING"): 2.0,
    ("TYPE_ELECTRIC", "TYPE_DRAGON"): 0.5,
    ("TYPE_GRASS", "TYPE_FIRE"): 0.5,
    ("TYPE_GRASS", "TYPE_WATER"): 2.0,
    ("TYPE_GRASS", "TYPE_GRASS"): 0.5,
    ("TYPE_GRASS", "TYPE_POISON"): 0.5,
    ("TYPE_GRASS", "TYPE_GROUND"): 2.0,
    ("TYPE_GRASS", "TYPE_FLYING"): 0.5,
    ("TYPE_GRASS", "TYPE_BUG"): 0.5,
    ("TYPE_GRASS", "TYPE_ROCK"): 2.0,
    ("TYPE_GRASS", "TYPE_DRAGON"): 0.5,
    ("TYPE_GRASS", "TYPE_STEEL"): 0.5,
    ("TYPE_ICE", "TYPE_WATER"): 0.5,
    ("TYPE_ICE", "TYPE_GRASS"): 2.0,
    ("TYPE_ICE", "TYPE_ICE"): 0.5,
    ("TYPE_ICE", "TYPE_GROUND"): 2.0,
    ("TYPE_ICE", "TYPE_FLYING"): 2.0,
    ("TYPE_ICE", "TYPE_DRAGON"): 2.0,
    ("TYPE_ICE", "TYPE_STEEL"): 0.5,
    ("TYPE_ICE", "TYPE_FIRE"): 0.5,
    ("TYPE_FIGHTING", "TYPE_NORMAL"): 2.0,
    ("TYPE_FIGHTING", "TYPE_ICE"): 2.0,
    ("TYPE_FIGHTING", "TYPE_POISON"): 0.5,
    ("TYPE_FIGHTING", "TYPE_FLYING"): 0.5,
    ("TYPE_FIGHTING", "TYPE_PSYCHIC"): 0.5,
    ("TYPE_FIGHTING", "TYPE_BUG"): 0.5,
    ("TYPE_FIGHTING", "TYPE_ROCK"): 2.0,
    ("TYPE_FIGHTING", "TYPE_DARK"): 2.0,
    ("TYPE_FIGHTING", "TYPE_STEEL"): 2.0,
    ("TYPE_POISON", "TYPE_GRASS"): 2.0,
    ("TYPE_POISON", "TYPE_POISON"): 0.5,
    ("TYPE_POISON", "TYPE_GROUND"): 0.5,
    ("TYPE_POISON", "TYPE_ROCK"): 0.5,
    ("TYPE_POISON", "TYPE_GHOST"): 0.5,
    ("TYPE_POISON", "TYPE_STEEL"): 0.0,
    ("TYPE_GROUND", "TYPE_FIRE"): 2.0,
    ("TYPE_GROUND", "TYPE_ELECTRIC"): 2.0,
    ("TYPE_GROUND", "TYPE_GRASS"): 0.5,
    ("TYPE_GROUND", "TYPE_POISON"): 2.0,
    ("TYPE_GROUND", "TYPE_FLYING"): 0.0,
    ("TYPE_GROUND", "TYPE_BUG"): 0.5,
    ("TYPE_GROUND", "TYPE_ROCK"): 2.0,
    ("TYPE_GROUND", "TYPE_STEEL"): 2.0,
    ("TYPE_FLYING", "TYPE_ELECTRIC"): 0.5,
    ("TYPE_FLYING", "TYPE_GRASS"): 2.0,
    ("TYPE_FLYING", "TYPE_FIGHTING"): 2.0,
    ("TYPE_FLYING", "TYPE_BUG"): 2.0,
    ("TYPE_FLYING", "TYPE_ROCK"): 0.5,
    ("TYPE_FLYING", "TYPE_STEEL"): 0.5,
    ("TYPE_PSYCHIC", "TYPE_FIGHTING"): 2.0,
    ("TYPE_PSYCHIC", "TYPE_POISON"): 2.0,
    ("TYPE_PSYCHIC", "TYPE_PSYCHIC"): 0.5,
    ("TYPE_PSYCHIC", "TYPE_DARK"): 0.0,
    ("TYPE_PSYCHIC", "TYPE_STEEL"): 0.5,
    ("TYPE_BUG", "TYPE_FIRE"): 0.5,
    ("TYPE_BUG", "TYPE_GRASS"): 2.0,
    ("TYPE_BUG", "TYPE_FIGHTING"): 0.5,
    ("TYPE_BUG", "TYPE_POISON"): 0.5,
    ("TYPE_BUG", "TYPE_FLYING"): 0.5,
    ("TYPE_BUG", "TYPE_PSYCHIC"): 2.0,
    ("TYPE_BUG", "TYPE_GHOST"): 0.5,
    ("TYPE_BUG", "TYPE_DARK"): 2.0,
    ("TYPE_BUG", "TYPE_STEEL"): 0.5,
    ("TYPE_ROCK", "TYPE_FIRE"): 2.0,
    ("TYPE_ROCK", "TYPE_ICE"): 2.0,
    ("TYPE_ROCK", "TYPE_FIGHTING"): 0.5,
    ("TYPE_ROCK", "TYPE_GROUND"): 0.5,
    ("TYPE_ROCK", "TYPE_FLYING"): 2.0,
    ("TYPE_ROCK", "TYPE_BUG"): 2.0,
    ("TYPE_ROCK", "TYPE_STEEL"): 0.5,
    ("TYPE_GHOST", "TYPE_NORMAL"): 0.0,
    ("TYPE_GHOST", "TYPE_PSYCHIC"): 2.0,
    ("TYPE_GHOST", "TYPE_DARK"): 0.5,
    ("TYPE_GHOST", "TYPE_STEEL"): 0.5,
    ("TYPE_GHOST", "TYPE_GHOST"): 2.0,
    ("TYPE_DRAGON", "TYPE_DRAGON"): 2.0,
    ("TYPE_DRAGON", "TYPE_STEEL"): 0.5,
    ("TYPE_DARK", "TYPE_FIGHTING"): 0.5,
    ("TYPE_DARK", "TYPE_PSYCHIC"): 2.0,
    ("TYPE_DARK", "TYPE_GHOST"): 2.0,
    ("TYPE_DARK", "TYPE_DARK"): 0.5,
    ("TYPE_DARK", "TYPE_STEEL"): 0.5,
    ("TYPE_STEEL", "TYPE_FIRE"): 0.5,
    ("TYPE_STEEL", "TYPE_WATER"): 0.5,
    ("TYPE_STEEL", "TYPE_ELECTRIC"): 0.5,
    ("TYPE_STEEL", "TYPE_ICE"): 2.0,
    ("TYPE_STEEL", "TYPE_ROCK"): 2.0,
    ("TYPE_STEEL", "TYPE_STEEL"): 0.5,
    ("TYPE_FORESIGHT", "TYPE_FORESIGHT"): 0.0,
    ("TYPE_NORMAL", "TYPE_GHOST"): 0.0,
    ("TYPE_FIGHTING", "TYPE_GHOST"): 0.0,
}


# TODO: ranges from -6 to 8?
G_STAT_STAGE_RATIOS = [
    10 / 40,
    10 / 35,
    10 / 30,
    10 / 25,
    10 / 20,
    10 / 15,
    10 / 10,
    15 / 10,
    20 / 10,
    25 / 10,
    30 / 10,
    35 / 10,
    40 / 10,
    138 / 174,
    108 / 120,
]

MIN_STAT_STAGE = -6
MAX_STAT_STAGE = 6

S_ACCURACY_STAGE_RATIOS = [
    0.33,  # -6
    0.36,  # -5
    0.43,  # -4
    0.5,  # -3
    0.6,  # -2
    0.75,  # -1
    1.0,  #  0
    1.33,  # +1
    1.66,  # +2
    2.0,  # +3
    2.33,  # +4
    2.66,  # +5
    3.0,  # +6
]
