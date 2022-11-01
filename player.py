
from character import available_characters
from colors import Colors
from save import save_quit
import random

class Player :

    def __init__(self, name, life, money):
        """
        PARAM : - name : str
                - life : float
                - money : float
        initialisate team to empty list, game and direction to None
        """                                                                       
        self.name = name
        self.life = life
        self.money = money
        self.team = []
        self.game = None
        self.direction = None


    @property
    def is_alive(self):
        """
        - Return his life if over 0
        """
        return self.life > 0


    def get_hit(self, damages):
        """
        Take the damage to life
        PARAM : - damages : float
        """
        self.life -= damages


    def new_character(self):
        """
        Ask the player wich character wants
        Ask the player where to add a new Character,       
        and create the new one
        
        """
        print(Colors.White+("Iғ ʏᴏᴜ ᴡᴀɴᴛ, ɪɴꜱᴇʀᴛ Q ᴏʀ ᴇxɪᴛ ᴀᴛ ᴀɴʏ ᴛɪᴍᴇ ᴛᴏ ᴇxɪᴛ ᴀɴᴅ ꜱᴀᴠᴇ"))
        
        print(("""
                All characters availble : 
               """))
        for letter, values in list(available_characters.items()):
            print(f"Insert {letter} for choose {values.__str__(values)}")
        
           
        choose_character = " "
        while not choose_character in list(available_characters.keys()) and choose_character != "" :
            if self.direction == +1:
                choose_character = input(Colors.Blue+f"{self.name}{Colors.White} : Choose your character : (Enter if none) ").upper()
            else :
                choose_character = input(Colors.Green+f"{self.name}{Colors.White} : Choose your character : (Enter if none) ").upper()
            
            if choose_character.lower() in ("q","exit"):
                save_quit(self.game)
                    
        line = "-1"
        while not line in ("0","1","2","3","4","5") and line != "":
        
            if self.direction == +1 :                    
                line = input(Colors.Blue+f"{self.name}{Colors.White} : Wich line would you place the new one (0-{self.game.nb_lines-1}) ? (enter if none) ")
            else : 
                line = input(Colors.Green+f"{self.name}{Colors.White} : Wich line would you place the new one (0-{self.game.nb_lines-1}) ? (enter if none) ")
               
            if line.lower() in ("q","exit"):
                save_quit(self.game)
            
        if choose_character != "":
            if line != "":
                line = int(line)
                if 0<=line<=self.game.nb_lines-1 :
                    if self.money >= available_characters[choose_character].base_price :
                        column = 0 if self.direction == +1 else self.game.nb_columns-1
                        available_characters[choose_character](self,(line, column))
                    else : 
                        print("\nNot enough money")
                        
class AI(Player):
    
    def __init__(self, name, life, money):
        super().__init__(name, life, money)
        
    def new_character(self):
        """
        Create new random line
        Make a random choice for a character
        Check if AI has enough money
        """
        line_random = random.randint(0, self.game.nb_lines)
        character_ia_choice = random.choice(list(available_characters))
        if available_characters[character_ia_choice].base_price <= self.money :
            available_characters[character_ia_choice](self,(line_random, self.game.nb_columns-1))