from adventurelib import *

#Imports

#Define Rooms

bedroom = Room("""
	A very nice looking bedroom, there seems to be a door ahead""")

hallway1 = Room("""
	You fall into a wide and massive hallway with a menacing looking door at the end""")

hallway2 = Room("""
	You move closer to the door""")

hallway3 = Room("""
	You're nearly there""")

hallway4 = Room("""
	You reach the door""")

room1 = Room("""
	You come in and you see a dull looking set of rooms""")

room2 = Room("""
	The same set of dull looking rooms but something doesn't feel right""")

room3 = Room("""
	So many things are going in this room would you like to look around?""")




#Define Connections

bedroom.north = hallway1
hallway1.north = hallway2
hallway2.north = hallway3
hallway3.north = hallway4
hallway4.north = room1
room1.west = room2
room1.north = room1
room1.east = room1
room2.north = room3
room3.west = room4
room4


#Define Items
#Define Bags
#Add Items to Bags
#Define any variable
#Bind (eg"@when("look"))
#Main

def main():
	start()

if __name__ == '__main__':
	main()