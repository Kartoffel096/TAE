#ToDo's:
#Spielerklasse
#Levelklasse
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#








from pystyle import Write, Box, Center, Colors

from time import sleep



lvl = 0
action = ""

def pr(text):
    Write.Print(text + "\n", Colors.red_to_purple, interval=0.0025)

#verinfachte Printanweisung in roter farbe für alerts
def pra(text):
    Write.Print(text + "\n", Colors.red, interval=0.0025)

def pri(text):
    Input = Write.Input(text + "\n→ ", Colors.red_to_purple, interval=0.0025)
    return Input



class Player():

    name = "Blankoname"
    health = 100
    wealth = 100
    xp = 0
    inv = [["Waffen"],["Rüstung"],["Usables"],["Questitems"],["Misc"]]

    def __init__(self):
        pass
    
    def set_name(self):
        while True:
            global name
            self.name = pri("Wie soll der Held deiner Geschichte heißen?")
            pr(f"Möchtest du deinen Helden wirklich {self.name} nennen?")
            action = pri("[DIESE EINSTELLUNG KANNST DU NICHT RÜCKGÄNGIG MACHEN!](y/n)")
            if action == "y":
                break

    def get_name(self):
        pr(f"Dein Held heißt {self.name}.")
        
        


#lvl1 vars:
lvl1_umgesehen = False
#vereinfachte Printanweisung mit Write und Color


# while True:
#     while lvl == 0:
#         Write.Print(Box.Lines("Nicks Textadventure!"), Colors.dark_red, interval=0.02)
#         choices = "1. Spiel starten\n2. Spielstand laden\n3.Spiel beenden\n4.debug mode"
#         action = Write.Input(Center.XCenter(choices + "\n→ "), Colors.red_to_purple, interval=0.0025)
#         if action == "1":
#             lvl = 1
#             print("\n\n\n\n\n")
#         if action =="2":        
#             pass

#     while lvl == 1:
#         Write.Print("\n" + "#"*50 + "\n\n", Colors.red_to_purple, interval=0.0025)
#         if lvl1_umgesehen == False:
#             Write.Print("Du wachst auf.\nDein Schädel brummt.\nDu öffnest deine Augen und schaust dich um.\nGeblendet von der Sonne erkennst du, dass du auf einer Wiese bist.\n", Colors.red_to_purple, interval=0.0025)
#             choices = "\n1. Umsehen\n2. Etwas gegen deine Kopfschmerzen machen\n"
#             action = Write.Input(choices + "\n→ ", Colors.red_to_purple, interval=0.0025)
#         if lvl1_umgesehen == True:
#             Write.Print("Du wachst auf.\nDein Schädel brummt.\nDu öffnest deine Augen und schaust dich um.\nGeblendet von der Sonne erkennst du, dass du auf einer Wiese bist.\nDu siehst einen Weg.\nIn der Ferne siehst du die Umrisse einer Stadt.\n", Colors.red_to_purple, interval=0.0025)
#             choices = "1. Umsehen\n2. Etwas gegen deine Kopfschmerzen machen\n3. Den Weg entlanggehen\n"
#             action = Write.Input(choices + "\n→ ", Colors.red_to_purple, interval=0.0025)

#         if action == "1":
#             pr("Du siehst dich um.\nDu siehst einen Weg.\nIn der Ferne siehst du die Umrisse einer Stadt.\n")
#             lvl1_umgesehen = True
#             sleep(2)
#         if action == "2":
#             pr("Du schüttelst deinen Kopf, die Kopfschmerzen verschwinden.")
#             Write.Print("[Statuseffekt] (Kopfschmerz) verschwindet!" + "\n", Colors.red, interval=0.0025)
#             sleep(2)
#         if action == "3" and lvl1_umgesehen == True:
#             pr("Du stehst auf und gehst zu dem Weg.\nDer Weg ist ein schmutziger, kleiner Trampelpfad.\n")



if __name__ == "__main__":
    Player()
    Player.get_name(self=Player)







