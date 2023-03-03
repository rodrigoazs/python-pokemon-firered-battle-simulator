from pokemon import *

attacker = BattlePokemon(
    level=10,
    attack=16,
    defense=20,
    speed=17,
    sp_attack=15,
    sp_defense=17,
    ability="ABILITY_TORRENT",
)
defender = BattlePokemon(
    level=10,
    attack=16,
    defense=20,
    speed=17,
    sp_attack=15,
    sp_defense=17,
    ability="ABILITY_TORRENT",
)

damage = calculate_base_damage(
    attacker=attacker,
    defender=defender,
    move="MOVE_TACKLE",
    side_status=None,
    power_override=None,
    type_override=None,
    battler_id_atk=None,
    battler_id_def=None,
)

print(f"damage: {damage}")
