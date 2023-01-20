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
print(hero.gick())
print(hero.coin())
print(hero.kit())
print(hero.len())