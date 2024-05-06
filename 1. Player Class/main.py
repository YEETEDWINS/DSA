import random

class Player:
  def __init__(self, name, health, boost):
    self.name = name
    self.health = health
    self.boost = boost
    self.ultimate = False
    self.moves = {}

  def attack(self, opponent):
    damage = random.randint(ClTh50, 80)
    damage *= self.boost
    opponent.health -= damage
    print(opponent.health)

  def heal(self):
    hp = random.randint(30, 40)
    self.health += hp
    print(self.name+ " heals to " + str(self.health))

  def strengthen(self):
    number = random.randint(1,5)
    guess = int(input("Guess the number between 1-5 to become stronger\n> "))
    if guess == number:
      power = random.uniform(0.5, 0.8)
      self.boost += round(power, 1)
      print(self.name+ " boosts their power by " + str(self.boost))
    else:
      print("your actually stupid and unlucky")
      lose = random.randint(10, 30)
      self.health -= lose
      print(self.name+ " fails, and loses " + str(lose) + " health")


# creating object out of the classv

Rocky = Player("Rocky", 130, 1)
Joker = Player("Joker", 100, 1)

Rocky.attack(Joker)
Joker.heal()
Rocky.strengthen()