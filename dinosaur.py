import random

class Dinosaur:
    def __init__(self,name,hp,tp,attack,defence):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.tp = tp
        self.max_tp = tp
        self.attack = attack
        self.defence = defence

    def attack_opponent(self,opponent):
        base_damage = self.attack - opponent.defence #攻撃者の攻撃力−攻撃される側の守備力
        damage_range = int(base_damage * 0.1)          #ダメージの変化量を決めている
        damage = random.randint(base_damage - 1, base_damage + 1) #実際のダメージ範囲が決まる
        if damage>1:
            opponent.hp -= damage
        else:
            damage = int(1)
            opponent.hp -= damage
        # 攻撃メッセージ
        if self.name == "ティラノサウルス":
            print(f"{self.name}の嚙みつく攻撃！{opponent.name}に{damage}ダメージ与えた！")
        else:
            print(f"{self.name}のフリルで守りながらの攻撃！{opponent.name}に{damage}ダメージ与えた！")

    #アタックスキル
    def use_attack_skill(self, opponent):
        if self.tp >= 20:
            self.tp -= 20 #tpの消費
            skill_damage = self.attack * 2 - opponent.defence
            damage_range = int(skill_damage * 0.1)
            damage = random.randint(skill_damage - damage_range,skill_damage + damage_range)
            if opponent.hp >= 20:
                opponent.hp -= damage
                print(f"{self.name}は攻撃スキル「猛進」を使って{opponent.name}に{damage}与えた！")
                print(f"{self.name}の残りtpは{self.tp}")
            else:
                print("TPが足りません")

    def use_boost_skill(self):
        if self.tp >= 10:
            self.tp -= 10
            self.attack += 5
            self.defence += 5

            print(f"{self.name}はブーストスキルを使い攻撃力を{self.attack}にアップし、防御力が{self.defence}にアップした！")
            print(f"{self.name}の残りtpは{self.tp}")
        else:
            print("TPが足りません")

    def use_heal_skill(self):
        if self.tp >= 20:
            self.tp -= 20
            heal_base = self.max_hp * 1.5
            heal_range = heal_base * 0.1
            heal_amount = random.randint(heal_base - heal_range,heal_base + heal_range)
            self.hp += heal_amount
            print(f"{self.name}は古代のしずくを呼びHPを{heal_amount}回復させた！")
            print(f"{self.name}のHPは{self.hp}になったよ！")
        elif self.hp == self.max_hp:
            print("HPは満タンです")
        else:
            print("TPが足りません")