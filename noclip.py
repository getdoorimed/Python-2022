from adventurelib import *
Room.items = Bag()
#Imports

#Define Rooms

bedroom = Room("""
	A very nice looking bedroom, there seems to be a door ahead, something tells you that you have to
	go through it.""")
hallway1 = Room("""
	After enetering the door. you fall into a long and massive hallway with a menacing looking door that
	glows purple light at the end.""")
hallway2 = Room("""
	You move closer to the door, you feel an unpleasant feeling as you get closer.""")
hallway3 = Room("""
	You're nearly there, the unpleasant feeling gets stronger but you decide to move in anyways.""")
hallway4 = Room("""
	You reach the door, but is it really worth going in? you ask yourself.
	You decide to head in anyway.""")
room1 = Room("""
	You come in and you see a dull looking set of rooms, something tells you that something doesn't feel right.""")
room2 = Room("""
	The same set of dull looking rooms but something doesn't feel right""")
room3 = Room("""
	So many things are going in this room would you like to look around?""")
room4 = Room("""
	This room seems locked, you should look around for a key in the previous rooms.""")
room5 = Room("""
	You enter the room that you unlocked, you find a note that says "for every wrong turn you make-" then  """)
room6 = Room("""
	""")
room7 = Room("""
	""")
room8 = Room("""
	""")
room9 = Room("""
	""")
room10 = Room("""
	""")
exit = Room("""
	""")

#Define Connections

bedroom.north = hallway1

hallway1.north = hallway2
hallway2.north = hallway3
hallway3.north = hallway4


room1.west = room2

room2.north = room3
room2.west = room1
room2.east = room1
room2.south = room1


room3.west = room4
room3.north = room1
room3.east = room1
room3.south = room2

room4.north = room5
room4.east = room3
room4.west = room1
room4.south = room1

room5.north = room6
room5.east = room1
room5.south = room5
room5.west = room1

room6.west = room1
room6.north = room1
room6.east = room7
room6.south = room5

room7.east = room8
room7.north = room1
room7.west = room6
room7.south = room1

room8.east = room9
room8.north = room1
room8.south = room1
room8.west = room7

room9.north = room1
room9.east = room1
room9.west = room8
room9.south = room9

room10.north = room9
room10.west = room1
room10.east = room1
room10.south = exit

#Define Items
current_room = bedroom
inventory = Bag()



#Define Bags


room1.items.add("doll")


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

gold_key = Item("gold key")
gold_key.description = "This golden key must be important, you should pick it up"

#Add Items to Bags

@when("enter room")
@when("enter bedroom")
def enter_bedroom():
	global current_room
	#check in action can be done
	if current_room is not bedroom:
		say("You aren't allowed in here...")
		return
	else:
		current_room = bedroom
		print("""You get into your bedroom as you prepare to rest for the night.""")
		print(current_room)

@when("enter door")
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



@when("look")
def look():
	print(current_room)
	print(f"There are exits to the {current_room.exits()}.")
	if len(current_room.items) > 0:
		print("You also see: ")
		for items in current_room.items:
			print(items)

@when("get ITEM")
@when("take ITEM")
@when("pick up ITEM")
def pickup(item):
	if item in current_room.items:
		t = current_room.items.take(item)
		inventory.add(t)
		print(f"You pick up the {item}")
	else:
		print(f"You don't see a {item}")



@when ("go DIRECTION")
@when ("move DIRECTION")
def travel(direction):
	global current_room
	if direction in current_room.exits():
		current_room = current_room.exit(direction)
		print(f"You go {direction}.")
		print(current_room)
	
@when("inventory")
@when("show inventory")
@when("what is in my pocket")
def player_inventory():
	print("You are carrying these items:")
	for item in inventory:
		print(item)

@when("look at ITEM")
@when("inspect ITEM")
@when("view ITEM")
def look_at(item):
	if item in inventory:
		t = inventory.find(item)
		print(t.description)
	else:
		print(f"You aren't carrying an {item}")




#Define any variable


#Bind (eg"@when("look"))


#Main



def main():
	start()

if __name__ == '__main__':
	main()