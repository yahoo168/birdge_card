import random
import math
from card import *
from robot import *
import sys
import time
from threading import Thread, Lock

#  無聊的小動畫彩蛋


def animated_loading(option):
    if option == 1:
        print('原住民小石 ： 喔啊發薩撒刁得！！ 小馮我愛你！！！ ')
        time.sleep(2.5)
        print('醫學系小馮 ：我也是！！ ♥你 喜歡跟你做♥心！')
        print('關燈後...')
        time.sleep(2.5)
        for _ in range(10):
            print('醫學系小馮：' + 'A' * 15 + '!!!', sep=' ')
            time.sleep(0.5)

    if option == 2:
        print('\n-1 跟 1 都搞錯，你他媽喜憨兒嗎？\n')
        time.sleep(1)
        print('\n就是有你們這種人，程式才要防錯變得很長，懲罰一下:')
        print('滾回去重選')
        chars = "/—\\|"*10
        for char in chars:
            sys.stdout.write('\r'+'loading...'+char)
            time.sleep(.1)
            sys.stdout.flush()


def call_choose(person, valid_suite, valid_num):
    person.arrange(get_key)
    print('\n你的手牌', person.cards_on_hand)
    number = input("請輸入數值 1,2,...,7: ")
    if number == "pass":
        person.call_status = int(1)
        suite, number = valid_suite, valid_num
        print(person.name, "pass")
    else:
        suite = input("請輸入花色 ♠(0) ♥(1) ♦(2) ♣(3): \n")
        if suite not in "0123" or (number not in "1234567"):
            print("您的輸入不合規則!")
            return call_choose(person, valid_suite, valid_num)
        if int(number) == int(valid_num) and (int(suite) >= valid_suite):
            print("您的輸入不合規則!")
            return call_choose(person, valid_suite, valid_num)
        if int(number) < int(valid_num):
            print("您的輸入不合規則!")
            return call_choose(person, valid_suite, valid_num)
        result = ["♠","♥","♦","♣"][int(suite)]+str(number)
    return suite, number, result

def random_call(person, suite, number):
    prob = (random.randint(0, 100) % 2)
    if int(suite) == int(4):
        sui = int(suite) - 1
        num = number
        result = ["♠","♥","♦","♣"][int(sui)]+str(num)
    else:
        if prob == 0:
            sui, num = suite, number
            person.call_status = int(1)
            result = "pass"
        if prob == 1:
            if int(suite) > 0:
                sui = int(suite) - 1
                num = number
                result = ["♠","♥","♦","♣"][int(sui)]+str(num)
            else:
                if int(number) == 7:
                    person.call_status = int(1)
                    sui, num = suite, number
                    result = "pass"
                else:
                    sui = 3
                    num = int(number) + 1
                    result = ["♠","♥","♦","♣"][int(sui)]+str(num)
    return sui, num, result

# 出牌的人 自己選要出什麼
def choose(person, suite_for_this_turn="♠♥♦♣"):
    person.arrange(get_key)
    print('\n你的手牌', person.cards_on_hand)
    suite = input("請輸入花色 ♠(0) ♥(1) ♦(2) ♣(3): ")
    face = input("請輸入數值 A,2,...J,Q,K: \n")

    # 輸入型態錯誤
    if suite not in "0123" or (face not in map(str, range(2, 11)) and face not in "AJQK"):
        print("您的輸入不合規則! 注意：A 和 JQK 請直接輸入文字，而非數字!")
        return choose(person, suite_for_this_turn)

    # 出的花色不符合本回合花色
    suite = ["♠", "♥", "♦", "♣"][int(suite)]

    if suite_for_this_turn in person.suites_on_hand() and suite not in suite_for_this_turn:
        print("\n您的花色不符合規則，花色要出{0}，除非您已無該花色的牌".format(suite_for_this_turn))
        print("但你還有{0}張{1}牌，你又不是韓國瑜，非要作弊不可嗎？\n"
              .format(len(person.find_suite(suite_for_this_turn)), suite_for_this_turn))

        return choose(person, suite_for_this_turn)

    key = '%s%s' % (suite, face)

    # 出的牌不在手中
    for card in person.cards_on_hand:
        if card.__repr__() == key:
            person.cards_on_hand.remove(card)
            return card

    print("你選的牌不在你手中！台北的未來在丁守中！ 他要重選，你也一樣")
    return choose(person, suite_for_this_turn)

# 隨機出牌 待改 花色限制問題


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

    person.cards_on_hand.remove(card_choosed)

    return card_choosed

# 展示手牌


def show_cards(close_show=1):
    if close_show != -1:
        print("展示手牌" + "-"*15)
        for player in players:
            print(player.name + ':', end=' ')
            player.arrange(get_key)
            print(player.cards_on_hand)
        print("-"*20)
    return 0

def call(position, players, model, nickname = "國家機器"):
    pass_count = int(0)
    suite_on_call = int(4)
    num_on_call = int(1)
    while pass_count < 3:
        person_on_turn = players[position]
        if person_on_turn.call_status == 1:
            position += 1
            if position == 4:
                position = 0
            continue
        if model == 0:
            if person_on_turn.name == nickname:
                suite_on_call, num_on_call, k = call_choose(person_on_turn, suite_on_call, num_on_call)
                if close_show != -1:
                    print(person_on_turn.name, k)
            else:
                suite_on_call, num_on_call, k = random_call(person_on_turn, suite_on_call, num_on_call)
                if close_show != -1:
                    print(person_on_turn.name, k)
        if model == 1:
            suite_on_call, num_on_call, k = random_call(person_on_turn, suite_on_call, num_on_call)
            if close_show != -1:
                print(person_on_turn.name, k)
        if person_on_turn.call_status == 1:
            pass_count += 1
        position += 1
        if position == 4:
            position = 0
    for i in range(4):
        if players[i].call_status == int(0):
            person_got_call = players[i]
    king = ["♠","♥","♦","♣"][int(suite_on_call)]
    return king, num_on_call, person_got_call

# 每回合玩牌過程

def play(position, players, king, model, close_show, nickname="國家機器"):  # 玩家的名字 待改
    person_on_turn = players[position]

    # 如果不是真人玩家，展示所有電腦的手牌
    if model != 0:
        show_cards(close_show)

    # 第一個玩家出的牌
    if model == 0:  # 玩家和三名電腦對戰
        if person_on_turn.name == nickname:
            fst_card = choose(person_on_turn)
        else:
            fst_card = random_choose(person_on_turn,
                                     len(person_on_turn.cards_on_hand))

            # 待改 fst_card = person_on_turn.fst_turn_decide()
    elif model == 1:  # 電腦自動對戰
        fst_card = random_choose(person_on_turn,
                                 len(person_on_turn.cards_on_hand))
    if close_show != -1:
        print(person_on_turn, fst_card)

    suite_for_this_turn = fst_card.suite  # 本回合適用的花色
    # max_face = fst_card.face
    # end of 第一個玩家出的牌

    person_got_trick = person_on_turn  # 目前牌面最大的人
    max_card = fst_card  # 這回合最終獲勝的牌，預設為第一張牌

    position += 1  # 出完牌後，換下一個人出
    if position == 4:  # 配合座位列表值，滿四就歸零
        position = 0

    # 第一張牌丟出後的牌局
    for _ in range(3):
        person_on_turn = players[position]

        if model == 0:
            if person_on_turn.name == nickname:
                card_on_turn = choose(person_on_turn, fst_card.suite)
                time.sleep(0.3)  # 稍微緩速，增強真實感

            else:
                card_on_turn = random_choose(
                    person_on_turn, len(person_on_turn.cards_on_hand), suite_for_this_turn)
                time.sleep(0.3)  # 稍微緩速，增強真實感



        if model == 1:
            # card_on_turn = random_choose(
            #     person_on_turn, len(person_on_turn.cards_on_hand), suite_for_this_turn)
            card_on_turn = person_on_turn.decide(1, person_on_turn, person_got_trick, suite_for_this_turn, max_card)

        if model == 2:
            pass

        face_on_turn = card_on_turn.face
        if close_show != -1:
            print(person_on_turn, card_on_turn)

        # 若花色相同，單純比大小 (註：此處是以字元的 Ascii 碼比對)
        if suite_for_this_turn == card_on_turn.suite:
            if face_on_turn > max_card.face:
                max_card = card_on_turn
                person_got_trick = person_on_turn

        # 挑戰者出king，而守位者非king
        elif suite_for_this_turn != card_on_turn.suite:
            if card_on_turn.suite == king:
                suite_for_this_turn = card_on_turn.suite
                max_card = card_on_turn
                person_got_trick = person_on_turn

        position += 1
        if position == 4:
            position = 0
    # end of 第一張牌丟出後的牌局

    return(person_got_trick, max_card)


def bridge_game(model, close_show):  # 牌局開始
    p = Poker()  # 建立牌組
    p.shuffle()  # 洗牌
    global count_A_win
    # 發牌
    for _ in range(13):
        for player in players:
            player.get(p.next)
    # random.shuffle(players)  # 玩家座位重排
    team_A = (players[0], players[2])  # A隊伍
    team_B = (players[1], players[3])  # B隊伍

    for i in range(4):
        players[i].teammate = players[(i+2) % 4]

    if close_show != -1:
        print('\n隊伍分組:\nA隊伍:{}\nB隊伍{}\n'.format(team_A, team_B))
        time.sleep(0.5)
        print("-"*12)
        print("叫牌階段")

    position = (random.randint(0, 100) % 4)  # 隨機從某人開始叫牌
    # position = 0
    # king = Function 叫牌
    # trick = 叫牌()
    king, target_num, person_got = call(position, players, model)
    
    if close_show != -1:
        print("叫牌結果是", king ,target_num, ",由%s拿下" % person_got.name)
        print('-'*12)
    
    position = players.index(person_got) + 1
    if position == 4:
        position = 0

    target_num = int(target_num) - 1
    if person_got in team_A:
        target_num *= -1

    # 待改 叫牌引入
    target_for_B = 7 + target_num
    target_for_A = 14 - target_for_B
    trick_team_A = 0
    trick_team_B = 0
    if close_show != -1:
        print("A隊需要%s墩才能獲勝,B隊需要%s墩才能獲勝" % (target_for_A, target_for_B))

    while trick_team_A != target_for_A and trick_team_B != target_for_B:

        # 各回合開始
        person_got_trick, max_card = play(
            position, players, king, model, close_show)

        # 由贏的人優先出牌
        position = players.index(person_got_trick)

        if person_got_trick in team_A:
            team = "A"  # 用於下面打印
            trick_team_A += 1
        else:
            team = "B"  # 用於下面打印
            trick_team_B += 1

        if close_show != -1:
            print("本回合由{0}隊的{1}拿下，他的牌為{2}"
                  .format(team, person_got_trick, max_card))

            print("A隊墩數為{0}，B隊墩數為{1}"
                  .format(trick_team_A, trick_team_B))
            print("-"*20)
            print()

    if trick_team_A == target_for_A:
        shared_resource_lock.acquire()
        count_A_win += 1
        shared_resource_lock.release()
    return True
def control_model():
    num = 1  # 牌局執行次數，預設為1，可由model選擇修改
    close_show = 1  # 是否開啟顯示過程，預設為開啟，可由model選擇修改
    model = input("請輸入本局型態:\n\t扮演國家機器，和助手一起消滅台灣敗類，請輸入 0:\n\
\t電腦自動對戰，請輸入 1: \n\
\t測試橋牌策略，請輸入 2: \n\
\t想告白，請輸入 520:\n")

    if model == "520":
        animated_loading(1)  # 顯示小動畫
        return control_model()

    if model not in map(str, range(0, 3)):
        print('\n看清楚指示，瞎了去看眼科 o__o，重選啦幹\n')
        return control_model()

    if model == "1":
        # print('因為我懶的防錯了，所以這邊不打數字會爆掉，不用試了')
        try:
            num = int(input('您希望跑幾次呢？請輸入阿拉伯數字:'))
        except:
            print('\n叫你打阿拉伯數字，你打啥小？\n')
            return control_model()

        if num >= 10:
            try:
                close_show = int(input('\n您輸入的模擬遊戲次數偏多，若要關閉顯示過程請輸入-1\n\
                    否則會跑很慢，若仍要開啟請輸入1：'))
            except:
                animated_loading(2)  # 顯示小動畫
                return control_model()

    if model == "2":
        print("施工中...\n")
        return control_model()

    else:
        return (int(model), num, close_show)


# 替共享變數（A隊勝率）上鎖
shared_resource_lock = Lock()
# A隊勝率
count_A_win = 0

if __name__ == "__main__":
    # 設定玩家
    players = [Smart('國家機器'), Smart('韓國瑜'), Smart('國家機器的助手'), Smart('李佳芬')]
    model, num, close_show = control_model()  # 此局的遊戲型態
    num_completed = 0
    try:
        start_time = time.time()
        for i in range(num):
            t = bridge_game(model, close_show)
            percent = ((i+1) / num) * 100
            print("目前完成{}次\t進度 | {:>5.3f}%".format(i+1, percent))
            num_completed +=1
            for j in range(4):
                players[j].call_status = int(0)
    finally:    
        end_time = time.time()
        win_ratio = count_A_win / (num_completed)
        print('總共執行了{}次，A隊勝利{}次，勝率為{:.5f}'.format(num_completed, count_A_win, win_ratio))
        print('共耗費{:.3f}秒'.format(end_time - start_time))