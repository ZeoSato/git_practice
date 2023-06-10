import random

class Dinosaur:
    def __init__(self, name, hp, tp, attack, defense):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.tp = tp
        self.max_tp = tp
        self.attack = attack
        self.defense = defense

    def attack_opponent(self, opponent):
        base_damage = self.attack - opponent.defense
        damage_range = int(base_damage * 0.1)
        damage = random.randint(base_damage - damage_range, base_damage + damage_range)

        if damage > 0:
            opponent.hp -= damage
        else:
            damage = 0

        if self.name == "ティラノサウルス":
            print(f"{self.name}の噛みつく攻撃！{opponent.name}に{damage}のダメージ！")
        else:
            print(f"{self.name}のフリルで守りながら角で攻撃！{opponent.name}に{damage}のダメージ！")

    def use_attack_skill(self, opponent):
        if self.tp >= 20:
            self.tp -= 20
            skill_damage = self.attack * 2 - opponent.defense
            damage_range = int(skill_damage * 0.1)
            damage = random.randint(skill_damage - damage_range, skill_damage + damage_range)

            if damage > 0:
                opponent.hp -= damage
            else:
                damage = 0

            print(f"{self.name}は攻撃スキル「猛突撃」を使って{opponent.name}に{damage}のダメージを与えた！")
        else:
            print("TPが足りません！")

    def use_stat_boost_skill(self):
        if self.tp >= 30:
            self.tp -= 30
            self.attack += 5
            self.defense += 5

            print(f"{self.name}はステータスブーストスキル「パワーアップ」を使って攻撃力と防御力を上昇させました！")
        else:
            print("TPが足りません！")

    def use_heal_skill(self):
        if self.tp >= 40:
            self.tp -= 40
            heal_amount = int(self.max_hp * 0.3)
            self.hp += heal_amount
            if self.hp > self.max_hp:
                self.hp = self.max_hp

            print(f"{self.name}は回復スキル「ヒーリングウェイブ」を使って{heal_amount}のHPを回復しました！")
        else:
            print("TPが足りません！")

# プレイヤーの恐竜選択
selected_dinosaur = None
while selected_dinosaur is None:
    selected = input("ティラノサウルス(1) または トリケラトプス(2) を選択してください: ")
    if selected == "1":
        selected_dinosaur = Dinosaur("ティラノサウルス", 100, 50, 20, 10)
    elif selected == "2":
        selected_dinosaur = Dinosaur("トリケラトプス", 120, 40, 15, 15)
    else:
        print("無効な選択です。もう一度選択してください。")

# CPUの恐竜作成
cpu_dinosaur = Dinosaur("ティラノサウルス", 100, 50, 20, 10) if selected == "2" else Dinosaur("トリケラトプス", 120, 40, 15, 15)

# 恐竜の行動
turn = 1  # 行動ターンの初期値
while selected_dinosaur.hp > 0 and cpu_dinosaur.hp > 0:
    if turn % 2 == 1:
        attacking_dinosaur = selected_dinosaur
        defending_dinosaur = cpu_dinosaur
    else:
        attacking_dinosaur = cpu_dinosaur
        defending_dinosaur = selected_dinosaur
    
    print(f"現在の{attacking_dinosaur.name}のHP: {attacking_dinosaur.hp}")
    print(f"現在の{defending_dinosaur.name}のHP: {defending_dinosaur.hp}")
    
    command = input("攻撃(1) または スキル(2) を選択してください: ")
    if command == "1":
        attacking_dinosaur.attack_opponent(defending_dinosaur)
    elif command == "2":
        skill_choice = input("攻撃スキル(1)、ステータスブーストスキル(2)、回復スキル(3) を選択してください: ")
        if skill_choice == "1":
            attacking_dinosaur.use_attack_skill(defending_dinosaur)
        elif skill_choice == "2":
            attacking_dinosaur.use_stat_boost_skill()
        elif skill_choice == "3":
            attacking_dinosaur.use_heal_skill()
        else:
            print("無効な選択です。もう一度選択してください。")
            continue
    else:
        print("無効な選択です。もう一度選択してください。")
        continue
    
    turn += 1

# 結果の表示
if selected_dinosaur.hp > 0:
    print(f"{selected_dinosaur.name}の勝利！")
else:
    print(f"{cpu_dinosaur.name}の勝利！")

print(f"君は{selected_dinosaur.name}と{cpu_dinosaur.name}どっちが好き？")