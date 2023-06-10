# game.py
import random
from dinosaur import Dinosaur

def player_action(player_dinosaur,opponet_dinosaur):
    print(f"現在の{player_dinosaur.name}のHP: {player_dinosaur.hp}")
    print(f"現在の{opponet_dinosaur.name}のHP: {opponet_dinosaur.hp}")

        # スキルを使うか通常の攻撃をするかを選択
    command = input("攻撃(1) または スキル(2) を選択してください: ")
    if command == "1":
        player_dinosaur.attack_opponent(opponet_dinosaur)
    elif command == "2":
        while True:
            skill_choice = input("攻撃スキル(1)、ステータスブーストスキル(2)、回復スキル(3) を選択してください: ")
            if skill_choice == "1":
                if player_dinosaur.tp >= 20:
                    player_dinosaur.use_attack_skill(opponet_dinosaur)
                    break
                else:
                    print("TPが足りません。")
                    return player_action(player_dinosaur,opponet_dinosaur)
            elif skill_choice == "2":
                if player_dinosaur.tp >= 10:
                    player_dinosaur.use_boost_skill()
                    break
                else:
                    print("TPが足りません。")
                    return player_action(player_dinosaur,opponet_dinosaur)
            elif skill_choice == "3":
                if player_dinosaur.tp >= 20:
                    player_dinosaur.use_heal_skill()
                    break
                else:
                    print("TPが足りません。")
                    return player_action(player_dinosaur,opponet_dinosaur)
    else:
        print("無効な番号です。")
        return player_action(player_dinosaur,opponet_dinosaur)


def cpu_action(player_dinosaur,cpu_dinosaur):
    #ランダムな行動をさせる
    actions  = ["normal","skill_1"]
    action = random.choice(actions)

    if action == "normal":
        cpu_dinosaur.attack_opponent(player_dinosaur)
    elif action == "skill_1":
        skill_choice = random.choice(["1","2","3"])
        if skill_choice == "1":
            cpu_dinosaur.use_attack_skill(player_dinosaur)
        elif skill_choice == "2":
            cpu_dinosaur.use_boost_skill()
        elif skill_choice == "3":
            cpu_dinosaur.use_heal_skill()
        else:
            #行動が無効な場合やり直し
            print("行動不可")
            return cpu_action(player_dinosaur,cpu_dinosaur)

def main():
    # プレイヤーによる恐竜選択
    selected_dinosaur = None
    while selected_dinosaur is None:
        selected = input("ティラノサウルス(1) または トリケラトプス(2) を選択してください: ")
        if selected == "1":
            selected_dinosaur = Dinosaur("ティラノサウルス", 100, 50, 20, 10)
        elif selected == "2":
            selected_dinosaur = Dinosaur("トリケラトプス", 120, 40, 15, 15)
        else:
            print("もう一度選択してください")

    # CPU恐竜の選択
    cpu_dinosaur = Dinosaur("ティラノサウルス", 100, 50, 20, 10) if selected == "2" else Dinosaur("トリケラトプス", 120, 40, 15, 15)

    # 恐竜の行動
    turn = 1  # ターンの初期化
    while selected_dinosaur.hp > 0 and cpu_dinosaur.hp > 0:
        if turn % 2 == 1:
            print("あなたの攻撃")
            player_action(selected_dinosaur, cpu_dinosaur)
        else:
            print("相手の攻撃")
            cpu_action(selected_dinosaur, cpu_dinosaur)
        turn += 1

    # 結果の表示
    if selected_dinosaur.hp > 0:
        print(f"{selected_dinosaur.name}の勝利！")
    else:
        print(f"{cpu_dinosaur.name}の勝利！")

if __name__ == "__main__":
    main()
