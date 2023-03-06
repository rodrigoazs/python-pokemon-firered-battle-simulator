from core.battle_main import G_TYPE_EFFECTIVENESS


def modulate_by_type_effectiveness(atk_type: str, def_type1: str, def_type2: str):
    multiplier = G_TYPE_EFFECTIVENESS.get((atk_type, def_type1), 1.0)
    if def_type1 != def_type2:
        multiplier *= G_TYPE_EFFECTIVENESS.get((atk_type, def_type2), 1.0)
    return multiplier
