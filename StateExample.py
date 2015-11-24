import re

class MainHall:
  def __init__(self, game):
    # We need this for game context (exit, items)
    self.game = game
    # Regular expressions to match ser response
    self.left = re.compile('left', re.IGNORECASE)
    self.right = re.compile('right', re.IGNORECASE)
    # No recognised action comes back here
    self.nextState = 'hall' # no recognised action comes back here

  # Main logic of this state / room
  def run(self):
    print "You're in the main hall. You can go left or right."
    action = raw_input("$ ")
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
    # Regular expressions to match ser response
    self.back = re.compile('back', re.IGNORECASE)
    self.pick = re.compile('pick up', re.IGNORECASE)
    self.kick = re.compile('kick', re.IGNORECASE)
    # No recognised action comes back here
    self.nextState = 'storage' # no recognised action comes back here

  # Main logic of this state / room
  def run(self):
    print "This is the storage. There is a torch and lots or rats."
    action = raw_input("$ ")
    if (self.back.match(action)):
      self.nextState = 'hall'
    elif (self.pick.match(action)):
      if (self.game.items.count('torch')):
        print "You already have the torch"
      else:
        self.game.items.append('torch')
        print "You've picked the torch"
    elif (self.kick.match(action)):
      print "You kicked a rat and it squealed loudly"

  # Returns the next state (which could still be this one)
  def next(self):
    return self.nextState

# State: Corridor
class Corridor:
  def __init__(self, game):
    # We need this for game context (exit, items)
    self.game = game
    # Regular expressions to match ser response
    self.back = re.compile('back', re.IGNORECASE)
    # No recognised action comes back here
    self.nextState = 'corridor'

  # Main logic of this state / room
  def run(self):
    if (self.game.items.count('torch')):
      print "This is the corridor. You can see some doors, but you can't go through them now. Cry."
      self.game.exit = True
    else:
      print "It's too dark in here, you better go back."
      action = raw_input("$ ")
      if (self.back.match(action)):
        self.nextState = 'hall'

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
    # Initialise the items list
    self.items = list()
    # Exit condition (states set this to quit)
    self.exit = False
    # Current state
    self.state = self.hall

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
    elif (next == 'corridor'):
      self.state = self.corridor
    elif (next == 'storage'):
      self.state = self.storage
    else:
      print "Unrecognised state, quitting."
      self.exit = True

# Start up the Text Based Game engine
game = TextBased()

# Run!
game.run()
