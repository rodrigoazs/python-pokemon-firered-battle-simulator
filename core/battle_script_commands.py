import random

from core.pokemon import BattlePokemon


# Multiplies the damage by a random factor between 85% to 100% inclusive
# TODO: int can be applied only in the end of calculation
def apply_random_dmg_multiplier(damage):
    if not damage:
        return damage
    damage *= random.randint(85, 100) / 100
    return max([1, damage])


def is_battler_of_type(battler: BattlePokemon, type_: str):
    return battler.type1 == type_ or battler.type2 == type_


# check stab
def modulate_by_stab(attacker: BattlePokemon, move_type: str):
    return 1.5 if is_battler_of_type(attacker, move_type) else 1.0
