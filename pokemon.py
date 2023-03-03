from dataclasses import dataclass, field

from battle_moves import G_BATTLE_MOVES

# TODO: remove bitwise operators
STATUS1_BURN = 1 << 4
SIDE_STATUS_REFLECT = 1 << 0

# TODO: collect from external
WEATHER_HAS_EFFECT2 = False


@dataclass
class BattlePokemon:
    species: int | None = None
    attack: int = 0
    defense: int = 0
    speed: int = 0
    sp_attack: int = 0
    sp_defense: int = 0
    moves: list[str] = list[None, None, None, None]
    # /*0x14*/ u32 hpIV:5;
    # /*0x14*/ u32 attackIV:5;
    # /*0x15*/ u32 defenseIV:5;
    # /*0x15*/ u32 speedIV:5;
    # /*0x16*/ u32 spAttackIV:5;
    # /*0x17*/ u32 spDefenseIV:5;
    # /*0x17*/ u32 isEgg:1;
    # /*0x17*/ u32 abilityNum:1;
    # /*0x18*/ s8 statStages[BATTLE_STATS_NO];
    stat_stages: dict = field(
        default_factory=lambda: {
            "STAT_HP": 0,
            "STAT_ATK": 0,
            "STAT_DEF": 0,
            "STAT_SPEED": 0,
            "STAT_SPATK": 0,
            "STAT_SPDEF": 0,
        }
    )
    # /*0x20*/ u8 ability;
    ability: str = None
    # /*0x21*/ u8 type1;
    # /*0x22*/ u8 type2;
    # /*0x23*/ u8 unknown;
    # /*0x24*/ u8 pp[4];
    # /*0x28*/ u16 hp;
    # /*0x2A*/ u8 level;
    level: int = 1
    # /*0x2B*/ u8 friendship;
    # /*0x2C*/ u16 maxHP;
    max_hp: int | None = None
    # /*0x2E*/ u16 item;
    # /*0x30*/ u8 nickname[POKEMON_NAME_LENGTH + 1];
    # /*0x3B*/ u8 ppBonuses;
    # /*0x3C*/ u8 otName[8];
    # /*0x44*/ u32 experience;
    # /*0x48*/ u32 personality;
    # /*0x4C*/ u32 status1;
    status1: int = 0
    # /*0x50*/ u32 status2;
    status2: int = 0
    # /*0x54*/ u32 otId;


@dataclass
class External:
    g_crit_multiplier: int = 1


def is_type_physical(type_):
    return type_ in [
        "TYPE_NORMAL",
        "TYPE_FIGHTING",
        "TYPE_FLYING",
        "TYPE_POISON",
        "TYPE_GROUND",
        "TYPE_ROCK",
        "TYPE_BUG",
        "TYPE_GHOST",
        "TYPE_STEEL",
    ]


def is_type_special(type_):
    return type_ in [
        "TYPE_FIRE",
        "TYPE_WATER",
        "TYPE_GRASS",
        "TYPE_ELECTRIC",
        "TYPE_PSYCHIC",
        "TYPE_ICE",
        "TYPE_DRAGON",
        "TYPE_DARK",
    ]


G_STAT_STAGE_RATIOS = [
    (10, 40),
    (10, 35),
    (10, 30),
    (10, 25),
    (10, 20),
    (10, 15),
    (10, 10),
    (15, 10),
    (20, 10),
    (25, 10),
    (30, 10),
    (35, 10),
    (40, 10),
    (138, 174),
    (108, 120),
]


def apply_stat_mod(var: int, mon: BattlePokemon, stat: int, stat_index: str):
    var = stat * G_STAT_STAGE_RATIOS[mon.stat_stages[stat_index]][0]
    var /= G_STAT_STAGE_RATIOS[mon.stat_stages[stat_index]][1]
    return var


# s32 CalculateBaseDamage(struct BattlePokemon *attacker, struct BattlePokemon *defender, u32 move, u16 sideStatus, u16 powerOverride, u8 typeOverride, u8 battlerIdAtk, u8 battlerIdDef)
def calculate_base_damage(
    attacker: dict,
    defender: dict,
    move: str,
    side_status: int,
    power_override: int = None,
    type_override: str = None,
    battler_id_atk: int = None,
    battler_id_def: int = None,
    external: External = External(),
):
    #     u32 i;
    #     s32 damage = 0;
    #     s32 damageHelper;
    #     u8 type;
    #     u16 attack, defense;
    #     u16 spAttack, spDefense;
    #     u8 defenderHoldEffect;
    #     u8 defenderHoldEffectParam;
    #     u8 attackerHoldEffect;
    #     u8 attackerHoldEffectParam;
    damage = 0
    damage_helper = 0

    g_battle_move_power = (
        power_override if power_override else G_BATTLE_MOVES[move]["power"]
    )

    #     if (!typeOverride)
    #         type = gBattleMoves[move].type;
    #     else
    #         type = typeOverride & 0x3F;
    type_ = type_override if type_override else G_BATTLE_MOVES[move]["type"]

    attack = attacker.attack
    defense = defender.defense
    sp_attack = attacker.sp_attack
    sp_defense = defender.sp_defense

    #     if (attacker->item == ITEM_ENIGMA_BERRY)
    #     {
    #         attackerHoldEffect = gEnigmaBerries[battlerIdAtk].holdEffect;
    #         attackerHoldEffectParam = gEnigmaBerries[battlerIdAtk].holdEffectParam;
    #     }
    #     else
    #     {
    #         attackerHoldEffect = ItemId_GetHoldEffect(attacker->item);
    #         attackerHoldEffectParam = ItemId_GetHoldEffectParam(attacker->item);
    #     }

    #     if (defender->item == ITEM_ENIGMA_BERRY)
    #     {
    #         defenderHoldEffect = gEnigmaBerries[battlerIdDef].holdEffect;
    #         defenderHoldEffectParam = gEnigmaBerries[battlerIdDef].holdEffectParam;
    #     }
    #     else
    #     {
    #         defenderHoldEffect = ItemId_GetHoldEffect(defender->item);
    #         defenderHoldEffectParam = ItemId_GetHoldEffectParam(defender->item);
    #     }

    if (
        attacker.ability == "ABILITY_HUGE_POWER"
        or attacker.ability == "ABILITY_PURE_POWER"
    ):
        attack *= 2

    #     // In FRLG, the Battle Tower and opponent checks are stubbed here.
    #     if (!(gBattleTypeFlags & (BATTLE_TYPE_LINK | /*BATTLE_TYPE_BATTLE_TOWER |*/ BATTLE_TYPE_EREADER_TRAINER)))
    #     {
    #         if (FlagGet(FLAG_BADGE01_GET)
    #             && GetBattlerSide(battlerIdAtk) == B_SIDE_PLAYER)
    #             attack = (110 * attack) / 100;
    #     }
    #     if (!(gBattleTypeFlags & (BATTLE_TYPE_LINK | /*BATTLE_TYPE_BATTLE_TOWER |*/ BATTLE_TYPE_EREADER_TRAINER)))
    #     {
    #         if (FlagGet(FLAG_BADGE05_GET)
    #             && GetBattlerSide(battlerIdDef) == B_SIDE_PLAYER)
    #             defense = (110 * defense) / 100;
    #     }
    #     if (!(gBattleTypeFlags & (BATTLE_TYPE_LINK | /*BATTLE_TYPE_BATTLE_TOWER |*/ BATTLE_TYPE_EREADER_TRAINER)))
    #     {
    #         if (FlagGet(FLAG_BADGE07_GET)
    #             && GetBattlerSide(battlerIdAtk) == B_SIDE_PLAYER)
    #             spAttack = (110 * spAttack) / 100;
    #     }
    #     if (!(gBattleTypeFlags & (BATTLE_TYPE_LINK | /*BATTLE_TYPE_BATTLE_TOWER |*/ BATTLE_TYPE_EREADER_TRAINER)))
    #     {
    #         if (FlagGet(FLAG_BADGE07_GET)
    #             && GetBattlerSide(battlerIdDef) == B_SIDE_PLAYER)
    #             spDefense = (110 * spDefense) / 100;
    #     }

    #     for (i = 0; i < NELEMS(sHoldEffectToType); i++)
    #     {
    #         if (attackerHoldEffect == sHoldEffectToType[i][0]
    #             && type == sHoldEffectToType[i][1])
    #         {
    #             if (IS_TYPE_PHYSICAL(type))
    #                 attack = (attack * (attackerHoldEffectParam + 100)) / 100;
    #             else
    #                 spAttack = (spAttack * (attackerHoldEffectParam + 100)) / 100;
    #             break;
    #         }
    #     }

    #     if (attackerHoldEffect == HOLD_EFFECT_CHOICE_BAND)
    #         attack = (150 * attack) / 100;
    #     if (attackerHoldEffect == HOLD_EFFECT_SOUL_DEW && !(gBattleTypeFlags & (BATTLE_TYPE_BATTLE_TOWER)) && (attacker->species == SPECIES_LATIAS || attacker->species == SPECIES_LATIOS))
    #         spAttack = (150 * spAttack) / 100;
    #     if (defenderHoldEffect == HOLD_EFFECT_SOUL_DEW && !(gBattleTypeFlags & (BATTLE_TYPE_BATTLE_TOWER)) && (defender->species == SPECIES_LATIAS || defender->species == SPECIES_LATIOS))
    #         spDefense = (150 * spDefense) / 100;
    #     if (attackerHoldEffect == HOLD_EFFECT_DEEP_SEA_TOOTH && attacker->species == SPECIES_CLAMPERL)
    #         spAttack *= 2;
    #     if (defenderHoldEffect == HOLD_EFFECT_DEEP_SEA_SCALE && defender->species == SPECIES_CLAMPERL)
    #         spDefense *= 2;
    #     if (attackerHoldEffect == HOLD_EFFECT_LIGHT_BALL && attacker->species == SPECIES_PIKACHU)
    #         spAttack *= 2;
    #     if (defenderHoldEffect == HOLD_EFFECT_METAL_POWDER && defender->species == SPECIES_DITTO)
    #         defense *= 2;
    #     if (attackerHoldEffect == HOLD_EFFECT_THICK_CLUB && (attacker->species == SPECIES_CUBONE || attacker->species == SPECIES_MAROWAK))
    #         attack *= 2;
    if defender.ability == "ABILITY_THICK_FAT" and (
        type_ == "TYPE_FIRE" or type_ == "TYPE_ICE"
    ):
        sp_attack /= 2
    if attacker.ability == "ABILITY_HUSTLE":
        attack = (150 * attack) / 100

    #     if (attacker->ability == ABILITY_PLUS && ABILITY_ON_FIELD2(ABILITY_MINUS))
    #         spAttack = (150 * spAttack) / 100;
    #     if (attacker->ability == ABILITY_MINUS && ABILITY_ON_FIELD2(ABILITY_PLUS))
    #         spAttack = (150 * spAttack) / 100;
    if attacker.ability == "ABILITY_GUTS" and attacker.status1:
        attack = (150 * attack) / 100
    if defender.ability == "ABILITY_MARVEL_SCALE" and defender.status1:
        defense = (150 * defense) / 100
    #     if (type == TYPE_ELECTRIC && AbilityBattleEffects(ABILITYEFFECT_FIELD_SPORT, 0, 0, ABILITYEFFECT_MUD_SPORT, 0))
    #         gBattleMovePower /= 2;
    #     if (type == TYPE_FIRE && AbilityBattleEffects(ABILITYEFFECT_FIELD_SPORT, 0, 0, ABILITYEFFECT_WATER_SPORT, 0))
    #         gBattleMovePower /= 2;
    if (
        type_ == "TYPE_GRASS"
        and attacker.ability == "ABILITY_OVERGROW"
        and attacker.hp <= (attacker.max_hp / 3)
    ):
        g_battle_move_power = (150 * g_battle_move_power) / 100
    if (
        type_ == "TYPE_FIRE"
        and attacker.ability == "ABILITY_BLAZE"
        and attacker.hp <= (attacker.max_hp / 3)
    ):
        g_battle_move_power = (150 * g_battle_move_power) / 100
    if (
        type_ == "TYPE_WATER"
        and attacker.ability == "ABILITY_TORRENT"
        and attacker.hp <= (attacker.max_hp / 3)
    ):
        g_battle_move_power = (150 * g_battle_move_power) / 100
    if (
        type_ == "TYPE_BUG"
        and attacker.ability == "ABILITY_SWARM"
        and attacker.hp <= (attacker.max_hp / 3)
    ):
        g_battle_move_power = (150 * g_battle_move_power) / 100
    #     if (gBattleMoves[gCurrentMove].effect == EFFECT_EXPLOSION)
    #         defense /= 2;

    # TODO: where g_current_move comes from?
    g_current_move = "MOVE_NONE"
    #################
    if G_BATTLE_MOVES[g_current_move]["effect"] == "EFFECT_EXPLOSION":
        defense /= 2

    if is_type_physical(type_):
        if external.g_crit_multiplier == 2:
            if attacker.stat_stages["STAT_ATK"] > 6:
                damage = apply_stat_mod(damage, attacker, attack, "STAT_ATK")
            else:
                damage = attack
        else:
            damage = apply_stat_mod(damage, attacker, attack, "STAT_ATK")

        damage = damage * g_battle_move_power
        damage *= 2 * attacker.level / 5 + 2

        if external.g_crit_multiplier == 2:
            if defender.stat_stages["STAT_DEF"] < 6:
                damage_helper = apply_stat_mod(
                    damage_helper, defender, defense, "STAT_DEF"
                )
            else:
                damage_helper = defense
        else:
            damage_helper = apply_stat_mod(damage_helper, defender, defense, "STAT_DEF")

        damage /= damage_helper
        damage /= 50

        if (attacker.status1 & STATUS1_BURN) and attacker.ability != "ABILITY_GUTS":
            damage /= 2

        # if (side_status & SIDE_STATUS_REFLECT) and external.g_crit_multiplier == 1:
        #     if False:
        #         damage = 2 * (damage / 3)
        #     else:
        #         damage /= 2

        #     if ((sideStatus & SIDE_STATUS_REFLECT) && gCritMultiplier == 1)
        #     {
        #         if ((gBattleTypeFlags & BATTLE_TYPE_DOUBLE) && CountAliveMonsInBattle(BATTLE_ALIVE_DEF_SIDE) == 2)
        #             damage = 2 * (damage / 3);
        #         else
        #             damage /= 2;
        #     }

        #     if ((gBattleTypeFlags & BATTLE_TYPE_DOUBLE) && gBattleMoves[move].target == 8 && CountAliveMonsInBattle(BATTLE_ALIVE_DEF_SIDE) == 2)
        #         damage /= 2;

        # moves always do at least 1 damage.
        damage = max([1, damage])

    if type_ == "TYPE_MYSTERY":
        damage = 0  # is ??? type. does 0 damage.

    if is_type_special(type_):
        if external.g_crit_multiplier == 2:
            if attacker.stat_stages["STAT_SPATK"] > 6:
                damage = apply_stat_mod(damage, attacker, sp_attack, "STAT_SPATK")
            else:
                damage = sp_attack
        else:
            damage = apply_stat_mod(damage, attacker, sp_attack, "STAT_SPATK")

        damage *= g_battle_move_power
        damage *= 2 * attacker.level / 5 + 2

        if external.g_crit_multiplier == 2:
            if defender.stat_stages["STAT_SPDEF"] < 6:
                damage_helper = apply_stat_mod(
                    damage_helper, defender, sp_defense, "STAT_SPDEF"
                )
            else:
                damage_helper = sp_defense
        else:
            damage_helper = apply_stat_mod(
                damage_helper, defender, sp_defense, "STAT_SPDEF"
            )

        damage /= damage_helper
        damage /= 50

    #         if ((sideStatus & SIDE_STATUS_LIGHTSCREEN) && gCritMultiplier == 1)
    #         {
    #             if ((gBattleTypeFlags & BATTLE_TYPE_DOUBLE) && CountAliveMonsInBattle(BATTLE_ALIVE_DEF_SIDE) == 2)
    #                 damage = 2 * (damage / 3);
    #             else
    #                 damage /= 2;
    #         }

    #         if ((gBattleTypeFlags & BATTLE_TYPE_DOUBLE) && gBattleMoves[move].target == 8 && CountAliveMonsInBattle(BATTLE_ALIVE_DEF_SIDE) == 2)
    #             damage /= 2;

    #         // are effects of weather negated with cloud nine or air lock
    #         if (WEATHER_HAS_EFFECT2)
    #         {
    #             if (gBattleWeather & B_WEATHER_RAIN_TEMPORARY)
    #             {
    #                 switch (type)
    #                 {
    #                 case TYPE_FIRE:
    #                     damage /= 2;
    #                     break;
    #                 case TYPE_WATER:
    #                     damage = (15 * damage) / 10;
    #                     break;
    #                 }
    #             }

    #             // any weather except sun weakens solar beam
    #             if ((gBattleWeather & (B_WEATHER_RAIN | B_WEATHER_SANDSTORM | B_WEATHER_HAIL_TEMPORARY)) && gCurrentMove == MOVE_SOLAR_BEAM)
    #                 damage /= 2;

    #             // sunny
    #             if (gBattleWeather & B_WEATHER_SUN)
    #             {
    #                 switch (type)
    #                 {
    #                 case TYPE_FIRE:
    #                     damage = (15 * damage) / 10;
    #                     break;
    #                 case TYPE_WATER:
    #                     damage /= 2;
    #                     break;
    #                 }
    #             }
    #         }

    #         // flash fire triggered
    #         if ((gBattleResources->flags->flags[battlerIdAtk] & RESOURCE_FLAG_FLASH_FIRE) && type == TYPE_FIRE)
    #             damage = (15 * damage) / 10;
    #     }
    return damage + 2
