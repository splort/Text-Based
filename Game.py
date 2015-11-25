sanity = 25
print ("You wake up with no memory of anything. A gun lies on the table beside you, and bullets are spread about it.")
pistolOne = input ("Do you pick it up or not?").lower()
if pistolOne == ("yes"):
     print ("The gun is cold in your hand, and very heavy. You, despite your amnesia, expertly load the weapon. Your attention then turns to the dark room around you.")
     pistolAmmo = 6
else:
      print ("You stand, ignoring the gun, and turn in a circle, surveying the dark room around you.")
print ("The room offers little in the way of comfort, but a chest of drawers rests conspicuously in the corner, and a door is opposite you. The darkness shoruds all else.")
roomQ = input ("Do you go to the door, the chest of drawers, or explore further?").lower()
roomOne = ("drawers")
roomOneA = ("door")
roomOneB = ("explore")
if roomOne in roomQ:
    print ("You approach the chest of drawers cautiously. It is dull and brown, with no outstanding features. The first drawer contains naught but a small crayon, the second contains a key, and the third holds a file.")
    fileA1 = input("Do you wish to read the file?")
    if fileA1 == ("yes"):
        print ("In typed writing, the otherwise blank sheet of paper reads, 'Subject 32 is holding up surprisingly well to the psychoevaluation regime. With minimal stress levels, and only minor injuries sustained when the subject attempted to slit her wrists on a shard of broken glass, the patient is definitely superior in every way to most others in our ward.")
        print ("She does, however, have an annoying habit of doodling; on the paper, on the walls, sometimes even on herself. Drawings best left undescribed, more often than not about some entity she calls the Spectre. I recommend an extra supply of paper for her, but have no authority to do so. Please advise.'")
        roomQ = input ("Do you wish to explore further or go to the door?")
        if roomOneA in roomQ:
            print ("You walk towards the door; it is tall, towering above you, and very old. You try the metallic doorknob, but to no avail.")
            print ("You insert the key; it connects to the back with a dull sound. The doorknob moves freely when twisted, and you step out of the room.")
        elif roomOneB in roomQ:
            print ("You venture deeper into the room. A small parchment, face down and stained with what looks like tea, sits in a dark corner.")
            exploreOne = input ("Do you pick it up or not?")
            if exploreOne == ("yes"):
                print ("You bend down to pick it up, and a blast of wind rushes past you, taking the sheet along with it. You catch a glimpse of hair, and the putrid stench of blood invades your nostrils.")
                sanity = sanity - 3
                print ("After that terrible ordeal, you return to the piece of paper. It is now face up, displaying a collection of scribbles drawn by the hand of a baby; pictures of a small child in a tunnel, walking towards a bright light, hand in hand with a figure of the blackest black.")
            else:
                print ("You turn away, and a blast of wind rushes past you, taking the sheet along with it. You catch a glimpse of hair, and the putrid stench of blood invades your nostrils.")
                sanity = sanity - 3
                if pistolOne == ("yes"):
                    print ("You spin around wildly, gun in hand, breathing heavily. Nothing.")
                else:
                    print ("You spin around wildly, striking out at random, but stop when you find nothing there.")
            print ("The door that had been closed not moments before now lay open. The doorknob is red and dripping with blood.")
elif roomOneB in roomQ:
    print ("At the back of the room, in a dark corner, lies a small parchment, seemingly face down and stained with what seems like tea.")
    print ("There is a terrible blast of sound to the direction of the wardrobe. As you spin around in fear, a gust of wind rushes past you. You catch a glimpse of hair, and the putrid stench of blood invades your nostrils.")
    sanity = sanity - 3
    print ("You scream, wheeling madly in search of danger. When you ascertain that there is none, you realise something - the door that had been closed not moments before lay open. The doorknob is red and dripping with blood.")
    if pistolOne == ("Yes"):
        print ("You stalk out, pistol up and finger on the trigger. No threat readily presents itself, but the pistol remains raised. The corridor branches off to the left and right, with another door opposite. The irony smell of blood pervades your senses again, drawing your gaze towards your left - where you catch the merest of glimpses of the hem of a dress before it disappears around the corner.")
    else:
        print ("You creep out, hands shaking slightly, and look around the corner to the right; you smell the rich iron of blood to the other direction, and turn just in time to catch the hem of a dress disappear around the corner.")
        sanity = sanity - 1
decisionOne = input ("Do you go to the left or the right?").lower()
if decisionOne == ("left"):
    print ("You stalk around the corner, curiosity overriding fear for a moment. Turning where you last saw... whatever it was... you find yourself at a door. A door with the words 'Nursery A' inscribed into it.")
    nurseryADoor = input ("Do you try the door or turn back?").lower()
    nurseryADoorA = ("door")
    if nurseryADoorA in nurseryADoor:
        print ("You fumble in the darkness for the handle, twisting it until the door creaks open. The room, unlike the corridor, is well lit by a campfire to one side. A set of three unlit candles sit atop a table, holding an obscured a sheet of paper up behind them.")
    else:
        print ("You turn back, and return to the first door. Striding past it, you go the way opposite to where you were before.")
        print ("You try the door, but it won't budge - it doesn't seem to be locked, so you figure there must be something holding it back from the other side.")
        print ("With no other option left, you return to the other door.")
print ("The room, despite the fire, is cold and foreboding. A door rests closed to the far right, and another is barred shut with far more locks than is necessary.")
nurseryDecision = input ("Do you explore further or try the door?").lower()
nurseryDecisionA = ("door")
if nurseryDecisionA in nurseryDecision:
    print ("You stroll past the fire, and the candles, and reach for the door. As you turn the door knob, you feel a deep, foreboding chill seep through. Pausing, you look around you for a threat; you then open the door.")
    print ("You shut the door just as quickly, taking in deep breaths and backing away from the corridor beyond. It ends in another room, no doubt the room you tried earlier, and there is an intersection halfway there.")
    print ("Worst of all, however, is the pale figure framed in the darkness; the little girl who's dress flows through the ground and who's edges blur into the background. Who's flesh is as opaque as a mirror.")
    sanity = sanity - 5
    print ("You gingerly pull the door towards you, careful not to make a noise. Upon closer inspection, the little girl seems to be about eight. She is facing the ground, white hair covering her face, hands to her side, feet clasped together.")
    if pistolOne == ("yes"):
        print ("You raise your gun, acutely aware of how ineffectual it would be, and take a single, soft step. Her head moves slowly upwards to reveal pale skin, and deep, black eyes. Her white lips part to reveal bloody lips in an otherwise innocent smile.")
    else:
        print ("You, trembling, take single, soft step. Her head moves slowly upwards to reveal pale skin, and deep, black eyes. Her white lips part to reveal bloody teeth in an otherwise innocent smile.")
    sanity = sanity - 5
else:
    print ("You examine the flame curiously. It feels old, its movements lethargic, its heat dulled. You frown slightly, then turn to the candles.")
    print ("They are normal, as waxy as one would expect, and as unlit as they were before. You reach out to take the paper, and a gust of wind with unknown origin blows the fire out. You wheel around in the darkness, only to find the candles have been lit. On the now readable piece of paper, a single arrow, scrawled in dried blood, points to the door. You, involuntarily, look that way, and freeze.")
    print ("A pale figure is framed in the darkness; a little girl, who's dress flows through the ground and who's edges blur into the background. Who's flesh is as opaque as a mirror.")
    sanity = sanity - 5
    print ("Upon closer inspection, the little girl seems to be about eight. She is facing the ground, white hair covering her face, hands to her side, feet clasped together.")
    if pistolOne == ("yes"):
        print ("You raise your gun, acutely aware of how ineffectual it would be, and take a single, soft step. Her head moves slowly upwards to reveal pale skin, and deep, black eyes. Her white lips part to reveal bloody lips in an otherwise innocent smile.")
    else:
        print ("You, trembling, take a single, soft step. Her head moves slowly upwards to reveal pale skin, and deep, black eyes. Her white lips part to reveal bloody lips in an otherwise innocent smile.")
    sanity = sanity - 5
print ("She stops smiling suddenly. You back up, but instead of attacking, she simply looks up to above her shoulder, where she rests her hand on thin air. You take another step forwards, trying to see wat she had touched, but she looks back at you, and splits into a milliom wisps of wind that disperse into the dark corridor.")
sanity = sanity - 1
