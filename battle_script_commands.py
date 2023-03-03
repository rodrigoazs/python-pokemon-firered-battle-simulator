import random


# Multiplies the damage by a random factor between 85% to 100% inclusive
# TODO: int can be applied only in the end of calculation
def apply_random_dmg_multiplier(damage):
    if not damage:
        return damage
    damage = damage * int(random.randint(85, 100) / 100)
    return max([1, damage])
