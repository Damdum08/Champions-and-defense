
from colors import Colors
from time import sleep
import os, platform


class Game :


    def __init__(self, player0, player1, nb_lines=6,nb_columns=15):
        """
        PARAM : - player0 : Player
                - player1 : Player
                - nb_lines : float
                - nb_columns : float
        - update players' direction and game
        - initialisate player_turn to 0
        """                                                           
        self.nb_lines = nb_lines
        self.nb_columns = nb_columns
        self.players = [player0, player1]
        self.player_turn = 0

        player0.direction = +1
        player0.game = self
        player1.direction = -1
        player1.game = self


    @property
    def current_player(self):
        """
        Returns the player according to the turn
        """
        return self.players[self.player_turn]

    @property
    def oponent(self):
        """
        Returns rival based on turn
        """
        return self.players[self.player_turn^1]

    @property
    def all_characters(self):
        """
        Returns the characters present on the map of each player
        """
        return self.players[0].team + self.players[1].team
        

    def get_character_at(self, position):
        """
        PARAM : - position : tuple
        RETURN : character at the position, None if there is nobody
        """
        for character in self.all_characters :
            if character.position == position :
                return character
    

    def place_character(self, character, position):
        """
        place character to the position if possible
        PARAM : - character : Character
                - position : tuple
        RETURN : bool if placing is done or not
        """
        line, column = position
        if character.direction == +1 :
            if (self.get_character_at(position) == None) and (0 <= column < self.nb_columns-1) and (0 <= line <= self.nb_lines):
                character.position = position
                return True
        elif character.direction == -1 :
            if (self.get_character_at(position) == None) and (1 <= column < self.nb_columns) and (0 <= line <= self.nb_lines):
                character.position = position
                return True
        else :
            return False
        

    def draw(self):
        """
        print the board
        print player's info
        """
        self.clear_screen()
        print(Colors.Blue+f"\n{self.players[0].name:<4}{'  '*self.nb_columns}{Colors.Green}{self.players[1].name:>4}")
        print(Colors.Blue+f"{self.players[0].life:<4}{'  '*self.nb_columns}{Colors.Green}{self.players[1].life:>4}")  
        print(Colors.White+"----"+self.nb_columns*"--"+"----")

        for line in range(self.nb_lines):
            print(f"|{line:>2}|", end="")
            for col in range(self.nb_columns) :

                if self.get_character_at((line, col)) :                            
                    print(self.get_character_at((line, col)).design, end = ' ')
                else :      
                    print(".", end=" ")
                    
            print(f"|{line:<2}|")
        print(Colors.White+"----"+self.nb_columns*"--"+"----")
        print(Colors.Blue+f"{self.players[0].money:<3}${'  '*self.nb_columns}{Colors.Green}${self.players[1].money:>3}{Colors.White}")
        

    def play_turn(self):
        """
        play one turn :
            - current player can add a new character
            - current player's character play turn
            - oponent player's character play turn
            - draw the board
        """
        self.current_player.new_character()

        for character in self.current_player.team :
            character.play_turn()

        for character in self.oponent.team :            
            character.play_turn()

        self.draw()


    def play(self):
        """
        Play an entire game : while current player is alive, play a turn and change player turn
        Check which player wins and display it        
        """
        while self.current_player.is_alive and self.oponent.is_alive:

            self.play_turn()

            if self.player_turn == 0:
                self.player_turn += 1
            else :
                self.player_turn -= 1
        if self.current_player.is_alive and self.oponent.is_alive == False :
            print(f"\nThe winner is {self.current_player.name}")
        elif self.current_player.is_alive == False and self.oponent.is_alive :
            print(f"\nThe winner is {self.oponent.name}")
        print("\nWAIT ...")
        sleep(4)
        
    def clear_screen(self):
        if platform.system() == "Windows":
            os.system("cls")
        else:
            os.system("clear")