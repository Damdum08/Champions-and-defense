
from colors import Colors
from time import sleep

available_characters = {}

class Character :

    base_price = 2
    base_life = 5     
    base_strength = 1 
    name = "Soldier"

    def __init__(self, player, position):
        """
        PARAM : - player : Player
                - position : tuple
        Set player to player in param.
        Set life, strength and price to base_life, base_strength and base_price.
        Place th character at the position
        If OK : add the current character to the player's team and take the price
        """
        self.player = player
        self.life = self.base_life
        self.strength = self.base_strength
        self.price = self.base_price
        self.position = position

        ok = self.game.place_character(self, position)                              
        if ok :
            self.player.team.append(self)
            self.player.money -= self.price


    @property
    def direction(self):
        return self.player.direction                                            #@property à expliquer

    @property
    def game(self):
        return self.player.game                                                 #@property à expliquer

    @property
    def enemy(self):
        if self.player.direction == +1 :                                        #@property à expliquer
            return self.game.players[1]                                         #Si la direction vaut +1 on retourne le joueur à la place '0' de la liste
        else : 
            return self.game.players[0]                                         #Sinon on retourne le joueur à la place '1' de la liste

    @property
    def design(self):
        if self.player.direction == -1 :
            return (Colors.Green+'<'+Colors.White)
        else : 
            return (Colors.Blue+'>'+Colors.White)

   
    def move(self):
        """
        the character move one step front
        """ 
        new_position = (self.position[0],  self.position[1] + self.direction)
        self.game.place_character(self, new_position)


    def get_hit(self, damages):
        """
        Take the damage to life. If dead, the character is removed from his team and return reward
        PARAM : damages : float
        RETURN : the reward due to hit (half of price if the character is killed, 0 if not)
        """
        self.life -= damages                                             
        if self.life <= 0 :
            self.player.team.remove(self)
            return (self.price // 2)                                           
        else : 
            return 0 


    def attack(self):
        """
        Make an attack :
            - Position initialization after character
            - if in front of ennemy's base : hit the base
            - if in front of character : hit him (and get reward)
        """
        new_position = (self.position[0], self.position[1] + self.direction)
        if new_position[1] == self.game.nb_columns-1 or new_position[1] == 0:
            self.enemy.get_hit(self.strength)
        elif self.game.get_character_at(new_position) and self.game.get_character_at(new_position).direction != self.direction : 
            self.player.money += self.game.get_character_at(new_position).get_hit(self.strength)

    def play_turn(self):
        """
        play one turn : move and attack
        """
        self.move()
        self.attack()
        
            
    def __str__(self):
        """
        return a string represent the current object
        """
        if self. :
            return (f"{self.name} costs {self.base_price} {Colors.Green}${Colors.White} ||| Life : {self.base_life} {Colors.Red}❤ {Colors.White} ||| Strenght : {self.base_strength} ☩")
        else :
            return (f"{self.name} costs {self.base_price} {Colors.Red}${Colors.White} ||| Life : {self.base_life} {Colors.Green}❤ {Colors.White} ||| Strenght : {self.base_strength} ☩")

available_characters["C"] = Character
 
 
 
 
#------------------------------------------------#
#-----------------CLASS FIGHTER------------------#   


class Fighter(Character):
    
    base_price = 3
    base_strenght = 2
    name = "Fighter"
    
    @property
    def design (self): 
        if self.player.direction == -1 :
            return (Colors.Green+"◄"+Colors.White)
        else : 
            return (Colors.Blue+"►"+Colors.White)
    
available_characters["F"] = Fighter



#------------------------------------------------#
#-----------------CLASS TANK---------------------#


class Tank(Character):
    
    base_price = 3
    base_life = 10
    name = "Tank"
    
    def __init__(self, player, position):
        """
        - Initialize bool turn_to_move
        - Parent class called
        """
        self.turn_to_move = False
        super().__init__(player, position)
        
        
    @property
    def design(self):
        if self.player.direction == -1:
            return (Colors.Green+"♖"+Colors.White)
        else :
            return (Colors.Blue+"♜"+Colors.White)
        
    def move(self):
        """
        - if Turn_to_move is True, Parent class called, after set turn_to_move to False 
        - else, set turn_to_move to True
        """
        if self.turn_to_move == True:
            super().move()
            self.turn_to_move = False
        else :
            self.turn_to_move = True
    
available_characters["T"] = Tank



#------------------------------------------------#
#-----------------CLASS WARRIOR------------------#


class Warrior(Character):
    
    base_price = 5
    base_life = 8
    base_strength = 2
    name = "Warrior"

    def __init__(self, player, position):
        """
        - Initialize counter
        - Parent class called
        """
        self.counter_hit_warrior = 0
        super().__init__(player, position)

    @property 
    def design(self):
        if self.player.direction == -1:
            return (Colors.Green+"W"+Colors.White)
        else :
            return (Colors.Blue+"W"+Colors.White)

    def get_hit(self, damages):
        """
        - Each round, +1 to counter
        - Parent class called
        """
        self.counter_hit_warrior += 1
        return super().get_hit(damages)


    def attack(self):
        """
            Make an attack :
            - Position initialization after character
            - if in front of ennemy's base : hit the base
            - if in front of character : hit him (and get reward)
            - if warrior hits 3 times, self strenght *2
        """
        new_position = self.position[0], self.position[1] + self.direction
        if new_position[1] == self.game.nb_columns-1 or new_position[1] == 0:
            self.enemy.get_hit(self.strength)
        elif self.game.get_character_at(new_position) and self.game.get_character_at(new_position).direction != self.direction :   
            if self.counter_hit_warrior >= 3 :
                self.player.money += self.game.get_character_at(new_position).get_hit(self.base_strength*2)
            else :
                self.player.money += self.game.get_character_at(new_position).get_hit(self.strength)


available_characters["W"]= Warrior



#------------------------------------------------#
#-----------------CLASS HEAL---------------------#


class Heal(Character):
    
    base_price = 5
    base_life = 3
    base_strenght = 1
    base_heal = 1
    name = "Heal"
    
    def __init__(self, player, position):
        """
        - Initialize counter to heal his team
        - Parent class call
        """
        self.counter_heal = 0
        super().__init__(player, position)
        
    
    @property 
    def design(self):
        if self.player.direction == -1:
            return (Colors.Green+"H"+Colors.White)
        else :
            return (Colors.Blue+"H"+Colors.White)
    
    
    def heal_team(self):
        """
        - if life champion < life base --> ok heal
        - print life of all team character
        """
        for champion in self.player.team:
            if champion.life < champion.base_life:  
                if self.counter_heal % 4 == 0: 
                    champion.life += Heal.base_heal
                    if champion.direction == +1 : 
                        print(f"\n{Colors.Blue}{champion.name}{Colors.White} line {champion.position[0]} have {champion.life} {Colors.Red}❤{Colors.White}")
                    else :
                        print(f"\n{Colors.Green}{champion.name}{Colors.White} line {champion.position[0]} have {champion.life} {Colors.Red}❤{Colors.White}")

    def play_turn(self):
        """
        - Each round, +1 to counter
        - Heal_team function call
        - Parent class call
        """
        self.counter_heal += 1
        self.heal_team()
        return super().play_turn()
   
available_characters["H"]= Heal


#-----------------------------------------------------#
#-----------------CLASS SUICIDE BOMBER----------------#


class SuicideBomber(Character):
    
    base_price = 8
    base_life = 1
    base_strength = 10
    speed = 2
    name = "Suicide bomber"


    def __init__(self, player, position):
        """
        - Parent class call
        """
        super().__init__(player, position)

    @property 
    def design(self):
        if self.player.direction == -1:
            return (Colors.Green+"K"+Colors.White)
        else :
            return (Colors.Blue+"K"+Colors.White)


    def move(self):
        """
        the character move two step front
        """ 
        shift = 0    
        while shift < self.speed :
            shift += 1 
            super().move()


    def attack(self):
        """
        Make an attack :
            - Position initialization after character
            - if in front of ennemy's base : hit the base
            - if in front of character : hit him (and get reward)
        """
        
        new_position = (self.position[0], self.position[1] + self.direction)
        if new_position[1] == self.game.nb_columns-1 or new_position[1] == 0:
            self.enemy.get_hit(self.strength)
            self.player.team.remove(self)
            self.animation()
            sleep(3)
        elif self.game.get_character_at(new_position) and self.game.get_character_at(new_position).direction != self.direction : 
            self.player.money += self.game.get_character_at(new_position).get_hit(self.strength)
            self.animation()
            sleep(3)


    def animation(self):
        print("""
                _.-^^---....,,_
             _--                --_
            <                      >)
            |        Kᴀʙᴏᴜᴍ         |
            \._      -10HP        _./
                ```--. . , ; .--'''
                     | |   |
                  .-=||  | |=-.
                  `-=#$%&%$#=-'
                     | ;  :|
            _____.,-#%&$@%#&#~,._____
            """)

available_characters["K"]= SuicideBomber