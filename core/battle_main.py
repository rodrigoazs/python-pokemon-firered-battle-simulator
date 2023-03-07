import random

from core.battle_moves import G_BATTLE_MOVES
from core.pokemon import BattlePokemon

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


def get_who_strikes_first(
    battler1: BattlePokemon,
    battler2: BattlePokemon,
    move_battler1: str = "MOVE_NONE",
    move_battler2: str = "MOVE_NONE",
    ignore_chosen_moves: bool = True,
    environment: dict = {},
):
    speed_multiplier_battler1 = 0
    speed_multiplier_battler2 = 0
    speed_battler1 = 0
    speed_battler2 = 0
    move_battler1 = 0
    move_battler2 = 0

    # environment
    weather_has_effect = environment.get("weather_has_effect", False)
    g_battle_weather = environment.get("g_battle_weather", None)

    if weather_has_effect:
        if (
            battler1.ability == "ABILITY_SWIFT_SWIM"
            and g_battle_weather == "B_WEATHER_RAIN"
            or battler1.ability == "ABILITY_CHLOROPHYLL"
            and g_battle_weather == "B_WEATHER_SUN"
        ):
            speed_multiplier_battler1 = 2
        else:
            speed_multiplier_battler1 = 1
        if (
            battler2.ability == "ABILITY_SWIFT_SWIM"
            and g_battle_weather == "B_WEATHER_RAIN"
            or battler2.ability == "ABILITY_CHLOROPHYLL"
            and g_battle_weather == "B_WEATHER_SUN"
        ):
            speed_multiplier_battler2 = 2
        else:
            speed_multiplier_battler2 = 1
    else:
        speed_multiplier_battler1 = 1
        speed_multiplier_battler2 = 1

    ratio_el = G_STAT_STAGE_RATIOS[battler1.stat_stages["STAT_SPEED"] + 6]
    speed_battler1 = (
        battler1.speed * speed_multiplier_battler1 * ratio_el[0] / ratio_el[1]
    )

    #     if (gBattleMons[battler1].item == ITEM_ENIGMA_BERRY)
    #     {
    #         holdEffect = gEnigmaBerries[battler1].holdEffect;
    #         holdEffectParam = gEnigmaBerries[battler1].holdEffectParam;
    #     }
    #     else
    #     {
    #         holdEffect = ItemId_GetHoldEffect(gBattleMons[battler1].item);
    #         holdEffectParam = ItemId_GetHoldEffectParam(gBattleMons[battler1].item);
    #     }
    #     // badge boost
    #     if (!(gBattleTypeFlags & BATTLE_TYPE_LINK)
    #      && FlagGet(FLAG_BADGE03_GET)
    #      && GetBattlerSide(battler1) == B_SIDE_PLAYER)
    #         speedBattler1 = (speedBattler1 * 110) / 100;
    #     if (holdEffect == HOLD_EFFECT_MACHO_BRACE)
    #         speedBattler1 /= 2;
    #     if (gBattleMons[battler1].status1 & STATUS1_PARALYSIS)
    #         speedBattler1 /= 4;
    #     if (holdEffect == HOLD_EFFECT_QUICK_CLAW && gRandomTurnNumber < (0xFFFF * holdEffectParam) / 100)
    #         speedBattler1 = UINT_MAX;

    # check second battlerId's speed
    ratio_el = G_STAT_STAGE_RATIOS[battler2.stat_stages["STAT_SPEED"] + 6]
    speed_battler1 = (
        battler2.speed * speed_multiplier_battler2 * ratio_el[0] / ratio_el[1]
    )

    #     if (gBattleMons[battler2].item == ITEM_ENIGMA_BERRY)
    #     {
    #         holdEffect = gEnigmaBerries[battler2].holdEffect;
    #         holdEffectParam = gEnigmaBerries[battler2].holdEffectParam;
    #     }
    #     else
    #     {
    #         holdEffect = ItemId_GetHoldEffect(gBattleMons[battler2].item);
    #         holdEffectParam = ItemId_GetHoldEffectParam(gBattleMons[battler2].item);
    #     }
    #     // badge boost
    #     if (!(gBattleTypeFlags & BATTLE_TYPE_LINK)
    #      && FlagGet(FLAG_BADGE03_GET)
    #      && GetBattlerSide(battler2) == B_SIDE_PLAYER)
    #         speedBattler2 = (speedBattler2 * 110) / 100;
    #     if (holdEffect == HOLD_EFFECT_MACHO_BRACE)
    #         speedBattler2 /= 2;
    #     if (gBattleMons[battler2].status1 & STATUS1_PARALYSIS)
    #         speedBattler2 /= 4;
    #     if (holdEffect == HOLD_EFFECT_QUICK_CLAW && gRandomTurnNumber < (0xFFFF * holdEffectParam) / 100)
    #         speedBattler2 = UINT_MAX;

    if ignore_chosen_moves:
        move_battler1 = "MOVE_NONE"
        move_battler2 = "MOVE_NONE"

    # both move priorities are different than 0
    # TODO: in C code values are inverted??
    if (
        G_BATTLE_MOVES[move_battler1]["priority"] != 0
        or G_BATTLE_MOVES[move_battler2]["priority"] != 0
    ):
        # both priorities are the same
        if (
            G_BATTLE_MOVES[move_battler1]["priority"]
            == G_BATTLE_MOVES[move_battler2]["priority"]
        ):
            if speed_battler1 == speed_battler2:
                return random.randint(1, 2)  # same speeds, same priorities
            elif speed_battler1 < speed_battler2:
                return 2  # battler2 has more speed
            else:
                return 1  # battler1 has more speed
        elif (
            G_BATTLE_MOVES[move_battler1]["priority"]
            < G_BATTLE_MOVES[move_battler2]["priority"]
        ):
            return 2
        else:
            return 1
    # both priorities are equal to 0
    else:
        if speed_battler1 == speed_battler2:
            return random.randint(1, 2)  # same speeds, same priorities
        elif speed_battler1 < speed_battler2:
            return 2  # battler2 has more speed
        else:
            return 1  # battler1 has more speed
