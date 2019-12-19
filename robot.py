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

    # person.cards_on_hand.remove(card_choosed)

    return card_choosed

class Smart(Player):
    def __init__(self, name):
        super().__init__(name)

    def fst_turn_decide(self, num, person_on_turn, king): # 第一個出牌
        # 隨機出一張牌
        if num == 0:
            return random_choose(self,len(self.cards_on_hand))

        # 隨機出一張King花色的牌，無King就隨機出
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
                    chosen_suite = random_choose(self, len(suites[i]), king)
                elif (len(suites[i]) < min_length) and (suites[i][0].suite != king):
                    min_length = len(suites[i])
                    chosen_suite = random_choose(self, len(suites[i]), suites[i][0].suite)
            return chosen_suite

        # 出隊友手中所持有數量最少的花色
        if num == 3:
            my_teammate = self.teammate
            suites = []
            for suite in '♠♥♣♦':
                suites.append(len(my_teammate.find_suite(suite)))
            # print("我隊友是" + my_teammate.name, list(zip('♠♥♣♦',suites))) 
            chosen_suite = list('♠♥♣♦')[suites.index(min(suites))]
            return random_choose(self, len(self.cards_on_hand), chosen_suite)

        # 出隊友手中所持有數量最多的花色
        if num == 4:
            my_teammate = self.teammate
            suites = []
            for suite in '♠♥♣♦':
                suites.append(len(my_teammate.find_suite(suite)))
            # print("我隊友是" + my_teammate.name, list(zip('♠♥♣♦',suites))) 
            chosen_suite = list('♠♥♣♦')[suites.index(max(suites))]
            return random_choose(self, len(self.cards_on_hand), chosen_suite)

        #出手中數字最小的牌
        if num == 5:
            my_card  = self.cards_on_hand
            my_card.sort(key=get_key2)
            return my_card[0]

        #出手中數字最大的牌
        if num == 6:
            my_card  = self.cards_on_hand
            my_card.sort(key=get_key2)
            return my_card[-1]



    def decide(self, num, person_on_turn, person_got_trick, suite_for_this_turn, max_card, teammate_card, opposite_card, king): # 非第一個出牌
        if num == 0:
            return random_choose(self,len(self.cards_on_hand), suite_for_this_turn)

        if num == 1: # 隊友為當前最大就出最小的牌，若是對方為當前最大且自己沒更大的牌，就出最小，否則壓他。
            
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
                
        # 如果我的夥伴出JQKA，我就出相同花色最小的
        if num == 2:
            if teammate_card == 11 or 12 or 13 or 14:
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
                    return random_choose(self, len(self.cards_on_hand), king)
                # else:
                #     person_on_turn.arrange(get_key2)
                #     cards = person_on_turn.cards_on_hand
                #     if cards[len(cards) - 1].face < max_card.face:
                #         return cards[0]
                #     else:
                #         return cards[len(cards) - 1]
            else:
                return random_choose(self, len(self.cards_on_hand), suite_for_this_turn)

        # 某花色缺牌時，出king。
        if num == 4:
            if (suite_for_this_turn not in person_on_turn.suites_on_hand()) and (king in person_on_turn.suites_on_hand()):
                return random_choose(self, len(self.cards_on_hand), king)
            else:
                return random_choose(self, len(self.cards_on_hand), suite_for_this_turn)
