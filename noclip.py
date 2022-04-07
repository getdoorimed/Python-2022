from adventurelib import *
Room.items = Bag()


#Imports

#Define Rooms

backrooms0 = Room("""
	You noclip into the backrooms... instantly regretting the choice you decide you wanna get out because this place is spoopy.""")
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

invisible_wall_breaker = Item("invisible wall breaker")
invisible_wall_breaker.description = "This can be used to break through invisible walls!!! good job finding it."

rusty_gun = Item("rusty gun")
rusty_gun.description = "This gun seems to be old but it should work against any threats."
#Add Items to Bags

room1.items.add(doll)

room5.items.add(dead_body)



current_room = backrooms0
inventory = Bag()

@when("enter backrooms")
@when("enter bedroom")
def enter_backrooms():
	global current_room
	#check in action can be done
	if current_room is not backrooms0:
		say("You aren't allowed in here...")
		return
	else:
		current_room = backrooms0
		print(current_room)

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

@when("use ITEM")
def use(item):
	if inventory.find(item)==invisible_wall_breaker == lounge:
		print("You use the breaker to open this area")
		print("The invisible wall cracks open")
		room3.west = room4
		

@when ("go DIRECTION")
@when ("move DIRECTION")
def travel(direction):
	global current_room

	if current_room == room4 and direction == 'west':
		print("This door seems to be blocked with an invisible wall... you should try find an 'invisible wall breaker' in the past rooms to get through here")
		return

	if direction in current_room.exits():
		current_room = current_room.exit(direction)
		print(f"You go {direction}.")
		print(current_room)
	else:
		print("You can't go that way, you have to go back to the start")
		current_room = room1
	
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
	elif current_room == cargo and body_searched == True:
		print("You already searched this body")
	else:
		print("There is no body here to search")



#Define any variable


#Bind (eg"@when("look"))


#Main



def main():
	start()

if __name__ == '__main__':
	main()