import pickle
from time import sleep


def save_quit(current_game):
    """
    create a file,
    write in binary,
    And serialization
    """
    with open("save_game.data", "wb") as file:
        pickle.dump(current_game, file)
    print("Tʜᴇ ɢᴀᴍᴇ ɪꜱ ꜱᴀᴠᴇᴅ. Cᴏᴍᴇ ʙᴀᴄᴋ ᴡʜᴇɴ ʏᴏᴜ ᴡᴀɴᴛ")
    sleep(2)
    quit()

def backup_game():
    """
    Read the contents of the file,
    Deserialize it
    """
    with open("save_game.data", "rb") as file:
        data = pickle.Unpickler(file)
        back_game = data.load()
    return back_game