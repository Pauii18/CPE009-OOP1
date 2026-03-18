from Character import Character

class Novice(Character):
    def basicAttack(self, character):
        character.reduceHp(self.getDamage())
        print(f"{self.getUsername()} performed Basic Atack! -{self.getDamage()}")

character1 = Novice("Leo")
print(character1.getUsername()) 
print(character1.getHp()) 
