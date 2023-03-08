from core.battle_ai_switch_items import modulate_by_type_effectiveness
from core.battle_main import get_who_strikes_first
from core.battle_moves import G_BATTLE_MOVES
from core.battle_script_commands import (
    apply_random_dmg_multiplier,
    cmd_accuracy_check,
    modulate_by_stab,
)
from core.pokemon import BattlePokemon, calculate_base_damage


class Battle:
    def __init__(self, battler1: BattlePokemon, battler2: BattlePokemon):
        self.battlers = (battler1, battler2)
        self._set_who_strikes_first()

    def _get_attacker(self):
        return self.battlers[self.battler_turn]

    def _get_defender(self):
        return self.battlers[(self.battler_turn + 1) % 2]

    def _set_who_strikes_first(self):
        battler_first = get_who_strikes_first(self.battlers[0], self.battlers[1])
        self.battler_turn = battler_first - 1

    def move(self, move_index: int):
        attacker = self._get_attacker()
        defender = self._get_defender()
        move = attacker.moves[move_index]

        if cmd_accuracy_check(attacker, defender, move):
            # calculate damage
            damage = calculate_base_damage(
                attacker=attacker,
                defender=defender,
                move=move,
            )
            type_efectiveness = modulate_by_type_effectiveness(
                attacker.type1, defender.type1, defender.type2
            )
            stab = modulate_by_stab(attacker, G_BATTLE_MOVES[move]["type"])
            final_damage = int(
                apply_random_dmg_multiplier(damage * type_efectiveness * stab)
            )

            # apply damage
            print("attacked by ", final_damage)
            defender.hp = max([0, defender.hp - final_damage])

        self.battler_turn = (self.battler_turn + 1) % 2

    def end_of_battle(self):
        battler1 = self.battlers[0]
        battler2 = self.battlers[1]
        if battler1.hp == 0 or battler2.hp == 0:
            return True
        return False
