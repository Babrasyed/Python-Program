# <!-- # Assignment: Game Character Management System

# Create a **Game Character Management System** in Python using Object-Oriented Programming (OOP).

# ## Requirements

# 1. Create a class `Character` with the following attributes:

#    * `name`
#    * `level`
#    * `health` (private attribute)

# 2. Use a constructor (`__init__`) to initialize character details.

# 3. Implement the following methods:

#    * `attack()`
#    * `heal()`
#    * `display_info()`

# 4. Use **Encapsulation** by making `health` a private attribute.

# 5. Use **Property Decorators** (`@property` and `@setter`) to safely access and update health.

# 6. Create a child class `Warrior` that inherits from `Character`.

# 7. Override the `attack()` method in `Warrior` (Method Overriding).
# 8. Add a class variable:
#    * `game_name = "Battle Arena"`
# 9. Add a static method:
#    * `game_rules()`
# 10. Create at least **two character objects** and demonstrate all functionalities. -->

class Character:
   def __init__(self,name,level,health):
        self.name=name
        self.level=level
        self.__health=health
   def attack(self):
       print(f"{self.name} attacks with basic strike")
   def heal(self, energy):
       self.__health =  energy + self.__health
       print(f"{self.name} is {energy} points revived")
   def displayInfo(self):
      print(f"Name={self.name},Level={self.level},Health{self.__health}")
   @property
   def health(self):
      return self.__health
   @health.setter
   def health(self,health):
       if health <= 0:
           print(f"{self.name}passed away")
       else:
         self.__health=health
class Warriors(Character):
    game_name = "Battle Arena"
    @staticmethod
    def game_rules():
        print("----------Rules----------")
        print("1 : Defeat Aqib")
        print("2 : Save your life")
    def attack(self):
       print(f"{self.name} attacks with powerful strike")
cha1=Character("Elsa",5,100)
cha2=Warriors("Tom",6,100)
cha1.attack()
cha1.heal(80)
abc=cha1.health
print(abc)
cha1.health= 40
cha1.displayInfo()
print(Warriors.game_name)
cha2.game_rules()
cha2.attack()

print("I don't have a MacBook")





       
   
       



             


