# u8 DoBattlerEndTurnEffects(void)
# {
#     u8 effect = 0;

#     gHitMarker |= (HITMARKER_GRUDGE | HITMARKER_SKIP_DMG_TRACK);
#     while (gBattleStruct->turnEffectsBattlerId < gBattlersCount && gBattleStruct->turnEffectsTracker <= ENDTURN_BATTLER_COUNT)
#     {
#         gActiveBattler = gBattlerAttacker = gBattlerByTurnOrder[gBattleStruct->turnEffectsBattlerId];
#         if (gAbsentBattlerFlags & gBitTable[gActiveBattler])
#         {
#             gBattleStruct->turnEffectsBattlerId++;
#         }
#         else
#         {
#             switch (gBattleStruct->turnEffectsTracker)
#             {
#             case ENDTURN_INGRAIN:  // ingrain
#                 if ((gStatuses3[gActiveBattler] & STATUS3_ROOTED)
#                  && gBattleMons[gActiveBattler].hp != gBattleMons[gActiveBattler].maxHP
#                  && gBattleMons[gActiveBattler].hp != 0)
#                 {
#                     gBattleMoveDamage = gBattleMons[gActiveBattler].maxHP / 16;
#                     if (gBattleMoveDamage == 0)
#                         gBattleMoveDamage = 1;
#                     gBattleMoveDamage *= -1;
#                     BattleScriptExecute(BattleScript_IngrainTurnHeal);
#                     effect++;
#                 }
#                 gBattleStruct->turnEffectsTracker++;
#                 break;
#             case ENDTURN_ABILITIES:  // end turn abilities
#                 if (AbilityBattleEffects(ABILITYEFFECT_ENDTURN, gActiveBattler, 0, 0, 0))
#                     effect++;
#                 gBattleStruct->turnEffectsTracker++;
#                 break;
#             case ENDTURN_ITEMS1:  // item effects
#                 if (ItemBattleEffects(ITEMEFFECT_NORMAL, gActiveBattler, FALSE))
#                     effect++;
#                 gBattleStruct->turnEffectsTracker++;
#                 break;
#             case ENDTURN_ITEMS2:  // item effects again
#                 if (ItemBattleEffects(ITEMEFFECT_NORMAL, gActiveBattler, TRUE))
#                     effect++;
#                 gBattleStruct->turnEffectsTracker++;
#                 break;
#             case ENDTURN_LEECH_SEED:  // leech seed
#                 if ((gStatuses3[gActiveBattler] & STATUS3_LEECHSEED)
#                  && gBattleMons[gStatuses3[gActiveBattler] & STATUS3_LEECHSEED_BATTLER].hp != 0
#                  && gBattleMons[gActiveBattler].hp != 0)
#                 {
#                     gBattlerTarget = gStatuses3[gActiveBattler] & STATUS3_LEECHSEED_BATTLER; // Notice gBattlerTarget is actually the HP receiver.
#                     gBattleMoveDamage = gBattleMons[gActiveBattler].maxHP / 8;
#                     if (gBattleMoveDamage == 0)
#                         gBattleMoveDamage = 1;
#                     gBattleScripting.animArg1 = gBattlerTarget;
#                     gBattleScripting.animArg2 = gBattlerAttacker;
#                     BattleScriptExecute(BattleScript_LeechSeedTurnDrain);
#                     effect++;
#                 }
#                 gBattleStruct->turnEffectsTracker++;
#                 break;
#             case ENDTURN_POISON:  // poison
#                 if ((gBattleMons[gActiveBattler].status1 & STATUS1_POISON) && gBattleMons[gActiveBattler].hp != 0)
#                 {
#                     gBattleMoveDamage = gBattleMons[gActiveBattler].maxHP / 8;
#                     if (gBattleMoveDamage == 0)
#                         gBattleMoveDamage = 1;
#                     BattleScriptExecute(BattleScript_PoisonTurnDmg);
#                     effect++;
#                 }
#                 gBattleStruct->turnEffectsTracker++;
#                 break;
#             case ENDTURN_BAD_POISON:  // toxic poison
#                 if ((gBattleMons[gActiveBattler].status1 & STATUS1_TOXIC_POISON) && gBattleMons[gActiveBattler].hp != 0)
#                 {
#                     gBattleMoveDamage = gBattleMons[gActiveBattler].maxHP / 16;
#                     if (gBattleMoveDamage == 0)
#                         gBattleMoveDamage = 1;
#                     if ((gBattleMons[gActiveBattler].status1 & STATUS1_TOXIC_COUNTER) != STATUS1_TOXIC_TURN(15)) // not 16 turns
#                         gBattleMons[gActiveBattler].status1 += STATUS1_TOXIC_TURN(1);
#                     gBattleMoveDamage *= (gBattleMons[gActiveBattler].status1 & STATUS1_TOXIC_COUNTER) >> 8;
#                     BattleScriptExecute(BattleScript_PoisonTurnDmg);
#                     effect++;
#                 }
#                 gBattleStruct->turnEffectsTracker++;
#                 break;
#             case ENDTURN_BURN:  // burn
#                 if ((gBattleMons[gActiveBattler].status1 & STATUS1_BURN) && gBattleMons[gActiveBattler].hp != 0)
#                 {
#                     gBattleMoveDamage = gBattleMons[gActiveBattler].maxHP / 8;
#                     if (gBattleMoveDamage == 0)
#                         gBattleMoveDamage = 1;
#                     BattleScriptExecute(BattleScript_BurnTurnDmg);
#                     effect++;
#                 }
#                 gBattleStruct->turnEffectsTracker++;
#                 break;
#             case ENDTURN_NIGHTMARES:  // spooky nightmares
#                 if ((gBattleMons[gActiveBattler].status2 & STATUS2_NIGHTMARE) && gBattleMons[gActiveBattler].hp != 0)
#                 {
#                     // R/S does not perform this sleep check, which causes the nightmare effect to
#                     // persist even after the affected Pokemon has been awakened by Shed Skin.
#                     if (gBattleMons[gActiveBattler].status1 & STATUS1_SLEEP)
#                     {
#                         gBattleMoveDamage = gBattleMons[gActiveBattler].maxHP / 4;
#                         if (gBattleMoveDamage == 0)
#                             gBattleMoveDamage = 1;
#                         BattleScriptExecute(BattleScript_NightmareTurnDmg);
#                         effect++;
#                     }
#                     else
#                     {
#                         gBattleMons[gActiveBattler].status2 &= ~STATUS2_NIGHTMARE;
#                     }
#                 }
#                 gBattleStruct->turnEffectsTracker++;
#                 break;
#             case ENDTURN_CURSE:  // curse
#                 if ((gBattleMons[gActiveBattler].status2 & STATUS2_CURSED) && gBattleMons[gActiveBattler].hp != 0)
#                 {
#                     gBattleMoveDamage = gBattleMons[gActiveBattler].maxHP / 4;
#                     if (gBattleMoveDamage == 0)
#                         gBattleMoveDamage = 1;
#                     BattleScriptExecute(BattleScript_CurseTurnDmg);
#                     effect++;
#                 }
#                 gBattleStruct->turnEffectsTracker++;
#                 break;
#             case ENDTURN_WRAP:  // wrap
#                 if ((gBattleMons[gActiveBattler].status2 & STATUS2_WRAPPED) && gBattleMons[gActiveBattler].hp != 0)
#                 {
#                     gBattleMons[gActiveBattler].status2 -= STATUS2_WRAPPED_TURN(1);
#                     if (gBattleMons[gActiveBattler].status2 & STATUS2_WRAPPED)  // damaged by wrap
#                     {
#                         gBattleScripting.animArg1 = *(gBattleStruct->wrappedMove + gActiveBattler * 2 + 0);
#                         gBattleScripting.animArg2 = *(gBattleStruct->wrappedMove + gActiveBattler * 2 + 1);
#                         gBattleTextBuff1[0] = B_BUFF_PLACEHOLDER_BEGIN;
#                         gBattleTextBuff1[1] = B_BUFF_MOVE;
#                         gBattleTextBuff1[2] = *(gBattleStruct->wrappedMove + gActiveBattler * 2 + 0);
#                         gBattleTextBuff1[3] = *(gBattleStruct->wrappedMove + gActiveBattler * 2 + 1);
#                         gBattleTextBuff1[4] = EOS;
#                         gBattlescriptCurrInstr = BattleScript_WrapTurnDmg;
#                         gBattleMoveDamage = gBattleMons[gActiveBattler].maxHP / 16;
#                         if (gBattleMoveDamage == 0)
#                             gBattleMoveDamage = 1;
#                     }
#                     else  // broke free
#                     {
#                         gBattleTextBuff1[0] = B_BUFF_PLACEHOLDER_BEGIN;
#                         gBattleTextBuff1[1] = B_BUFF_MOVE;
#                         gBattleTextBuff1[2] = *(gBattleStruct->wrappedMove + gActiveBattler * 2 + 0);
#                         gBattleTextBuff1[3] = *(gBattleStruct->wrappedMove + gActiveBattler * 2 + 1);
#                         gBattleTextBuff1[4] = EOS;
#                         gBattlescriptCurrInstr = BattleScript_WrapEnds;
#                     }
#                     BattleScriptExecute(gBattlescriptCurrInstr);
#                     effect++;
#                 }
#                 gBattleStruct->turnEffectsTracker++;
#                 break;
#             case ENDTURN_UPROAR:  // uproar
#                 if (gBattleMons[gActiveBattler].status2 & STATUS2_UPROAR)
#                 {
#                     for (gBattlerAttacker = 0; gBattlerAttacker < gBattlersCount; gBattlerAttacker++)
#                     {
#                         if ((gBattleMons[gBattlerAttacker].status1 & STATUS1_SLEEP)
#                          && gBattleMons[gBattlerAttacker].ability != ABILITY_SOUNDPROOF)
#                         {
#                             gBattleMons[gBattlerAttacker].status1 &= ~STATUS1_SLEEP;
#                             gBattleMons[gBattlerAttacker].status2 &= ~STATUS2_NIGHTMARE;
#                             gBattleCommunication[MULTISTRING_CHOOSER] = 1;
#                             BattleScriptExecute(BattleScript_MonWokeUpInUproar);
#                             gActiveBattler = gBattlerAttacker;
#                             BtlController_EmitSetMonData(BUFFER_A, REQUEST_STATUS_BATTLE, 0, 4, &gBattleMons[gActiveBattler].status1);
#                             MarkBattlerForControllerExec(gActiveBattler);
#                             break;
#                         }
#                     }
#                     if (gBattlerAttacker != gBattlersCount)
#                     {
#                         effect = 2;  // a pokemon was awaken
#                         break;
#                     }
#                     else
#                     {
#                         gBattlerAttacker = gActiveBattler;
#                         gBattleMons[gActiveBattler].status2 -= STATUS2_UPROAR_TURN(1);
#                         if (WasUnableToUseMove(gActiveBattler))
#                         {
#                             CancelMultiTurnMoves(gActiveBattler);
#                             gBattleCommunication[MULTISTRING_CHOOSER] = B_MSG_UPROAR_ENDS;
#                         }
#                         else if (gBattleMons[gActiveBattler].status2 & STATUS2_UPROAR)
#                         {
#                             gBattleCommunication[MULTISTRING_CHOOSER] = B_MSG_UPROAR_CONTINUES;
#                             gBattleMons[gActiveBattler].status2 |= STATUS2_MULTIPLETURNS;
#                         }
#                         else
#                         {
#                             gBattleCommunication[MULTISTRING_CHOOSER] = B_MSG_UPROAR_ENDS;
#                             CancelMultiTurnMoves(gActiveBattler);
#                         }
#                         BattleScriptExecute(BattleScript_PrintUproarOverTurns);
#                         effect = 1;
#                     }
#                 }
#                 if (effect != 2)
#                     gBattleStruct->turnEffectsTracker++;
#                 break;
#             case ENDTURN_THRASH:  // thrash
#                 if (gBattleMons[gActiveBattler].status2 & STATUS2_LOCK_CONFUSE)
#                 {
#                     gBattleMons[gActiveBattler].status2 -= STATUS2_LOCK_CONFUSE_TURN(1);
#                     if (WasUnableToUseMove(gActiveBattler))
#                         CancelMultiTurnMoves(gActiveBattler);
#                     else if (!(gBattleMons[gActiveBattler].status2 & STATUS2_LOCK_CONFUSE)
#                      && (gBattleMons[gActiveBattler].status2 & STATUS2_MULTIPLETURNS))
#                     {
#                         gBattleMons[gActiveBattler].status2 &= ~STATUS2_MULTIPLETURNS;
#                         if (!(gBattleMons[gActiveBattler].status2 & STATUS2_CONFUSION))
#                         {
#                             gBattleCommunication[MOVE_EFFECT_BYTE] = MOVE_EFFECT_CONFUSION | MOVE_EFFECT_AFFECTS_USER;
#                             SetMoveEffect(TRUE, 0);
#                             if (gBattleMons[gActiveBattler].status2 & STATUS2_CONFUSION)
#                                 BattleScriptExecute(BattleScript_ThrashConfuses);
#                             effect++;
#                         }
#                     }
#                 }
#                 gBattleStruct->turnEffectsTracker++;
#                 break;
#             case ENDTURN_DISABLE:  // disable
#                 if (gDisableStructs[gActiveBattler].disableTimer != 0)
#                 {
#                     s32 i;
#                     for (i = 0; i < MAX_MON_MOVES; i++)
#                     {
#                         if (gDisableStructs[gActiveBattler].disabledMove == gBattleMons[gActiveBattler].moves[i])
#                             break;
#                     }
#                     if (i == MAX_MON_MOVES)  // pokemon does not have the disabled move anymore
#                     {
#                         gDisableStructs[gActiveBattler].disabledMove = MOVE_NONE;
#                         gDisableStructs[gActiveBattler].disableTimer = 0;
#                     }
#                     else if (--gDisableStructs[gActiveBattler].disableTimer == 0)  // disable ends
#                     {
#                         gDisableStructs[gActiveBattler].disabledMove = MOVE_NONE;
#                         BattleScriptExecute(BattleScript_DisabledNoMore);
#                         effect++;
#                     }
#                 }
#                 gBattleStruct->turnEffectsTracker++;
#                 break;
#             case ENDTURN_ENCORE:  // encore
#                 if (gDisableStructs[gActiveBattler].encoreTimer != 0)
#                 {
#                     if (gBattleMons[gActiveBattler].moves[gDisableStructs[gActiveBattler].encoredMovePos] != gDisableStructs[gActiveBattler].encoredMove)  // pokemon does not have the encored move anymore
#                     {
#                         gDisableStructs[gActiveBattler].encoredMove = MOVE_NONE;
#                         gDisableStructs[gActiveBattler].encoreTimer = 0;
#                     }
#                     else if (--gDisableStructs[gActiveBattler].encoreTimer == 0
#                      || gBattleMons[gActiveBattler].pp[gDisableStructs[gActiveBattler].encoredMovePos] == 0)
#                     {
#                         gDisableStructs[gActiveBattler].encoredMove = MOVE_NONE;
#                         gDisableStructs[gActiveBattler].encoreTimer = 0;
#                         BattleScriptExecute(BattleScript_EncoredNoMore);
#                         effect++;
#                     }
#                 }
#                 gBattleStruct->turnEffectsTracker++;
#                 break;
#             case ENDTURN_LOCK_ON:  // lock-on decrement
#                 if (gStatuses3[gActiveBattler] & STATUS3_ALWAYS_HITS)
#                     gStatuses3[gActiveBattler] -= STATUS3_ALWAYS_HITS_TURN(1);
#                 gBattleStruct->turnEffectsTracker++;
#                 break;
#             case ENDTURN_CHARGE:  // charge
#                 if (gDisableStructs[gActiveBattler].chargeTimer && --gDisableStructs[gActiveBattler].chargeTimer == 0)
#                     gStatuses3[gActiveBattler] &= ~STATUS3_CHARGED_UP;
#                 gBattleStruct->turnEffectsTracker++;
#                 break;
#             case ENDTURN_TAUNT:  // taunt
#                 if (gDisableStructs[gActiveBattler].tauntTimer)
#                     gDisableStructs[gActiveBattler].tauntTimer--;
#                 gBattleStruct->turnEffectsTracker++;
#                 break;
#             case ENDTURN_YAWN:  // yawn
#                 if (gStatuses3[gActiveBattler] & STATUS3_YAWN)
#                 {
#                     gStatuses3[gActiveBattler] -= STATUS3_YAWN_TURN(1);
#                     if (!(gStatuses3[gActiveBattler] & STATUS3_YAWN) && !(gBattleMons[gActiveBattler].status1 & STATUS1_ANY)
#                      && gBattleMons[gActiveBattler].ability != ABILITY_VITAL_SPIRIT
#                      && gBattleMons[gActiveBattler].ability != ABILITY_INSOMNIA && !UproarWakeUpCheck(gActiveBattler))
#                     {
#                         CancelMultiTurnMoves(gActiveBattler);
#                         gBattleMons[gActiveBattler].status1 |= STATUS1_SLEEP_TURN((Random() & 3) + 2); // 2-5 turns of sleep
#                         BtlController_EmitSetMonData(BUFFER_A, REQUEST_STATUS_BATTLE, 0, 4, &gBattleMons[gActiveBattler].status1);
#                         MarkBattlerForControllerExec(gActiveBattler);
#                         gEffectBattler = gActiveBattler;
#                         BattleScriptExecute(BattleScript_YawnMakesAsleep);
#                         effect++;
#                     }
#                 }
#                 gBattleStruct->turnEffectsTracker++;
#                 break;
#             case ENDTURN_BATTLER_COUNT:  // done
#                 gBattleStruct->turnEffectsTracker = 0;
#                 gBattleStruct->turnEffectsBattlerId++;
#                 break;
#             }
#             if (effect != 0)
#                 return effect;
#         }
#     }
#     gHitMarker &= ~(HITMARKER_GRUDGE | HITMARKER_SKIP_DMG_TRACK);
#     return 0;
# }
