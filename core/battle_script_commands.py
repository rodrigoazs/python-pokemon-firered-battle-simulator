import random

from core.battle_constants import (
    MAX_STAT_STAGE,
    MIN_STAT_STAGE,
    S_ACCURACY_STAGE_RATIOS,
)
from core.battle_moves import G_BATTLE_MOVES
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


def cmd_accuracy_check(
    attacker: BattlePokemon, target: BattlePokemon, move: str, environment: dict = {}
):
    type_ = G_BATTLE_MOVES[move]["type"]

    # environment
    weather_has_effect = environment.get("weather_has_effect", False)
    g_battle_weather = environment.get("g_battle_weather", None)

    #     u16 move = T2_READ_16(gBattlescriptCurrInstr + 5);

    #     if ((gBattleTypeFlags & BATTLE_TYPE_FIRST_BATTLE
    #         && !BtlCtrl_OakOldMan_TestState2Flag(1)
    #         && gBattleMoves[move].power != 0
    #         && GetBattlerSide(gBattlerAttacker) == B_SIDE_PLAYER)
    #      || (gBattleTypeFlags & BATTLE_TYPE_FIRST_BATTLE
    #         && !BtlCtrl_OakOldMan_TestState2Flag(2)
    #         && gBattleMoves[move].power == 0
    #         && GetBattlerSide(gBattlerAttacker) == B_SIDE_PLAYER)
    #      || (gBattleTypeFlags & BATTLE_TYPE_POKEDUDE))
    #     {
    #         JumpIfMoveFailed(7, move);
    #         return;
    #     }
    #     if (move == NO_ACC_CALC || move == NO_ACC_CALC_CHECK_LOCK_ON)
    #     {
    #         if (gStatuses3[gBattlerTarget] & STATUS3_ALWAYS_HITS && move == NO_ACC_CALC_CHECK_LOCK_ON && gDisableStructs[gBattlerTarget].battlerWithSureHit == gBattlerAttacker)
    #             gBattlescriptCurrInstr += 7;
    #         else if (gStatuses3[gBattlerTarget] & (STATUS3_ON_AIR | STATUS3_UNDERGROUND | STATUS3_UNDERWATER))
    #             gBattlescriptCurrInstr = T1_READ_PTR(gBattlescriptCurrInstr + 1);
    #         else if (!JumpIfMoveAffectedByProtect(0))
    #             gBattlescriptCurrInstr += 7;
    #     }
    #     else
    #     {
    #         u8 type, moveAcc, holdEffect, param;
    #         s8 buff;
    #         u16 calc;

    #         if (move == ACC_CURR_MOVE)
    #             move = gCurrentMove;

    #         GET_MOVE_TYPE(move, type);

    #         if (JumpIfMoveAffectedByProtect(move))
    #             return;
    #         if (AccuracyCalcHelper(move))
    #             return;

    if target.status2 == "STATUS2_FORESIGHT":
        acc = attacker.stat_stages["STAT_ACC"]
        buff = acc
    else:
        acc = attacker.stat_stages["STAT_ACC"]
        buff = acc + target.stat_stages["STAT_EVASION"]

    buff = min([max([MIN_STAT_STAGE, buff]), MAX_STAT_STAGE])

    move_acc = G_BATTLE_MOVES[move]["accuracy"]

    # check Thunder on sunny weather
    if (
        weather_has_effect
        and g_battle_weather == "B_WEATHER_SUN"
        and G_BATTLE_MOVES[move]["effect"] == "EFFECT_THUNDER"
    ):
        move_acc = 50

    calc = move_acc * S_ACCURACY_STAGE_RATIOS[int(buff)]

    if attacker.ability == "ABILITY_COMPOUND_EYES":
        calc = calc * 1.3  # 1.3 compound eyes boost
    if (
        weather_has_effect
        and target.ability == "ABILITY_SAND_VEIL"
        and g_battle_weather == "B_WEATHER_SANDSTORM"
    ):
        calc = calc * 0.8  # 1.2 sand veil loss
    if attacker.ability == "ABILITY_HUSTLE" and is_type_physical(type_):
        calc = calc * 0.8  # 1.2 hustle loss

    #         if (gBattleMons[gBattlerTarget].item == ITEM_ENIGMA_BERRY)
    #         {
    #             holdEffect = gEnigmaBerries[gBattlerTarget].holdEffect;
    #             param = gEnigmaBerries[gBattlerTarget].holdEffectParam;
    #         }
    #         else
    #         {
    #             holdEffect = ItemId_GetHoldEffect(gBattleMons[gBattlerTarget].item);
    #             param = ItemId_GetHoldEffectParam(gBattleMons[gBattlerTarget].item);
    #         }

    #         gPotentialItemEffectBattler = gBattlerTarget;

    #         if (holdEffect == HOLD_EFFECT_EVASION_UP)
    #             calc = (calc * (100 - param)) / 100;

    # final calculation
    if random.random() >= int(calc):
        return False  # avoided or missed
    #             gMoveResultFlags |= MOVE_RESULT_MISSED;
    #             if (gBattleTypeFlags & BATTLE_TYPE_DOUBLE
    #              && (gBattleMoves[move].target == MOVE_TARGET_BOTH || gBattleMoves[move].target == MOVE_TARGET_FOES_AND_ALLY))
    #                 gBattleCommunication[MISS_TYPE] = B_MSG_AVOIDED_ATK;
    #             else
    #                 gBattleCommunication[MISS_TYPE] = B_MSG_MISSED;
    #             CheckWonderGuardAndLevitate();
    return True


#         JumpIfMoveFailed(7, move);
