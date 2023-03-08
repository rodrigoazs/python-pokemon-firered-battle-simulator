import random

from core.battle_constants import G_STAT_STAGE_RATIOS
from core.battle_moves import G_BATTLE_MOVES
from core.pokemon import BattlePokemon


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

    ratio = G_STAT_STAGE_RATIOS[battler1.stat_stages["STAT_SPEED"] + 6]
    speed_battler1 = battler1.speed * speed_multiplier_battler1 * ratio

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
    ratio = G_STAT_STAGE_RATIOS[battler2.stat_stages["STAT_SPEED"] + 6]
    speed_battler2 = battler2.speed * speed_multiplier_battler2 * ratio

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
