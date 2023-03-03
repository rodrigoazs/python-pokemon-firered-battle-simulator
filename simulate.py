from battle_ai_switch_items import modulate_by_type_effectiveness
from pokemon import BattlePokemon, calculate_base_damage

attacker = BattlePokemon(
    level=10,
    attack=16,
    defense=20,
    speed=17,
    sp_attack=15,
    sp_defense=17,
    ability="ABILITY_TORRENT",
    stat_stages={
        "STAT_HP": 0,
        "STAT_ATK": 0,
        "STAT_DEF": 0,
        "STAT_SPEED": 0,
        "STAT_SPATK": 0,
        "STAT_SPDEF": 0,
    },
    type1="TYPE_WATER",
)
defender = BattlePokemon(
    level=10,
    attack=16,
    defense=20,
    speed=17,
    sp_attack=15,
    sp_defense=17,
    ability="ABILITY_TORRENT",
    stat_stages={
        "STAT_HP": 0,
        "STAT_ATK": 0,
        "STAT_DEF": 0,
        "STAT_SPEED": 0,
        "STAT_SPATK": 0,
        "STAT_SPDEF": 0,
    },
    type1="TYPE_FIRE",
    type2="TYPE_ROCK",
)

damage = calculate_base_damage(
    attacker=attacker,
    defender=defender,
    move="MOVE_TACKLE",
    side_status=[],
    power_override=None,
    type_override=None,
    battler_id_atk=None,
    battler_id_def=None,
    environment={"g_crit_multiplier": 1},
)

damage *= modulate_by_type_effectiveness(attacker.type1, defender.type1, defender.type2)


print(f"damage: {damage}")
