
from colors import Colors
from game import Game
from player import *
from time import sleep
from save import backup_game
import os, platform
import pickle

def clear_screen():
    """
    method execute the command 
    a string = clear 
    in a subshell
    """
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")


if __name__ == "__main__":

    print("""
   ___  _                                                                             _      .___          ,__
 .'   \ /        ___  , _ , _   \,___, `   __.  , __     ____        ___  , __     ___/      /   `    ___  /  `   ___  , __     ____   ___
 |      |,---.  /   ` |' `|' `. |    \ | .'   \ |'  `.  (           /   ` |'  `.  /   |      |    | .'   ` |__  .'   ` |'  `.  (     .'   `
 |      |'   ` |    | |   |   | |    | | |    | |    |  `--.       |    | |    | ,'   |      |    | |----' |    |----' |    |  `--.  |----'
  `.__, /    | `.__/| /   '   / |`---' /  `._.' /    | \___.'      `.__/| /    | `___,'      /---/  `.___, |    `.___, /    | \___.' `.___,
                                \                                                     `                    /
        """)
    input("ᴘʀᴇꜱꜱ ᴇɴᴛᴇʀ ᴛᴏ ᴄᴏɴᴛɪɴᴜᴇ . . . ")
    
    while 1 :
        clear_screen()
        print((Colors.White)+"""
            Tᴏᴡᴇʀ, Cʜᴀᴍᴘɪᴏɴꜱ ᴀɴᴅ Dᴇғᴇɴꜱᴇ\n
                1 : Rᴜɴ Gᴀᴍᴇ
                2 : Pʟᴀʏ ᴡɪᴛʜ IA
                3 : Rᴇᴄᴏᴠᴇʀ ʙᴀᴄᴋᴜᴘ
                4 : Qᴜɪᴛ
            """)

        choice = input("Eɴᴛᴇʀ ᴀ ᴄʜᴏɪᴄᴇ : ")
        while not choice in ("1234") or not choice.isdigit() or choice == "":
            choice = input("Eɴᴛᴇʀ ᴀ ᴄʜᴏɪᴄᴇ : ")

        choice = int(choice)
        if choice == 1:
            clear_screen()

            name_player_1, name_player_2 = "",""
            while name_player_1 == "" or name_player_2 == "":
                print("Fɪʀꜱᴛ ᴡᴇ ᴡɪʟʟ ᴀᴅᴅ ᴛʜᴇ ɴᴀᴍᴇꜱ ᴏғ ᴛʜᴇ 2 ᴘʟᴀʏᴇʀꜱ\n")
                name_player_1 = input("Aᴅᴅ ғɪʀꜱᴛ ᴘʟᴀʏᴇʀ ɴᴀᴍᴇ : ")
                name_player_2 = input("Aᴅᴅ ᴛʜᴇ ɴᴀᴍᴇ ᴏғ ᴛʜᴇ ꜱᴇᴄᴏɴᴅ ᴘʟᴀʏᴇʀ : ")

                if name_player_1 == "" or name_player_2 == "":
                    print("Oɴᴇ ᴏғ ᴛʜᴇ ғɪᴇʟᴅꜱ ɪꜱ ᴇᴍᴘᴛʏ")
                    sleep(1.5),clear_screen()

            confirm_name = ""
            while not confirm_name in ("no", "yes","n","y"):
                confirm_name = input("\nCᴏɴғɪʀᴍ ɴᴀᴍᴇꜱ ? (ʏᴇꜱ/ɴᴏ) : ").lower()

                while confirm_name in ("no", "n") or name_player_1 == "" or name_player_2 == "":
                    name_player_1 = input("Aᴅᴅ ғɪʀꜱᴛ ᴘʟᴀʏᴇʀ ɴᴀᴍᴇ : ")
                    name_player_2 = input("Aᴅᴅ ᴛʜᴇ ɴᴀᴍᴇ ᴏғ ᴛʜᴇ ꜱᴇᴄᴏɴᴅ ᴘʟᴀʏᴇʀ : ")
                    confirm_name = ""

            clear_screen()
            print(f"\nTʜᴇ 2 ᴘʟᴀʏᴇʀꜱ ᴀʀᴇ : {name_player_1} ᴀɴᴅ {name_player_2}")
            sleep(1)
            
            player0 = Player(name_player_1,80, 50)
            player1 = Player(name_player_2,80, 50)

            game = Game(player0,player1)
            game.play()


        elif choice == 2:
            clear_screen()

            name_player_1 = ""
            while name_player_1 == "" :
                print("Fɪʀꜱᴛ ᴡᴇ ᴡɪʟʟ ᴀᴅᴅ ʏᴏᴜʀ ɴᴀᴍᴇ \n")
                name_player_1 = input("Aᴅᴅ ʏᴏᴜʀ ɴᴀᴍᴇ : ")

                if name_player_1 == "":
                    print("ᴛʜᴇ ғɪᴇʟᴅ ɪꜱ ᴇᴍᴘᴛʏ")
                    sleep(1.5),clear_screen()

            confirm_name = ""
            while not confirm_name in ("no", "yes","n","y"):
                confirm_name = input("\nCᴏɴғɪʀᴍ ɴᴀᴍᴇ ? (ʏᴇꜱ/ɴᴏ) : ").lower()

                while confirm_name in ("no", "n") or name_player_1 == "":
                    name_player_1 = input("Aᴅᴅ ʏᴏᴜʀ ɴᴀᴍᴇ : ")
                    confirm_name = ""

            clear_screen()
            print(f"\nTʜᴇ 2 ᴘʟᴀʏᴇʀꜱ ᴀʀᴇ : {name_player_1} ᴀɴᴅ Jusepe")
            sleep(1)
            
            player0 = Player(name_player_1,80, 50)
            player1 = AI("Jusepe",80, 50)

            game = Game(player0,player1)
            game.play()
        
        
        elif choice == 3:
            clear_screen()
            try: 
                backup_game().play()
                print("Yᴏᴜ ᴀʀᴇ ʙᴀᴄᴋ, ᴄᴀʀʀʏ ᴏɴ\n")
                print("Bᴏᴛʜ ᴘᴀꜱꜱ ʏᴏᴜʀ ᴛᴜʀɴ ᴛᴏ ᴅɪꜱᴘʟᴀʏ ᴛʜᴇ ᴛᴀʙʟᴇ")
            except FileNotFoundError : 
                print("Tʜᴇʀᴇ ɪꜱ ɴᴏ ʀᴇᴄᴏʀᴅᴇᴅ ɢᴀᴍᴇ")
                sleep(1)
            except pickle.UnpicklingError:
                print("Wᴀʀɴɪɴɢ: Bᴀᴄᴋᴜᴘ Cᴏᴍᴘʀᴏᴍɪꜱᴇᴅ. Uɴᴀʙʟᴇ ᴛᴏ ʟᴏᴀᴅ ᴛʜᴇ ɢᴀᴍᴇ.")
                sleep(1)
            except EOFError:
                print("Wᴀʀɴɪɴɢ: Bᴀᴄᴋᴜᴘ ғɪʟᴇ ᴄᴀɴɴᴏᴛ ʙᴇ ʀᴇᴀᴅ. Uɴᴀʙʟᴇ ᴛᴏ ʟᴏᴀᴅ ɢᴀᴍᴇ")
                sleep(1)
            except Exception as error:
                print("Uɴᴋɴᴏᴡɴ ᴇʀʀᴏʀ")
                sleep(1)

        elif choice == 4: 
            
            print("Bʏᴇ")
            sleep(1)
            print("Fᴏʀғᴇɪᴛ . . .")
            sleep(2)
            quit()