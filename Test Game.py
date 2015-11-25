print ("You wake up to pain. Searing pain, racking your ribs and rendering your brain useless.")
print ("After a few minutes, the pain recedes, and you can finally stand up without fear of death.")
print ("The room you are in is lit by a small on the left. In front of you is a door, and another lies to the right.")
door = input ("Which way do you go?").lower()
if door == ("left"):
    print ("You find yourself in a dark corridor. There are three different paths you can take, but the lack of light comes with a fear that you can neither explain nor control. You start shaking until you back away.")
print ("You open a door and see nothing but a torch at the back. The floor seems to shift about you, but the darkness is too thick to see through.")
torch = input ("Do you take it or not?")
torchOne = ("no")
if torchOne not in torch:
    print ("You walk into the room. The floor is thick, like a liquid, but you manage to force yourself past and into the light.")
    print ("You take the torch gingerly, careful not to burn yourself, and turn around again. You finally see what you had walked through before.")
    print ("The floor is alive with rats, some no smaller than your foot, with others the lentgh of your arm.")
    ratFight = input ("Do you run or attack?").lower()
    if ratFight == ("run"):
        ("")