import random 

class Person():
    def __init__(self, name: str, hp: int, mana: int, exp: int, skin: str):
        self.name = name
        self.hp = hp
        self.mana = mana
        self.exp = exp
        self.skin = skin
        self.lvl = exp // 100


class Arms():
    def __init__(self, name: str, demage: int, exploid_mana: int, 
        lvl: int, type_class: str, skin: str):

        self.name = name
        self.demage = demage
        self.exploid_mana = exploid_mana
        self.lvl = lvl
        self.type_class = type_class

    def __str__(self):
        return f"{self.name} {self.demage} {self.exploid_mana} {self.lvl} {self.type_class}"


class ArmsType():
    def __init__(self):
        self.sword = "sword"
        self.bow = "bow"
    
    def sword_class(self):
        return self.sword

    def bow_class(self):
        return self.bow


class Mobs(Person):
    def __init__(self, name: str, hp: int, mana: int, exp: int, skin: str):
        super().__init__(name, hp, mana, exp, skin)
        pass
    


def main():
    hero1 = Person("Alex", 100, 100, 100, r"...")
    print(hero1, hero1.lvl)

    arm1 = Arms("Excalibur", 50, 30, 10, ArmsType().sword_class, r"...")
    print(arm1)

    mob1 = Mobs("Goblin", 5, 0, 0, r"...")
    print(mob1)


if __name__ == "__main__":
    main()