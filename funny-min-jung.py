from Entities import Entity, item, itemInit
from Level import Level
from Effect import Effect
import Utils as pr 
import json

##################
##Debug Variable##
global dbg
dbg = True
##################

###################
###ENV Variables###
items_file = "config/items.json"
lvl = 0
action = ""
###################

def change_location(level, entity, level_index, old_level, new_level):

    entity.change_location(old_level, new_level)
    #theo mit reh und tisch müsste hier jetzt eine umwandlung vom alten zum neuen level_index kommen
    #da ich aber grade selbst den durchblisck verloren habe, mache ich kurz pause und gucke später ob diese 
    #mönströsität von kontrollstruktur sinnhaftig ist


def hud(player, level):
    pr.n(f"Du befindest dich in: {level.name}")
    pr.n(f"Gold: {player.wealth}")
    pr.n(F"Level: {player.level} XP: {player.xp}")
    #hudfunction


def gameloop(player, level=[]):
    
    #print("*"*10 + "player" + "*"*10 + "\n")
    #print(vars(player))
    
    level_index = 0             #Index that corresponds to level from level[]
    lap = 0
    while True:
        current_level = level[level_index]
        
        hud(player, level[level_index])
        for e in current_level.entitylist:
            for a in list(e.actionstack.queue):
                pr.dbg(a)
        ###Todo Action parser for actionstack (pass entity to which the action applies, pass the action, process action on entity, return successfull or error)
        ##############################################

        nirvana.change_entity_list("-", mPlayer)
        newnewLevel.change_entity_list("+", mPlayer)
        mPlayer.change_location(nirvana, newnewLevel)
        level_index = 1
        player.let_effects_take_effect(dbg)
        lap += 1
        player.xp += 100
        level_ups = player.check_level_up()
        if level_ups[0] > 0:
            mPlayer.actionstack.put(f"Level_Up: {level_ups[0]}")
            pr.dbg(mPlayer.actionstack.queue)
            pr.n(f"Du bist {level_ups[0]} Level aufgestiegen!")
        pr.pause()







if __name__ == "__main__":
    mPlayer = Entity("Player", 100,100,0,[item("Item1","weapon"),item("item2","misc")])
    h = Entity()
    #mPlayer.set_name()
    vergiftung = Effect("Vergiftung","Nö","bad", -10, "hp")
    heilung = Effect("heilung","Nö","good", 5, "hp")
    heilung2 = Effect("heilung2","Nö","good", 5, "hp")
    heilung3 = Effect("heilung 3","Nö","good", 5, "hp")
    terror = Effect("Terror","Nö","evil", -100, "xp")
    #print(vars(vergiftung))
    mPlayer.add_effect(vergiftung)
    mPlayer.add_effect(heilung)
    mPlayer.add_effect(heilung2)
    mPlayer.add_effect(heilung3)
    #mPlayer.add_effect(terror)
    # mPlayer.show_effects()
    #print(mPlayer.effects)
    #allItems = itemInit.load_all_items_from_json(items_file)
    #print(vars(itemInit.load_item_by_name_from_json(items_file, "Sword")))
    #print()
    #menu = Level(["Textadventure","Hauptmenü","spiel wird geladen"],["Spiel laden","Spiel starten","Spiel beenden"],"Hauptmenü",[],"zivilisiert","Mainmanu descr")
    #gameloop(mPlayer, menu)
    
    
    ####Add actions to Player Actionstack
    mPlayer.actionstack.put("Some Action from Actionstack")
    mPlayer.actionstack.put("Another Action from Actionstack")
    mPlayer.actionstack.put("And Another Action from Actionstack")
    mPlayer.actionstack.put("let_effects_take_effect")
    
    ####Create a New Level with Player as only Entity in Level
    nirvana = Level(["Du siehst einen Weg.",], ["Atmen", "Den Wen entlanggehen"],"Nirvana", [], "Testtype", "nirvana",[mPlayer])                  #hier chillen entitys die existieren ohne in einem level eingesetzt zu werden
    nowhere = Level([""], [],"nowhere", [], "Testtype", "nowhere",[])                         #Hommage für alte Textadventures
    newnewLevel = Level(["Du siehst einen Weg, der ins Nirvana führt."], ["Nachdenken","Ins Nirvana gehen"],"NewNewLevel", [], "Testtype", "NewNewLevel",[])
    ####Run Gameloop with nirvana as Level
    gameloop(mPlayer, [nirvana, newnewLevel])
    
    