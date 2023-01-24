class SuperHero:
    people = "people"
    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        self.name = name 
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase
    
    def gick (self):
        return f'name: {self.name}'

    def coin (self):
        return f'health_points: {self.health_points * 2}' 

    def kit (self):
        return f"nickname: {self.nickname}, superpower: {self.superpower}, health_points: {self.health_points}, catchphrase: {self.catchphrase}" 

    def len(self):
        return f"lenght: {len(self.catchphrase)}"
hero = SuperHero("islam", "isko", "many", 100,"fuck")

class NewSuper(SuperHero):
    def __init__(self, name, nickname, supername, health_points, catchphrase) -> None:
         super().__init__(name, nickname, supername, health_points, catchphrase)
         self.damage = False
         self.fly = False
    def track(self):
        self.fly = True
        return f"Квадрат: {self.health_points ** 2}, Fly: {self.fly}"
    def full(self):
        return f"newdamage: {self.damage}, newfly: {self.fly}"
    def mango(self):
        return f"catchphrase: {self.catchphrase}"
newsuper = NewSuper("isko", "nitro", "sukw",6,"fly in the True phrase")
print(newsuper.track())
print(newsuper.full())
print(newsuper.mango())
class Villain(SuperHero):
    people = "five"
    def gen_x(self):
        pass
    def crit(self,damage1,damage2):
        return f"uron: {damage1 ** damage2}"
villain = Villain("one", "ssd", "ok",100,"no")
print(villain.crit(6,10)) 