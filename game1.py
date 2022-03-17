from adventurelib import *


@when("brush teeth")
@when("brush")
@when("clean teeth")
@when("clean mouth")
@when("brush mouth")
def brush_teeth():
	print("You brush your teeth")

@when("comb hair")
@when("comb")
def comb_hair():
	say("""
		You brush your long flowing locks with
		the gold hairbrush that you have selected from the
		in the red basket.
		""")

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


@when("enter airlock")
@when("enter spaceship")
@when("enter ship")
def enter_spaceship():
	global current_room
	#check in action can be done
	if current_room is not space:
		say("There is no airlock here")
		return
else:
	current_room = enter_spaceship
	print("""You heave yourself into the spaceship and slam you hand on the button to close the door.""")
	print(current_room)

#variables
current_room = space
spaceship.east = hallway
spaceship.south = quarters
hallway.east == bridge
hallway.north == cargo
hallway.south == mess_hall
hallway.west == airlock
cargo.east == docking
bridge.south == escape_pods
mess_hall.west == quarters


def main():
	start()

if __name__ == '__main__':
	main()