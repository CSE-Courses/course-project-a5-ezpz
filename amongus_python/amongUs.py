import sys
import pygame
from client import Client
from pygame import mixer
import random




TIMEOUT = 4  # number of seconds until timeout
clock = pygame.time.Clock()

# timer
current_time = 0

current_time = pygame.time.get_ticks()
print(current_time)
#########################################################################################################################################
class Lobby():

    def __init__(self, w, h, name="None"):
        self.screen = pygame.display.set_mode((w, h))
        pygame.display.set_caption(name)
        self.width = w
        self.height = h
        self.walls = []

    def getLobby(self):
        return self.screen

    def drawLobbyBackground(self):
        #Place background image for lobby
        self.screen.fill((0, 0, 1))
        self.bg_img = pygame.image.load('Images/lobbyShip.png') #653x584
        self.screen.blit(self.bg_img, (375,0), self.bg_img.get_rect())
        #draw walls for lobby
        wall = Wall(365, 0, 10, 584) #left wall
        self.walls.append(wall)
        wall = Wall(1038, 0, 10, 584) #right wall
        self.walls.append(wall)
        wall = Wall(375, 584, 653, 10) #bottom wall
        self.walls.append(wall)
        for wall in self.walls:
            pygame.draw.rect(self.screen, ((0, 0, 1)), wall.rect)
        #myfont = pygame.font.SysFont("monspace", 20)
        #self.screen.blit(self.button, self.button.get_rect())

    def drawLobbyBackground2(self):
        # Place background image for lobby
        self.bg_img = pygame.image.load('Images/starz.png')
        self.screen.blit(self.bg_img, self.bg_img.get_rect())
        # myfont = pygame.font.SysFont("monspace", 20)
        # self.screen.blit(self.button, self.button.get_rect())

########################################################################################################################################


class Map():

    def __init__(self, w, h, name="None"):
        self.screen = pygame.display.set_mode((w, h))
        pygame.display.set_caption(name)
        self.width = w
        self.height = h
        self.walls = []

    def getMap(self):
        return self.screen

    #makes window black and then draws the map walls
    def drawMapBackground(self):
        #fills window with black
        self.screen.fill((0, 0, 1))
        #walls holds every wall instance
        #walls at borders of window
        wall = Wall(1356, 0, 10, 768)
        self.walls.append(wall)
        wall = Wall(0, 758, 1366, 10)
        self.walls.append(wall)
        wall = Wall(0, 0, 10, 768)
        self.walls.append(wall)
        wall = Wall(0, 0, 1366, 10)
        self.walls.append(wall)
        #top left room (spawn)
        wall = Wall(0, 192, 80, 10)
        self.walls.append(wall)
        wall = Wall(145, 192, 80, 10)
        self.walls.append(wall)
        wall = Wall(225, 0, 10, 202)
        self.walls.append(wall)
        #top right room
        wall = Wall(960, 160, 406, 10)
        self.walls.append(wall)
        wall = Wall(960, 60, 10, 110)
        self.walls.append(wall)
        #middle room
        wall = Wall(350, 250, 200, 10)
        self.walls.append(wall)
        wall = Wall(620, 250, 390, 10)
        self.walls.append(wall)
        wall = Wall(350, 250, 10, 350)
        self.walls.append(wall)
        wall = Wall(350, 590, 590, 10)
        self.walls.append(wall)
        wall = Wall(1000, 250, 10, 350)
        self.walls.append(wall)
        #bottom right room
        wall = Wall(1100, 590, 140, 10)
        self.walls.append(wall)
        wall = Wall(1310, 590, 56, 10)
        self.walls.append(wall)
        wall = Wall(1100, 590, 10, 178)
        self.walls.append(wall)
        #bottom left room
        wall = Wall(0, 330, 120, 10)
        self.walls.append(wall)
        wall = Wall(110, 330, 10, 348)
        self.walls.append(wall)
        wall = Wall(110, 670, 700, 10)
        self.walls.append(wall)
        wall = Wall(800, 670, 10, 30)

        self.walls.append(wall)

        """
        self.button1 = Button(100, 100, 950, 350, Game.map, "red")  # voting buttons
        self.button2 = Button(100, 100, 950, 400, Game.map, "blue")
        self.button3 = Button(100, 100, 950, 450, Game.map, "cyan")
        self.button4 = Button(100, 100, 950, 500, Game.map, "orange")
        """


        # Voting boxes
        pygame.draw.rect(self.screen, (50, 50, 50), [1500, 250, 140, 40])
        pygame.draw.rect(self.screen, (50, 50, 50), [1500, 300, 140, 40])
        pygame.draw.rect(self.screen, (50, 50, 50), [1500, 350, 140, 40])
        pygame.draw.rect(self.screen, (50, 50, 50), [1500, 400, 140, 40])



        for wall in self.walls:
            pygame.draw.rect(self.screen, ((192, 192, 192)), wall.rect)



########################################################################################################################################
# wall class that takes coordinates, width, and height to make rectangle
class Wall(object):
    def __init__(self, x, y, w, h):
        super(Wall, self).__init__()
        self.image = pygame.Surface([w, h])
        self.image.fill((192, 192, 192))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y




########################################################################################################################################
class Player(object):


    def __init__(self, startx, starty, w, h, color, colorDead):
        #pygame.sprite.Sprite.__init__(self)
        self.rect = pygame.Rect(w, w, h, h)
        self.rect.x = startx
        self.rect.y = starty
        self.rate = 2
        self.height = h  # 48pixels
        self.width = w  # 36pixels
        self.screen = pygame.display.set_mode((w, h))
        self.color = color  # color is not a string it is a pygame.Surface type containing the .png file that will produce character
        self.dead = colorDead
        self.voted = "no vote"
        self.status = "alive"
        self.username = "player 1"
        self.role = "crewmate"

        self.place = object


        self.images = [pygame.image.load(self.color).convert_alpha(), pygame.image.load(self.dead).convert_alpha()]
        self.current_image = self.images[0]

    # directKey parameter will be used to move player instance in certain direction
    def move(self, directKey):
        if directKey == 0:  # right
            self.rect.x = self.rect.x + self.rate
        elif directKey == 1:  # left
            self.rect.x = self.rect.x - self.rate
        elif directKey == 2:  # up
            self.rect.y = self.rect.y - self.rate
        else:  # down
            self.rect.y = self.rect.y + self.rate

        #checks for wall collision and stops player if necessary
        for wall in self.place.walls:
            if self.rect.colliderect(wall.rect):
                if (directKey == 0):
                    self.rect.right = wall.rect.left
                if (directKey == 1):
                    self.rect.left = wall.rect.right
                if (directKey == 2):
                    self.rect.top = wall.rect.bottom
                if (directKey == 3):
                    self.rect.bottom = wall.rect.top


    def draw(self, player):

        self.screen.blit(self.current_image, (self.rect.x, self.rect.y))  # params converted image, starting positions of characters



########################################################################################################################################
class Enemy(pygame.sprite.Sprite):

    def __init__(self, startx, starty, w, h, end, color, colorDead):
        pygame.sprite.Sprite.__init__(self)
        self.x = startx
        self.y = starty
        self.height = h  # 48pixels
        self.width = w  # 36pixels
        self.end = end
        self.path = [self.x, self.end]  # represents where we are starting and where we are ending
        self.walkCount = 0
        self.rate = 2
        self.screen = pygame.display.set_mode((w, h))
        self.color = color  # color is not a string it is a pygame.Surface type containing the .png file that will produce character
        self.dead = colorDead

        self.images = [pygame.image.load(self.color).convert_alpha(), pygame.image.load(self.dead).convert_alpha()]
        self.current_image = self.images[0]

    def moveX(self):
        if self.rate > 0:
            if self.x + self.rate < self.path[1]:
                self.x = self.x + self.rate
            else:
                self.rate = self.rate * -1
                self.walkCount = 0
        else:
            if self.x - self.rate > self.path[0]:
                self.x = self.x + self.rate
            else:
                self.rate = self.rate * -1
                self.walkCount = 0

    def draw(self, g):
        if self.current_image == self.images[0]:
            self.moveX()
        self.screen.blit(self.current_image, (self.x, self.y))  # params converted image, starting positions of characters


##############################################################################################################################


class Button():
    def __init__(self, w, h, x, y, Lobby, text=""):
        self.width = w
        self.height = h
        self.posx = x
        self.posy = y
        self.screen = pygame.display.set_mode((w, h))
        self.Lobby = Lobby
        self.text = text

    def draw(self):
        # rect = pygame.draw.rect(self.screen, (0,200,0), (150, 550, 100, 50))
        # self.screen.blit(rect, (self.posx, self.posy))
        pygame.draw.rect(self.Lobby.getLobby(), (0, 200, 0), (150, 500, 100, 50))

##############################################################################################################################

class Label():
    def __init__(self, xCoord, yCoord, text, fontSize, Lobby):
        self.x = xCoord
        self.y = yCoord
        self.text = text
        self.size = fontSize
        self.lobby = Lobby

        self.colors = [ (255, 255, 255), (0, 0, 0)]
        self.current = self.colors[0]


    def draw(self):
        font = pygame.font.Font(None, self.size)
        label = font.render(self.text, 1, self.current)
        self.lobby.getLobby().blit(label, (self.x, self.y))


##############################################################################################################################


class Game():
    clock = pygame.time.Clock()  # create an object to help track time
    #started will be true if enter is pressed to start the game
    started = False


    def __init__(self, w, h, mapw, maph):
        self.width = w
        self.height = h
        self.mapwidth = mapw
        self.mapheight = maph
        self.network = Client()
        self.player1 = Player(435, 75, 36, 48, 'Images/cyan.png', 'Images/cyanDead.png')  # Initializing Player class instance at set point(40,40) in map
        self.player2 = Player(450, 50, 36, 48, 'Images/orange.png', 'Images/orangeDead.png')  # Initializing Player class instance at set point(300,300) in map
        self.enemy1 = Enemy(435, 150, 36, 48, 495, 'Images/blue.png', 'Images/blueDead.png')  # Initializing Player class instance at set point(100,100)
        self.lobby = Lobby(self.width, self.height, "Version 1.0")  # Creating Lobby class instance

        self.player1.place = self.lobby
        self.player2.place = self.lobby

        self.botLabel = Label(1030, 300, "BlueBot in game", 20, self.lobby)
        self.p1Label = Label(1030, 315, "Player1 has joined", 20, self.lobby)
        self.p2Label = Label(1030, 330, "Player2 has joined", 20, self.lobby)

        self.player_list = []
        self.vote_tracker = []

        """
        self.button1 = Button(100, 100, 950, 350, self.lobby, "red") #voting buttons
        self.button2 = Button(100, 100, 950, 400, self.lobby, "blue")
        self.button3 = Button(100, 100, 950, 450, self.lobby, "cyan")
        self.button4 = Button(100, 100, 950, 500, self.lobby, "orange")
        """


    # will get info from server in a form we can understand so we can then draw the other character
    @staticmethod
    def parseData(data):
        try:
            arr = data.split(":")[1].split(",")
            return int(arr[0]), int(arr[1])
        except:
            return -1, -1

    # this is what will send ur current position in certain form to the server
    def sendData(self):
        data = str(self.network.id) + ":" + str(self.player1.rect.x) + "," + str(self.player1.rect.y)
        reply = self.network.sendData(data)
        return reply

    """
    def interrupted(signum, frame):
        # Called when the text input times out
        print("Interrupted")
    signal.signal(signal.SIGALRM, interrupted)
    """

    def add_player(self, player):
        self.player_list.append(player)

    def assign_roles(self):
        random.shuffle(self.player_list)
        self.player_list[0].role = "impostor"

    def playerDead(self, username):
        index = self.getPlayerIndex(username)
        self.player_list[index].status = "dead"
        if (self.player_list[index].role == "impostor"):
            self.crewmate_win()
        self.checkDeathWin()


    def set_vote_tracker(self):
        if len(self.vote_tracker) == 0:
            self.vote_tracker.clear()
        players = len(self.player_list)
        i = 0
        while (not (i == players)):
            self.vote_tracker.append(0)

    def getPlayerIndex (self, username):
        return self.player_list.index(username)

    def vote(self, voter):
        if (voter.voted == "skip"):
            self.vote_tracker[len(self.player_list) + 1] = self.vote_tracker[len(self.player_list) + 1] + 1
            voter.voted = "no vote"
        elif (voter.voted == "no vote"):
            voter.voted = "no vote"
        else:
            self.vote_tracker[self.getPlayerIndex(voter.voted)] = self.vote_tracker[self.getPlayerIndex(voter.voted)] + 1

    def applyVotes(self):
        i = 0
        while (not (i == len(self.player_list))):
            if (self.player_list[i].status == "alive"):
                self.vote(self.player_list[i])
            i = i + 1

    def tallyVotes(self):
        tied = True
        current_champ = 0
        current_champ_votes = 0
        i = 0
        while (i < len(self.vote_tracker)):
            if (self.vote_tracker[i] > current_champ_votes):
                current_champ = i
                current_champ_votes = self.vote_tracker[i]
                tied = False
                i= i + 1
            elif (self.vote_tracker[i] == current_champ_votes):
                tied = True
                i = i + 1
            else:
                i = i + 1
        if (not tied and not (current_champ == len(self.player_list))):
            self.playerDead(self.player_list[current_champ].username)

    def checkDeathWin(self, username):
        number_of_players = len(self.player_list)
        alive_crewmates = 0
        i = 0
        while (i < number_of_players):
            if (self.player_list[i].status == "alive" and self.player_list[i].role == "crewmate"):
                alive_crewmates = alive_crewmates + 1
            i = i + 1
        if (alive_crewmates == 1):
            self.impostor_win()

    def crewmate_win(self):
        print("crewmates win")

    def impostor_win(self):
        print("impostor win")





    def run(self):
        running = True
        self.add_player(self.player1)
        self.add_player(self.player2)
        # self.add_player(self.enemy1)
        self.assign_roles()
        msg_bool = False  # boolean for if theres a message
        p1_input = 'a'
        p1_bytes = ''
        while running:
            self.clock.tick(60)  # once per frame, the program will never running at more than 60 fps.self.started = True

            # Properly quit (pygame will crash without this)
            for event in pygame.event.get():
                # If closed out, quit program
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:

                    # If key pressed is ESC key, quit program
                    if event.key == pygame.K_ESCAPE:
                        running = False
                    # If enter is pressed, lobby will close and game will start
                    if event.key == pygame.K_RETURN:
                        self.started = True
                        running = False

            # making character move
            keys = pygame.key.get_pressed()
            if keys[pygame.K_RIGHT]:
                if self.player1.rect.x <= self.width - self.player1.rate:
                    self.player1.move(0)
            if keys[pygame.K_LEFT]:
                if self.player1.rect.x >= self.player1.rate:
                    self.player1.move(1)
            if keys[pygame.K_UP]:
                if self.player1.rect.y >= self.player1.rate:
                    self.player1.move(2)
            if keys[pygame.K_DOWN]:
                if self.player1.rect.y <= self.height - self.player1.rate:
                    self.player1.move(3)
            """     
            if keys[pygame.K_0]:
                p1_input = input("enter an input :")
                # p1_text = font.render("player 1: " + p1_input, 1, (255, 255, 255)) # player 1 text
                msg_bool = True
                print(msg_bool)
            """
            # Send Network data
            self.player2.rect.x, self.player2.rect.y = self.parseData(self.sendData())

            # Update Lobby
            pygame.init()  # initialize pygame, needed to create fonts, etc.
            self.lobby.drawLobbyBackground()
            self.player1.draw(self.lobby.getLobby())
            self.player2.draw(self.lobby.getLobby())
            self.enemy1.draw(self.lobby.getLobby())
            #Joined labels for each player that state player has entered lobby
            self.botLabel.draw()
            self.p1Label.draw()
            self.p2Label.draw()

            #ENTER LABEL PLACED IN LOBBY TO ENTER GAME#
            #pygame.init()

            """
            pygame.mixer.init()
            pygame.mixer.music.load('Images/audio.wav')
            pygame.mixer.music.play(0)
            """

            font = pygame.font.Font(None, 30)
            enterLabel = font.render("Press 'Enter' when all players have joined.", 1, (255, 255, 255))
            self.lobby.getLobby().blit(enterLabel, (495, 457))


            #FADING OUT JOINED LABELS IF NUM KEY 1 PRESSED
            if keys[pygame.K_1]:
                self.botLabel.current = self.botLabel.colors[1]
                self.p1Label.current = self.p1Label.colors[1]
                self.p2Label.current = self.p2Label.colors[1]
                pygame.display.flip()



            #KILLING CHARACTERS#
            #press 2 on keyboard to transform player2 to dead image
            if keys[pygame.K_2]:
                self.player2.current_image = self.player2.images[1]
                pygame.display.flip()
            # press 3 on keyboard to transform 3rd player aka enemy1 to dead image
            if keys[pygame.K_3]:
                self.enemy1.current_image = self.enemy1.images[1]
                pygame.display.flip()


            # CHAT BOX SHIT#
            # signal.alarm(TIMEOUT)
            font = pygame.font.Font(None, 30)
            if keys[pygame.K_0]:
                p1_input = input("enter an input :")
            #else:
                #p1_input = ""
            print(p1_input) # Test, prints current output
            p1_text = font.render("player: " + p1_input, 1, (255, 255, 255)) # player 1 text
            self.lobby.getLobby().blit(p1_text, (15, 20))
            #signal.alarm(0) # Disable alarm after success

            """
            if msg_bool:
                print(msg_bool)
                print("delivered")
                print(p1_input)
                p1_text = font.render("player 1: ", 1, (255, 255, 255))  # player 1 text
                #self.lobby.getLobby().blit(p1_text, (150, 2)) # Display
                p1_bytes = bytes("wow", 'ascii')
                scoretext = font.render(p1_bytes, 1, (255, 255, 255))
                self.lobby.getLobby().blit(scoretext, (150, 457))
                msg_bool = False
                #print(p1_text)
                #print(msg_bool)
            """
            pygame.display.update()

        #started will be true if enter has been pressed
        if not self.started:
            pygame.quit()
        else:
            Game.rungame(self)


    global isBlueDead
    isBlueDead = False  # Boolean to check if blue is dead
    #runs the actual game
    def rungame(self):
        global isBlueDead
        global called
        called = 0 #only call simon says once
        simon = "Error no one left to call the shots" #player who is simon

        running = True
        #creates the game map
        self.map = Map(self.mapwidth, self.mapheight, "Version 1.0")

        #place gets accurate walls
        self.player1.place = self.map
        self.player2.place = self.map
        self.player1.rect.x = 30
        self.player1.rect.y = 30

        """
        self.button1 = Button(100, 100, 950, 350, self.map, "red")  # voting buttons
        self.button2 = Button(100, 100, 950, 400, self.map, "blue")
        self.button3 = Button(100, 100, 950, 450, self.map, "cyan")
        self.button4 = Button(100, 100, 950, 500, self.map, "orange")
        """

        msg_bool = False  # boolean for if theres a message
        self.assign_roles()
        p1_input = 'a'
        p1_bytes = ''
        start_ticks = pygame.time.get_ticks()  # start timer
        max_time = 30 # set max time
        vote = 2
        labelx = 50
        while running:
            self.clock.tick(60)  # once per frame, the program will never running at more than 60 fps.self.started = True

            # Properly quit (pygame will crash without this)
            for event in pygame.event.get():
                # If closed out, quit program
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    # If key pressed is ESC key, quit program
                    if event.key == pygame.K_ESCAPE:
                        running = False

            # making character move
            keys = pygame.key.get_pressed()
            if keys[pygame.K_RIGHT]:
                if self.player1.rect.x <= self.width - self.player1.rate:
                    self.player1.move(0)
            if keys[pygame.K_LEFT]:
                if self.player1.rect.x >= self.player1.rate:
                    self.player1.move(1)
            if keys[pygame.K_UP]:
                if self.player1.rect.y >= self.player1.rate:
                    self.player1.move(2)
            if keys[pygame.K_DOWN]:
                if self.player1.rect.y <= self.height - self.player1.rate:
                    self.player1.move(3)
            """     
            if keys[pygame.K_0]:
                p1_input = input("enter an input :")
                # p1_text = font.render("player 1: " + p1_input, 1, (255, 255, 255)) # player 1 text
                msg_bool = True
                print(msg_bool)
            """
            # Send Network data
            self.player2.rect.x, self.player2.rect.y = self.parseData(self.sendData())

            # Update map
            self.map.drawMapBackground()
            self.player1.draw(self.map.getMap())
            self.player2.draw(self.map.getMap())
            self.enemy1.draw(self.map.getMap())

            # ENTER LABEL PLACED IN LOBBY TO ENTER GAME#
            pygame.init()  # initialize pygame
            font = pygame.font.Font(None, 30)
            enterLabel = font.render("", 1, (255, 255, 255))
            self.map.getMap().blit(enterLabel, (500, 457))

            eLabel = font.render(self.player1.role, 1, (255, 255, 255))
            self.map.getMap().blit(eLabel, (500, labelx))
            labelx = labelx - 3


            # KILLING CHARACTERS#
            # press 2 on keyboard to transform player2 to dead image
            if keys[pygame.K_2]:
                self.player2.current_image = self.player2.images[1]
                pygame.display.flip()
            # press 3 on keyboard to transform 3rd player aka enemy1 to dead image
            if keys[pygame.K_3]:
                self.enemy1.current_image = self.enemy1.images[1]
                pygame.display.flip()
                isBlueDead = True # set boolean to true
            print("Is blue dead")
            print(isBlueDead)

            # CHAT BOX SHIT#
            # signal.alarm(TIMEOUT)
            if keys[pygame.K_0]:
                p1_input = input("enter an input :")
            # else:
            # p1_input = ""
            print(p1_input)  # Test, prints current output
            p1_text = font.render("player: " + p1_input, 1, (255, 255, 255))  # player 1 text
            self.map.getMap().blit(p1_text, (15, 800))

            # signal.alarm(0) # Disable alarm after success
            # Code for Displaying the mission prompts
            mission = 7
            mision_prompt = 'mission: '
            mission_text = ''
            random_num = 1  # for simon says assignment

            if (mission == 1):
                print("mission: 1")
                mission_prompt = "Move to your colored circle"
                pygame.draw.circle(self.lobby.getLobby(), (255, 0, 0), (700, 300), 25)  # Red circle
                pygame.draw.circle(self.lobby.getLobby(), (0, 0, 255), (700, 400), 25)  # Blue circle
                pygame.draw.circle(self.lobby.getLobby(), (255, 140, 0), (800, 300), 25)  # Orange circle
                pygame.draw.circle(self.lobby.getLobby(), (0, 255, 255), (800, 400), 25)  # cyan circle

            elif (mission == 2):
                print("mission: 2")
                mission_prompt = "Go to the bottom right corner of the screen"
            elif (mission == 3):
                print("mission: 3")
                mission_prompt = "Use the movement keys to do a dance party"
            elif (mission == 4):
                print("mission: 4")
                mission_prompt = "Type your favorite color in the chat"
            elif (mission == 5):
                print("mission: 5")
                mission_prompt = "Type a meaningful number in the cha"
            elif (mission == 6):
                print("mission: 6")
                mission_prompt = "Type your favorite beverage in the chat"
            elif (mission == 7):
                print("mission: 7")
                print("called = " + str(called))
                if called == 0:
                    random_num = random.randint(1, 2)
                    print(random_num)
                    number_of_players = len(self.player_list)
                    alive_players = 0
                    i = 0
                    while (i < number_of_players):
                        if (self.player_list[i].status == "alive"):
                            alive_players = alive_players + 1
                            print(self.player_list[i].color)
                            if (self.player_list[i].color == "Images/cyan.png" and random_num == 1):
                                simon = "Cyan is the simon"
                                break
                            elif (self.player_list[i].color == "Images/orange.png" and random_num == 2):
                                simon = "Orange is the simon"
                                break

                        i = i + 1

                mission_prompt = "Simon says, Type commands in chat, others follow when simon says; " + simon
                called = 1
            elif (mission == 8):
                print("mission: 8")
                mission_prompt = "Stand in a line"
            else:
                print("mission: 9")
                mission_prompt = "Go to the left of the screen and race to the right of the screen"

            mission_text = font.render(mission_prompt, 1, (255, 255, 255))  # player 1 text

            self.lobby.getLobby().blit(mission_text, (625, 800))

            # Voting labels
            red_text = font.render("red", 1, (255, 255, 255))  # player 1 text
            self.lobby.getLobby().blit(red_text, (1530, 260))
            blue_text = font.render("blue", 1, (255, 255, 255))  # player 1 text
            self.lobby.getLobby().blit(blue_text, (1530, 310))
            cyan_text = font.render("cyan", 1, (255, 255, 255))  # player 1 text
            self.lobby.getLobby().blit(cyan_text, (1530, 360))
            orange_text = font.render("orange", 1, (255, 255, 255))  # player 1 text
            self.lobby.getLobby().blit(orange_text, (1530, 410))

            if ((vote % 2) == 0):
                vote_text = font.render("vote", 1, (255, 255, 255))  # player 1 text
                self.lobby.getLobby().blit(vote_text, (1530, 200))

            else:
                vote_text = font.render("vote", 1, (0, 255, 0))  # set vote text to green
                self.lobby.getLobby().blit(vote_text, (1530, 200))
                number_of_players = len(self.player_list)
                alive_players = 0
                i = 0
                while (i < number_of_players):
                    if (self.player_list[i].status == "alive"):
                        alive_players = alive_players + 1
                        print(self.player_list[i].color)
                        if (self.player_list[i].color == "Images/cyan.png"):
                            cyan_text = font.render("cyan", 1, (0, 255, 255))  # player 1 text
                            self.lobby.getLobby().blit(cyan_text, (1530, 360))
                        elif (self.player_list[i].color == "Images/orange.png"):
                            orange_text = font.render("orange", 1, (255, 160, 0))  # player 1 text
                            self.lobby.getLobby().blit(orange_text, (1530, 410))
                        if not isBlueDead:
                            blue_text = font.render("blue", 1, (0, 0, 255))  # player 1 text
                            self.lobby.getLobby().blit(blue_text, (1530, 310))
                    i = i + 1

            # Timer
            seconds = (pygame.time.get_ticks() - start_ticks) / 1000  # calculate how many seconds

            # print(seconds) #print how many seconds
            print(int(max_time - seconds))  # debug
            diff = int(max_time - seconds)
            if (diff < 0):
                # start_ticks = 0
                max_time += 30
                vote += 1
            time_diff = "timer: " + str(diff)
            timer_text = font.render(time_diff, 1, (255, 255, 255))  # player 1 text
            self.lobby.getLobby().blit(timer_text, (1500, 150))

            """
            if msg_bool:
                print(msg_bool)
                print("delivered")
                print(p1_input)
                p1_text = font.render("player 1: ", 1, (255, 255, 255))  # player 1 text
                #self.lobby.getLobby().blit(p1_text, (150, 2)) # Display
                p1_bytes = bytes("wow", 'ascii')
                scoretext = font.render(p1_bytes, 1, (255, 255, 255))
                self.lobby.getLobby().blit(scoretext, (150, 457))
                msg_bool = False
                #print(p1_text)
                #print(msg_bool)
            """

            pygame.display.update()

        pygame.quit()

        #########################################################################################################################################################################################################################################

################################################################################################################################################################################################################################################################################