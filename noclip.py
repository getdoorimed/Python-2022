from adventurelib import *
Room.items = Bag()


#Imports

#Define Rooms

backrooms0 = Room("""
	You noclip into the backrooms...
	instantly regretting the choice you decide you wanna get out because this place gives an unnerving feel.""")
room1 = Room("""
	You come in and you see a dull looking set of rooms, something tells you that something doesn't feel right.""")
room2 = Room("""
	The same set of dull looking rooms but something doesn't feel right""")
room3 = Room("""
	So many things are going in this room would you like to look around?""")
room4 = Room("""
	There's not much in this room, except for the noise that you heard from the start gets louder""")
room5 = Room("""
	You enter the room that you unlocked, you find a note that says "for every wrong turn you make-" then  """)
room6 = Room("""
	As you head in further in the backrooms, the unsettling feeling dissapears...for now.""")
room7 = Room("""
	You see a figure running towards you""")
room8 = Room("""
	A locked door... You wonder what could happen if you go through it.""")
room9 = Room("""
	You see a light towards you but it seems that this is far from over.""")
room10 = Room("""
	The door for the exit is close, you'll finally be free.""")
exit = Room("""
	You leave the backrooms!!! congratulations you beat the game... wait... where are we...
	this doesn't seem like the outside world?

	TO BE CONTINUED....""")

#Define Connections

backrooms0.north = room1

room1.west = room2

room2.north = room3

room3.west = room4

room4.north = room5

room5.north = room6

room6.east = room7

room7.east = room8

room8.east = room9

room9.south = room10

room10.south = exit

#Define Items






#Define Bags


Item.description = "" #this adds a blank description to each item

knife = Item("a dirty knife","knife")
knife.description = "the knife has a dull sheen to it but it looks rather sharp."

red_keycard = Item("a red keycard","red card")
red_keycard.description = "It's a red keycard. It seems you'll need it to try get out."

blue_keycard = Item("a blue keycard","blue card")

gun = Item("gun")
gun.description = "a rusty but handy handgun."

doll = Item("doll")
doll.description = "a menacing doll, i wonder what it does."

dead_body = Item("dead body")
dead_body.description = "This body seemed like it's been here for quite a time."

gold_key = Item("gold key")
gold_key.description = "This golden key must be important, you should pick it up"


bag = Item("gun")
bag.description = "Something seems to be in this bag."

#Add Items to Bags


room1.items.add(doll)
room2.items.add(red_keycard)
room3.items.add(bag)
room5.items.add(dead_body)
room7.items.add(gold_key)
room2.items.add(knife)
room8.items.add(gun)

#This defines variables
current_room = backrooms0
inventory = Bag()
room4_unlocked = False
room8_unlocked = False
exit_unlocked = False

@when("enter backrooms")
@when("enter bedroom")
def enter_backrooms():
	global current_room
	#check if action can be done
	if current_room is not backrooms0:
		say("You aren't allowed in here...")
		return
	else:
		current_room = backrooms0
		print(current_room)

#this lets you start the game
@when("enter door")
@when("noclip backrooms")
@when("go to the door")
@when("go inside the door")
def enter_door():
	global current_room
	if current_room is not hallway4:
		say("What are you doing?")
		return
	else:
		current_room = hallway4
		print("""You enter the door""")
		print(current_room)


#This code makes it so you can look for items in the room you are in
@when("look")
def look():
	print(current_room)
	print(f"There are exits to the {current_room.exits()}.")
	if len(current_room.items) > 0:
		print("You also see: ")
		for items in current_room.items:
			print(items)

#This code lets you pick up items 
@when("get ITEM")
@when("take ITEM")
@when("pick up ITEM")
def pickup(item):
	if item in current_room.items:
		t = current_room.items.take(item)
		inventory.add(t)
		print(f"You pick up the {item}")
	else: #Code that shows what will happen if you dont see an item
		print(f"You don't see a {item}")

#shows you what's in your inventory		
@when("inventory")
@when("show inventory")
@when("what is in my pocket")
def player_inventory():
	print("You are carrying these items:")
	for item in inventory:
		print(item)

#lets you look at the item description
@when("look at ITEM")
@when("inspect ITEM")
@when("view ITEM")
def look_at(item):
	if item in inventory:
		t = inventory.find(item)
		print(t.description)
		pass
	else:
		print(f"You aren't carrying an {item}")



@when("search body")
@when("look at body")
@when("search corpse")
@when("look at corpse")
def search_body():
	global body_searched
	if current_room == room5 and body_searched == False:
		print("you search the dead body and you hear a noise rustle behind you, you find a rusty pistol in the process")
		current_room.items.add(rusty_gun)
		body_searched = True
	elif current_room == room5 and body_searched == True:
		print("You already searched this body")
	else:
		print("There is no body here to search")

@when("search bag")
@when("look at bag")
@when("search bag")
@when("look at bag")
def search_bag():
	global bag_searched
	if current_room == room3 and bag_searched == False:
		print("You search the bag")
		current_room.items.add(gun)
		bag_searched = True 
	elif current_room == room3 and body_searched == True:
		print("You already searched this bag")
	else:
		print("There is no body here to search")

#these set of codes makes it so you can use items to open locked areas
@when("use red keycard")
@when("use red card")
def use_red_keycard():
	global room4_unlocked
	global current_room
	if current_room == room3 and inventory.find("red keycard"):
		say("You unlocked the door.")
		room4_unlocked = True 
	elif current_room is not room3:
		say("You cannot use that here.")

@when("use blue keycard")
@when("use blue card")
def use_blue_keycard():
	global room8_unlocked
	if current_room == room7 and inventory.find("blue keycard"):
		say("You unlocked the door.")
		room8_unlocked = True 
	elif current_room is not room7:
		say("You cannot use that here.")

@when("use gold key")
@when("use key")
def use_gold_key():
	global exit_unlocked 
	if current_room == room10 and inventory.find("gold key"):
		say("You unlocked the final door.")
		exit_unlocked = True
	elif current_room is not room10:
		say("You cannot use that key here, perhaps you can use it somewhere else.")

#direction code that confirms the directions for being locked or making it so if you go the wrong way
#you go back to the start
@when ("go DIRECTION")
@when ("move DIRECTION")
def travel(direction):
	global current_room
	
	if room4_unlocked == True:
		room3.west = room4


	if current_room == room3 and room4_unlocked == False and direction == 'west':
		print("This Area is locked")
		return

	if current_room == room7 and room8_unlocked == False and direction == 'east':
		print("This Area seems to be locked")
		return

	if direction in current_room.exits():
		current_room = current_room.exit(direction)
		print(f"You go {direction}.")
		print(current_room)
	else:
		print("You can't go that way, you have to go back to the start")
		current_room = room1



#Define any variable


#Bind (eg"@when("look"))


#Main



def main():
	start()

if __name__ == '__main__':
	main()