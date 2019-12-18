from card import *

def random_choose(person, num, suite_for_this_turn=-1):  # 出牌的人，它剩幾張牌
    cards_on_hand_for_a_suite = person.find_suite(suite_for_this_turn)
    # 第一個出牌，還沒有決定本回合的花色

    if num == 1:
        card_choosed = person.cards_on_hand[0]

    elif len(cards_on_hand_for_a_suite) == 0:
        card_choosed = person.cards_on_hand[random.randint(0, num-1)]

    else:
        card_choosed = cards_on_hand_for_a_suite[random.randint(
            0, len(cards_on_hand_for_a_suite)-1)]

    return card_choosed

class Smart(Player):
    def __init__(self, name):
        super().__init__(name)

    def fst_turn_decide(self, num, person_on_turn, king): # 第一個出牌
        if num == 1:
            return random_choose(self, len(self.cards_on_hand), king)

        # 出數量最少的那個花色，若該花色不是king
        if num == 2:
            suites = []
            min_length = 20

            person_suites = person_on_turn.suites_on_hand()

            for suite in person_suites:
                suites.append(person_on_turn.find_suite(suite))

            for i in range(len(suites)):
                if (len(suites) == 1) and (suites[i][0].suite == king):
                    chosen_suite = suites[i][0]
                elif (len(suites[i]) < min_length) and (suites[i][0].suite != king):
                    min_length = len(suites[i])
                    chosen_suite = suites[i][0]
            
            return chosen_suite

        # 某花色缺牌時，出king。
        if num == 3:
            pass

    def decide(self, num, person_on_turn, person_got_trick, suite_for_this_turn, max_card, teammate_card, opposite_card): # 非第一個出牌
        if num == 1: # 隊友拿到 或 對方拿到 且 沒更大的牌，就出最小
            # length = len(self.cards_on_hand()

            if self.teammate == person_got_trick:
                if suite_for_this_turn in person_on_turn.suites_on_hand():
                    suites_on_hand = person_on_turn.find_suite(suite_for_this_turn)
                    return suites_on_hand[0]
                else:
                    person_on_turn.arrange(get_key2)
                    cards = person_on_turn.cards_on_hand
                    return cards[0]
            else:
                if suite_for_this_turn in person_on_turn.suites_on_hand():
                    suites_on_hand = person_on_turn.find_suite(suite_for_this_turn)
                    if suites_on_hand[len(suites_on_hand) - 1].face < max_card.face:
                        return suites_on_hand[0]
                    else:
                        return suites_on_hand[len(suites_on_hand) - 1]
                else:
                    person_on_turn.arrange(get_key2)
                    cards = person_on_turn.cards_on_hand
                    if cards[len(cards) - 1].face < max_card.face:
                        return cards[0]
                    else:
                        return cards[len(cards) - 1]
                
        # 如果我的夥伴出JQK，我就出相同花色最小的（除了king)
        if num == 2:
            if teammate_card == 11 or 12 or 13:
                if suite_for_this_turn in person_on_turn.suites_on_hand():
                    suites_on_hand = person_on_turn.find_suite(suite_for_this_turn)
                    return suites_on_hand[0]
                else:
                    person_on_turn.arrange(get_key2)
                    cards = person_on_turn.cards_on_hand
                    return cards[0]
            else:
                return random_choose(self, len(self.cards_on_hand), suite_for_this_turn)
        
        # 如果對方出JQKA，且自己沒有更大的牌時，出最小。
        if num == 3:
            if opposite_card == 11 or 12 or 13 or 14:
                if suite_for_this_turn in person_on_turn.suites_on_hand():
                    suites_on_hand = person_on_turn.find_suite(suite_for_this_turn)
                    if suites_on_hand[len(suites_on_hand) - 1].face < max_card.face:
                        return suites_on_hand[0]
                    else:
                        return suites_on_hand[len(suites_on_hand) - 1]
                else:
                    person_on_turn.arrange(get_key2)
                    cards = person_on_turn.cards_on_hand
                    if cards[len(cards) - 1].face < max_card.face:
                        return cards[0]
                    else:
                        return cards[len(cards) - 1]
            else:
                return random_choose(self, len(self.cards_on_hand), suite_for_this_turn)

if __name__ == '__main__':
    AA = person_smart("AA")
    print(AA.name)
    print(AA._cards_on_hand)

# information:
# card on this turn (and biggest)
# king 
# probability of others' main card
