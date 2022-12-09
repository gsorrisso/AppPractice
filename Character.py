class Character:
    NOT_ENOUGH_POWER_POINTS = "not_enough_power_points" # CONST constant 
    # constructor 
    #  a method is just a function inside a class 
    def __init__(self, type, name, inventory =[], power_points = 10, can_teleport = False, position=Point(), token='?'):
        self.type = type
        self.name = name
        self.inventory = inventory
        self.power_points = power_points
        self.can_teleport = can_teleport

    def run(self):
        if self.power_points >= 2:
            print(f"{self.name} is running.")
            self.power_points -= 2
            return True
        else:
            print( f"{self.name} only has {self.power_points} Power Points and cannot run.")
            return Character.NOT_ENOUGH_POWER_POINTS

    def rest(self):
        if self.power_points < 10:
            print( f'{self.name} is resting.')
            self.power_points += 1
            return True #not required but is useful 

        else:
            print( f'{self.name} has {self.power_points} Power Points and does not need to rest.')
            return False #not required but is useful

    def teleport(self):
        if self.power_points >= 4 and self.can_teleport:
            print( f'{self.name} is teleporting.')
            self.power_points -= 4
            return True

        elif self.power_points < 4:
            print( f'{self.name} only has {self.power_points} Power Points and cannot teleport.')
            return Character.NOT_ENOUGH_POWER_POINTS

        else:
            print( f'{self.name} is not able to teleport.')
            return False

    def inventory(self): 
        for item in self.inventory:
            print ( item )

        else:
            print ( "Invalid action")