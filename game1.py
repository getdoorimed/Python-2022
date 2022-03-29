from adventurelib import *
Room.items = Bag()

#define rooms

space = Room("""
	You are drifting in space. It feels very cold.
	A slate-blue spaceship sits completely silently to your left,
	its airlock open and waiting.
	""")

spaceship = Room("""
	The bridge if the spaceship is shiny and white, with thousands
	of small, red, blinking lights.
	""")

cargo = Room("The cargo room feels it has something SUS is hiding in it")

docking = Room("A place where ships land")

hallway = Room("a very menacing hallway... i wonder what lies in it...")

bridge = Room("a place that leads to the escape pods")

quarters = Room("Who made this room, i dont know what it's purpose is so rip lol.")

mess_hall = Room("A very messy hall.")

escape_pods = Room("A room that people who have no guts go to")

#connections

spaceship.east = hallway
spaceship.south = quarters
hallway.east = bridge
hallway.north = cargo
hallway.south = mess_hall
hallway.west = spaceship
cargo.east = docking
bridge.south = escape_pods
mess_hall.west = quarters

#define variables
current_room = space
inventory = Bag()


#define items
Item.description = "" #this adds a blank description to each item

knife = Item("a dirty knife","knife")
knife.description = "the knife has a dull sheen to it but it looks rather sharp."

red_keycard = Item("a red keycard","keycard","red card","red card")
red_keycard.description = "It's a red keycard. It seems you'll need it to try get out."

gun = Item("gun")
gun.description = "A rusty but handy handgun."

doll = Item("doll")
doll.description = "A menacing doll, i wonder what it does."



#adds items to bags



@when("enter room")
@when("enter bedroom")
def enter_spaceship():
	global current_room
	#check in action can be done
	if current_room is not space:
		say("You aren't allowed in here...")
		return
	else:
		current_room = spaceship
		print("""You get into your bedroom as you prepare to rest for the night.""")
		print(current_room)



@when("look")
def look():
	print(current_room)
	print(f"There are exits to the {current_room.exits()}.")
	if len(current_room.items) > 0: #if there are some items in the room
		print("You also see: ")
		for item in current_room.items:
			print(item)#print out each item

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
	print("You are carrying")
	for item in inventory:
		print(item)

@when("look at ITEM")
def look_at(item):
	if item in inventory:
		t = inventory.find(item)
		print(t.description)
	else:
		print(f"You aren't carrying an {item}")



def main():
	start()

if __name__ == '__main__':
	main()