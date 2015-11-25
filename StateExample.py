import re
import random

class MainHall:
  def __init__(self, game):
    # We need this for game context (exit, items)
    self.game = game
    # Regular expressions to match user response
    self.left = re.compile('left', re.IGNORECASE)
    self.right = re.compile('right', re.IGNORECASE)
    # No recognised action comes back here
    self.nextState = 'hall' # no recognised action comes back here

  # Main logic of this state / room
  def run(self):
    print "You found yourself in what seems to be a main hall. There are exits to the left and right."
    action = raw_input("$ ")
    if (self.game.match(action)):
      return
    if (self.left.match(action)):
      self.nextState = 'storage'
    elif (self.right.match(action)):
      self.nextState = 'corridor'

  # Returns the next state (which could still be this one)
  def next(self):
    return self.nextState

class Storage:
  def __init__(self, game):
    # We need this for game context (exit, items)
    self.game = game
    # Regular expressions to match user response
    self.back = re.compile('back', re.IGNORECASE)
    self.pick = re.compile('(pick|take).*torch', re.IGNORECASE)
    self.kick = re.compile('kick.*rat', re.IGNORECASE)
    # No recognised action comes back here
    self.nextState = 'storage' # no recognised action comes back here

  # Main logic of this state / room
  def run(self):
    print "This is the storage. There is a torch and lots or rats."
    action = raw_input("$ ")
    if (self.game.match(action)):
      return
    if (self.back.match(action)):
      self.nextState = 'hall'
    elif (self.pick.match(action)):
      if (self.game.items.count('torch')):
        print "You already have the torch."
      else:
        self.game.items.append('torch')
        print "You've picked up the torch."
    elif (self.kick.match(action)):
      print "You kicked a rat and it squealed loudly."

  # Returns the next state (which could still be this one)
  def next(self):
    return self.nextState

# State: Corridor
class Corridor:
  def __init__(self, game):
    # We need this for game context (exit, items)
    self.game = game
    # Regular expressions to match user response
    self.back = re.compile('back', re.IGNORECASE)
    self.left = re.compile('left', re.IGNORECASE)
    self.forward = re.compile('forward', re.IGNORECASE)
    self.right = re.compile('right', re.IGNORECASE)
    # No recognised action comes back here
    self.nextState = 'corridor'

  # Main logic of this state / room
  def run(self):
    if (self.game.items.count('torch')):
      print "This is the corridor. You can see some doors - one to the left, one to the right, and one directly ahead."
      print "Which way do you go?"
      action = raw_input("$ ")
      if (self.game.match(action)):
        return
    if (self.left.match(action)):
      self.nextState = 'armoury'
    elif (self.forward.match(action)):
      self.nextState = 'key'
    elif (self.right.match(action)):
      self.nextState = 'boss'
    else:
      print "It's too dark in here. You better go back."
      action = raw_input("$ ")
      if (self.game.match(action)):
        return
      if (self.back.match(action)):
        self.nextState = 'hall'

  # Returns the next state (which could still be this one)
  def next(self):
    return self.nextState

class Armoury:
  def __init__(self, game):
    # We need this for game context (exit, items)
    self.game = game
    # Regular expressions to match user response
    self.axe = re.compile('(pick|take).*axe', re.IGNORECASE)
    self.back = re.compile('back', re.IGNORECASE)
    # No recognised action comes back here
    self.nextState = 'armoury' # no recognised action comes back here

  # Main logic of this state / room
  def run(self):
    print "You seem to be in an armoury; an axe rests on the floor in front of you."
    action = raw_input("$ ")
    if (self.game.match(action)):
      return
    if (self.axe.match(action)):
      if (self.game.items.count('axe')):
        print "You already have the axe."
      else:
        self.game.items.append('axe')
        print "You picked up the axe."
    elif (self.back.match(action)):
      self.nextState = 'corridor'

  # Returns the next state (which could still be this one)
  def next(self):
    return self.nextState

class KeyRoom:
  def __init__(self, game):
    # We need this for game context (exit, items)
    self.game = game
    # Regular expressions to match user response
    self.left = re.compile('left', re.IGNORECASE)
    self.right = re.compile('right', re.IGNORECASE)
    self.key = re.compile('(pick|take).*key', re.IGNORECASE)
    self.back = re.compile('back', re.IGNORECASE)
    self.barricade = False
    # No recognised action comes back here
    self.nextState = 'key' # no recognised action comes back here

  # Main logic of this state / room
  def run(self):
    print "The door is barred shut by several planks of wood."
    if (self.game.items.count('axe')):
      if self.barricade == False:
        print "You swing the axe vehemently, splintering the makeshift barricade."
        self.barricade = True
      print "The room is dark and dusty."
      if (self.game.items.count('key') == False):
        print "A key glints faintly in the corner. Do you take it?"
        action = raw_input("$ ")
        if (self.key.match(action)):
          self.game.items.append('key')
          print "You picked up the key."
    else:
      print "The barricade is far too sturdy for you to break off with your bare hands. You should go back."
    action = raw_input('$ ')
    if self.back.match(action):
      self.nextState = 'corridor'

  # Returns the next state (which could still be this one)
  def next(self):
    return self.nextState

class BossRoom:
  def __init__(self, game):
    # We need this for game context (exit, items)
    self.game = game
    # Regular expressions to match user response
    self.back = re.compile('back', re.IGNORECASE)
    # No recognised action comes back here
    self.nextState = 'boss' # no recognised action comes back here

  # Main logic of this state / room
  def run(self):
    print "The door ahead has a big padlocked chained across its surface."
    if (self.game.items.count('key')):
      print "You insert the key and twist. The padlock clicks open, and you open the door."
    else:
      print "You don't even try the padlock; you should probably try another way."
    action = raw_input('$ ')
    if (self.game.match(action)):
      return
    if self.back.match(action):
      self.nextState = 'corridor'

  # Returns the next state (which could still be this one)
  def next(self):
    return self.nextState

# Main state machine (knows all states, has game context)
class TextBased:
  def __init__(self):
    # Initialise all states, pass the game context (self)
    self.hall = MainHall(self)
    self.storage = Storage(self)
    self.corridor = Corridor(self)
    self.armoury = Armoury(self)
    self.key = KeyRoom(self)
    self.boss = BossRoom(self)
    # Initialise the items list
    self.items = list()
    # Exit condition (states set this to quit)
    self.exit = False
    # Current state
    self.state = self.hall
    # Global commands (work on every room)
    self.quit = re.compile('(quit|exit)', re.IGNORECASE);

  # Match global commands (returns true if matched anything)
  def match(self, action):
    if (self.quit.match(action)):
      self.exit = True
      return True
    return False

  # Main run method, infinite loop until "exit" is requested
  def run(self):
    while (not self.exit):
      self.state.run()
      self.nextState(self.state.next())
    print "Game Over. Thanks for playing"

  # Next state set by current state's logic
  def nextState(self, next):
    if (next == 'exit'):
      self.exit = True
    elif (next == 'hall'):
      self.state = self.hall
    elif (next == 'storage'):
      self.state = self.storage
    elif (next == 'corridor'):
      self.state = self.corridor
    elif (next == 'armoury'):
      self.state = self.armoury
    elif (next == 'key'):
      self.state = self.key
    elif (next == 'boss'):
      self.state = self.boss
    else:
      print "Unrecognised state, quitting."
      self.exit = True

# Start up the Text Based Game engine
game = TextBased()

# Run!
game.run()
