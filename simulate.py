from core.battle import Battle
from core.pokemon import BattlePokemon

battler1 = BattlePokemon(
    level=21,
    attack=36,
    defense=45,
    speed=37,
    sp_attack=33,
    sp_defense=38,
    hp=36,
    max_hp=36,
    ability="ABILITY_TORRENT",
    stat_stages={
        "STAT_HP": 0,
        "STAT_ATK": 0,
        "STAT_DEF": 0,
        "STAT_SPEED": 0,
        "STAT_SPATK": 0,
        "STAT_SPDEF": 0,
        "STAT_ACC": 0,
        "STAT_EVASION": 0,
    },
    type1="TYPE_WATER",
    type2="TYPE_NONE",
    moves=["MOVE_TACKLE", "MOVE_WATER_GUN", "MOVE_BUBBLE", "MOVE_WITHDRAW"],
)

battler2 = BattlePokemon(
    level=21,
    attack=36,
    defense=45,
    speed=37,
    sp_attack=33,
    sp_defense=38,
    hp=36,
    max_hp=36,
    ability="ABILITY_TORRENT",
    stat_stages={
        "STAT_HP": 0,
        "STAT_ATK": 0,
        "STAT_DEF": 0,
        "STAT_SPEED": 0,
        "STAT_SPATK": 0,
        "STAT_SPDEF": 0,
        "STAT_ACC": 0,
        "STAT_EVASION": 0,
    },
    type1="TYPE_WATER",
    type2="TYPE_NONE",
    moves=["MOVE_TACKLE", "MOVE_WATER_GUN", "MOVE_BUBBLE", "MOVE_WITHDRAW"],
)

battle = Battle(battler1, battler2)
battle.move(0)
print(battler1)
print(battler2)
battle.move(0)
print(battler1)
print(battler2)
